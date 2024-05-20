import json
from asset_manager import process_asset

def lambda_handler(event, context):
    for record in event['Records']:
        s3 = record['s3']
        bucket = s3['bucket']['name']
        key = s3['object']['key']
        process_asset(bucket, key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Assets processed successfully!')
    }
