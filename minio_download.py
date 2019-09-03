from minio import Minio

client = Minio('10.0.2.1:23760',
               access_key='centurion',
               secret_key='BlueVVat3r',
               secure=False)

client.fget_object(bucket_name='ds-container-files', object_name='clean.zip',
                   file_path='/mnt/mesos/sandbox/jupyter-data/clean.zip')
