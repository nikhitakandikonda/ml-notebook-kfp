import kfp
import kfp.components as comp
import kfp.dsl as dsl


@dsl.pipeline(
   name='FlightsPipeline',
   description='Trains, deploys flights model'
)
def flights_pipeline(
        model_name = dsl.PipelineParam('modelname'),
    model_version = dsl.PipelineParam('version'),
    model_bucket = dsl.PipelineParam('params')
):
    notebookop = dsl.ContainerOp(
      name='flightsmodel',
      # image needs to be a compile-time string
      image='gcr.io/ma-poc-automation/submitnotebook:latest',
      arguments=[
        model_bucket
      ],
        file_outputs={'train': '/output.txt'}
    )
    
    deploy_cmle = dsl.ContainerOp(
      name='deploycmle',
      # image needs to be a compile-time string
      image='gcr.io/ma-poc-automation/notebook-deploycmle:latest',
      arguments=[
        notebookop.outputs['train'],  # modeldir
        model_name,
        model_version
      ],
      file_outputs={
        'model': '/model.txt',
        'version': '/version.txt'
      }
    )
    
def run_pipeline(bucket,host,):
    
    
if __name__ == '__main__':
      logging.getLogger().setLevel(logging.INFO)
      parser = argparse.ArgumentParser()
      parser.add_argument('--project',
                          type=str,
                          required=True,
                          help='The GCP project to run the dataflow job.')
      parser.add_argument('--bucket',
                          type=str,
                          required=True,
                          help='Bucket to store outputs.')
      parser.add_argument('--pipeline_host',
                          type=str,
                          default='',
                          help='host to deploy the pipeline')

      args = parser.parse_args()
        
      GCSDIR='gs://{}/flights/notebook'.format(BUCKET)
      arguments = {
            'model_name' : 'flights',
            'model_version' : 'flt_1',
            'model_bucket': BUCKET,
        }

      preprocess(args.bucket, args.pipeline_host)
