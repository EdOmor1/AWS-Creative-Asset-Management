import boto3

rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

def process_asset(bucket, key):
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        MaxLabels=10
    )
    labels = response['Labels']
    tag_asset(bucket, key, labels)

def tag_asset(bucket, key, labels):
    tag_set = [{'Key': label['Name'], 'Value': str(label['Confidence'])} for label in labels]
    s3.put_object_tagging(
        Bucket=bucket,
        Key=key,
        Tagging={
            'TagSet': tag_set
        }
    )
