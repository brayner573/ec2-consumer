# Importa el módulo boto3, que es el SDK de AWS para Python.
# Permite interactuar con servicios como S3, Lambda y EC2.
# Importa el módulo boto3, que es el SDK de AWS para Python.
# Permite interactuar con servicios como S3, Lambda y EC2.
import boto3
import os

def main():
    s3 = boto3.client('s3')

    bucket_name = 's3-data-salida-covid-brayner573'
    local_file = 'data_transformada.json'
    s3_key = 'data_transformada.json'

    try:
        s3.head_object(Bucket=bucket_name, Key=s3_key)
        print("El archivo ya existe en S3. No se subirá de nuevo.")
    except:
        print("El archivo no existe en S3. Subiendo...")
        s3.upload_file(local_file, bucket_name, s3_key)
        print("Subido correctamente.")

if __name__ == '__main__':
    main()
