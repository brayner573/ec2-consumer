import boto3
import botocore
import os

def main():
    s3 = boto3.client('s3')
    bucket_name = 's3-data-salida-covid-brayner573'
    s3_key = 'data_transformada.json'
    local_file = 'data_transformada.json'

    try:
        # Verificar si el archivo ya existe en el bucket
        s3.head_object(Bucket=bucket_name, Key=s3_key)
        print(f"🟡 El archivo '{s3_key}' ya existe en S3. No se subirá de nuevo.")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"🔵 El archivo no existe en S3. Subiendo...")
            s3.upload_file(local_file, bucket_name, s3_key)
            print(f"✅ Archivo '{s3_key}' subido exitosamente.")
        else:
            raise

if __name__ == "__main__":
    main()
