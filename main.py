import boto3
import json
import os

def main():
    bucket_name = 's3-data-salida-covid-brayner573'
    s3_key = 'data_transformada.json'
    local_file = 'data_transformada.json'

    # 🔧 Simulación: crea el archivo local
    data = {
        "mensaje": "Archivo generado correctamente",
        "reglas_aplicadas": 20,
        "estado": "completado"
    }
    with open(local_file, 'w') as f:
        json.dump(data, f)

    # 🔐 Cliente S3
    s3 = boto3.client('s3')

    # 📤 Sube el archivo al bucket de salida
    s3.upload_file(local_file, bucket_name, s3_key)
    print(f"✅ Archivo '{local_file}' subido a S3 en '{bucket_name}/{s3_key}'")

if __name__ == '__main__':
    main()
