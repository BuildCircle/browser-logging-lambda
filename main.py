import json

def lambda_handler(event, context):
    error = json.loads(event['body'])
    stack = error['stack']
    formattedStack = stack.replace("\n","\r")
    print(f"{formattedStack}")
    return {
        'statusCode': 200,
        'body': json.dumps('Logged')
    }
