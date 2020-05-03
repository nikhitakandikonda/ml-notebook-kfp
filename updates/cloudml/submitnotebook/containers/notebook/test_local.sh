#!/bin/sh
docker run gcr.io/ma-poc-automation/submitnotebook:latest gs://hostedkfp-default-bmeiqdunw2/flights/notebook/flights_model.ipynb gs://hostedkfp-default-bmeiqdunw2/flights/notebook/flights_model_kfp.ipynb gs://hostedkfp-default-bmeiqdunw2/flights/notebook/params.yaml
