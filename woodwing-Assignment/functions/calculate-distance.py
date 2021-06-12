import json

x=0
y=0

def distanceAddition(event, context):
    print(event)
    http_method = event['httpMethod']
    
    if http_method == 'GET' :
        x = int(event['queryStringParameters']['x'])
        y = int(event['queryStringParameters']['y'])
        
    elif http_method == 'POST':
        body = json.loads(event['body'])
        x = body['x']
        y = body['y']
    

    return {
        'statusCode': 200,
        'body': json.dumps(calculate(x,y))
   }

def calculate(x,y):
    result = 0
    result = x + y
    
    return result