#!/bin/bash

# if [ "$#" -ne 3 ]; then
#     echo "Usage: ./deploy.sh  input_notebook output_notebook paramsfile"
#     exit
# fi

BUCKET=$1

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

mkdir working
cd working

git clone https://github.com/nikhitakandikonda/ml-notebook-kfp.git

cd notebooks
echo 'BUCKET: "$BUCKET"' >> params.yaml

papermill flights_model.ipynb output.ipynb -f params.yaml --log-output

cd ../..
rm -rf working


OUTDIR=gs://${BUCKET}/flights/trained_model
echo $OUTDIR > /output.txt