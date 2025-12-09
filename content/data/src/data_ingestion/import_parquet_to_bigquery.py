#!/usr/bin/env python
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

# Author: Wissem Khlifi, Fabian Hirschmann
from pyspark.sql import SparkSession

project_id = "astute-ace-336608"
gcs_parquet_path = f"gs://{project_id}-bucket/data/parquet/ulb_fraud_detection/"
bq_dataset_name = "ml_datasets"
bq_table_name = "ulb_fraud_detection_dataproc"
temporary_gcs_bucket = f"gs://{project_id}-bucket"

# Create a SparkSession
spark = SparkSession.builder.appName("bigquery_to_gcs_parquet").getOrCreate()

# Read Parquet Files from GCS
df = spark.read.parquet(gcs_parquet_path)

# Write DataFrame to BigQuery
(
    df.write.format("bigquery")
    .option("table", f"{project_id}:{bq_dataset_name}.{bq_table_name}")
    .option("temporaryGcsBucket", temporary_gcs_bucket)
    .mode("overwrite")
    .save()
)

spark.stop()
