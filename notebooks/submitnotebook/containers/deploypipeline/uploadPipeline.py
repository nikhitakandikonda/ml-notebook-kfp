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
    model_bucket = dsl.PipelineParam('bucket')
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
    
def upload_pipeline(host)
    pipeline_func = flights_pipeline
    pipeline_filename = pipeline_func.__name__ + '.tar.gz'
    import kfp.compiler as compiler
    compiler.Compiler().compile(pipeline_func, pipeline_filename)
    client = kfp.Client(host=host)
    pipelines = client.list_pipelines()
    if 
    client.upload_pipeline(pipeline_filename, 'flights')
    
    
if __name__ == '__main__':
      logging.getLogger().setLevel(logging.INFO)
      parser = argparse.ArgumentParser()
      parser.add_argument('--bucket',
                          type=str,
                          required=True,
                          help='Bucket to store outputs.')
      parser.add_argument('--pipeline_host',
                          type=str,
                          default='',
                          help='host to deploy the pipeline')
      parser.add_argument('--model_name',
                          type=str,
                          default='',
                          help='model name')
      parser.add_argument('--model_version',
                          type=str,
                          default='',
                          help='model version')
      parser.add_argument('--pipeline_host',
                          type=str,
                          default='',
                          help='kubeflow pipeline host')


      args = parser.parse_args()
      
      upload_pipeline(args.pipeline_host)
        
      GCSDIR='gs://{}/flights/notebook'.format(BUCKET)
      arguments = {
            'model_name' : args.model_name,
            'model_version' : args.model_version,
            'model_bucket': args.bucket,
        }
        
        
      pipeline = kfp.Client(host=args.pipeline_host).create_run_from_pipeline_func(flights_pipeline, arguments=arguments)
