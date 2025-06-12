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
import joblib

import flask
import numpy as np
from google.cloud.aiplatform.utils import prediction_utils

AIP_STORAGE_URI = os.environ["AIP_STORAGE_URI"]
print(f"Downloading model from {AIP_STORAGE_URI}/model.joblib")
prediction_utils.download_model_artifacts(AIP_STORAGE_URI)
model = joblib.load("model.joblib")

app = flask.Flask(__name__)

@app.route(os.environ.get("AIP_PREDICT_ROUTE", "/predict"), methods=["POST"])
def predict():
    data = flask.request.get_json()
    inputs = np.array(data["instances"])
    predictions = model.predict(inputs).tolist()
    return flask.jsonify({"predictions": predictions})

@app.route(os.environ.get("AIP_HEALTH_ROUTE", "/health"), methods=["GET"])
def health_check():
    print("Received health check")
    return flask.jsonify({"status": "healthy"}), 200

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("AIP_HTTP_PORT", 8080)))
