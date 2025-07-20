import boto3
import json
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        message = body['message']
        subject = body.get('subject', 'Notification from SNS Lambda')

        # Use environment variable for SNS Topic ARN
        topic_arn = os.environ['SNS_TOPIC_ARN']

        response = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Notification sent!', 'sns_response': response})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
