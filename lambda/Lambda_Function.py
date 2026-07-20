import boto3
import json

SNS = "arn:aws:sns:us-east-1:472125991512:event-notifications"

def get_file_deatils(event):
    record = event['Records'][0]
    file_deatils = {

        'bucket': record['s3']['bucket']['name'],
        'file'  : record['s3']['object']['key'],
        'size'  : record['s3']['object']['size'],
        'region':  record['awsRegion']
       
  
    }
    return file_deatils

def format_message(file_deatils):
    message = f"""
    ====================================
    NEW FILE UPLOADED
    ====================================
    File: {file_deatils['file']}
    Size: {file_deatils['size']} bytes
    Bucket: {file_deatils['bucket']}
    Region: {file_deatils['region']}
    ====================================
    """
    return message

def send_notification(message):
    sns = boto3.client('sns')
    sns.publish(
        TopicArn="arn:aws:sns:us-east-1:472125991512:event-notifications",
        Message=message,
        Subject='New S3 File Uploaded Alert'
    )
    print("Notofication sent !")

def lambda_handler (event, context):
   try:
        file_details = get_file_deatils(event)
        message = format_message(file_details)
        send_notification(message)

        return {
            'statusCode': 200,
            'body': json.dumps('Hello from S3 Notifier!')
        }

   except Exception as e:
        print(f"Error:{e}")
        raise 

