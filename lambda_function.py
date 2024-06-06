import json
import os

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'pass': os.environ['passcode'],
        'mydata': os.environ['mydata'],
        'new_var': os.environ['new_var']
    }
