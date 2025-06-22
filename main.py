import boto3
import json
from datetime import datetime
s3 = boto3.client('s3')
bucket_name = 's3-data-salida-covid-brayner573'
local_file = 'data_transformada.json'
s3_key = 'data_transformada.json'

s3.upload_file(local_file, bucket_name, s3_key)
print(f"{local_file} subido a {bucket_name}/{s3_key}")

# Configura los valores del bucket
bucket_name = 's3-data-salida-covid-brayner573'
input_key = 'data_transformada.json'
log_key = f'logs/resumen-{datetime.utcnow().strftime("%Y%m%d-%H%M%S")}.json'

def main():
    s3 = boto3.client('s3')

    # Leer archivo JSON de entrada
    response = s3.get_object(Bucket=bucket_name, Key=input_key)
    content = response['Body'].read().decode('utf-8')
    data = json.loads(content)
    
    total_registros = len(data)

    print(f"Registros procesados: {total_registros}")

    # Crear resumen y guardarlo como log
    resumen = {
        "archivo_procesado": input_key,
        "registros": total_registros,
        "timestamp": datetime.utcnow().isoformat()
    }

    s3.put_object(
        Bucket=bucket_name,
        Key=log_key,
        Body=json.dumps(resumen).encode('utf-8')
    )

    print(f"Resumen guardado en: {log_key}")

if __name__ == "__main__":
    main()
