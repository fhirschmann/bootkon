# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import kfp
from kfp import dsl, compiler

from google.cloud import aiplatform
from google_cloud_pipeline_components.types import artifact_types
from google_cloud_pipeline_components.v1.custom_job import CustomTrainingJobOp
from google_cloud_pipeline_components.v1.endpoint import EndpointCreateOp, ModelDeployOp
from google_cloud_pipeline_components.v1.model import ModelUploadOp
from kfp.dsl import importer_node

PROJECT_ID = os.environ["PROJECT_ID"]
REGION = os.environ["REGION"]
TRAIN_IMAGE_URI = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/bootkon/bootkon-train:latest"
PREDICT_IMAGE_URI = f"{REGION}-docker.pkg.dev/{PROJECT_ID}/bootkon/bootkon-predict:latest"
PIPELINE_ROOT = f"gs://{PROJECT_ID}-bucket/pipelines"
BQ_SOURCE = f"{PROJECT_ID}.ml_datasets.ulb_fraud_detection_dataproc"

@kfp.dsl.pipeline(name="bootkon-pipeline")
def pipeline(
    bq_source: str,
    project: str
):
    model_dir = f"{PIPELINE_ROOT}/model-{kfp.dsl.PIPELINE_JOB_ID_PLACEHOLDER}"
    custom_job_task = CustomTrainingJobOp(
        project=project,
        display_name="bootkon-training-job",
        worker_pool_specs=[
            {
                "containerSpec": {
                    "args": [bq_source, project],
                    "env": [{"name": "AIP_MODEL_DIR", "value": model_dir}],
                    "imageUri": TRAIN_IMAGE_URI,
                },
                "replicaCount": "1",
                "machineSpec": {
                    "machineType": "n1-standard-4",
                },
            }
        ],
    )

    import_unmanaged_model_task = importer_node.importer(
        artifact_uri=model_dir,
        artifact_class=artifact_types.UnmanagedContainerModel,
        metadata={
            "containerSpec": {
                "imageUri": PREDICT_IMAGE_URI,
            },
        },
    ).after(custom_job_task)

    model_upload_op = ModelUploadOp(
        project=project,
        display_name="bootkon-model",
        unmanaged_container_model=import_unmanaged_model_task.outputs["artifact"],
    )
    model_upload_op.after(import_unmanaged_model_task)

    endpoint_create_op = EndpointCreateOp(
        project=project,
        display_name="bootkon-endpoint",
    )

    model_deploy_op = ModelDeployOp(
        endpoint=endpoint_create_op.outputs["endpoint"],
        model=model_upload_op.outputs["model"],
        deployed_model_display_name="bootkon-endpoint",
        dedicated_resources_machine_type="n1-standard-4",
        dedicated_resources_min_replica_count=1,
        dedicated_resources_max_replica_count=1
    )
    model_deploy_op.after(endpoint_create_op)


compiler.Compiler().compile(
    pipeline_func=pipeline,
    package_path="pipeline.json",
)

job = aiplatform.PipelineJob(
    display_name="bootkon-pipeline",
    template_path="pipeline.json",
    pipeline_root=PIPELINE_ROOT,
    enable_caching=False,
    project=PROJECT_ID,
    parameter_values={
        "project": PROJECT_ID,
        "bq_source": BQ_SOURCE
    },
)

job.run(sync=False)