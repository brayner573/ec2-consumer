import boto3
import json

bucket_name = 's3-data-salida-covid-brayner573'
json_key = 'data_transformada.json'

def main():
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=json_key)
    content = response['Body'].read().decode('utf-8')
    data = json.loads(content)

    # Aquí puedes aplicar lógica sobre los datos
    print("Total de registros procesados:", len(data))

if __name__ == "__main__":
    main()
