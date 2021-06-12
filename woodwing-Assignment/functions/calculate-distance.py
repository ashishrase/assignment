import json

#Function definition to get distance value in over the REST service
def distanceAddition(event, context):
    print(event)
    distanceX=0
    distanceY=0
    m1 = "meters"
    m2 = "m"
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        distanceX = int(event['queryStringParameters']['distanceX'])
        distanceY = int(event['queryStringParameters']['distanceY'])
        units = (event['queryStringParameters']['units'])      
    elif http_method == 'POST':
        body = json.loads(event['body'])
        distanceX = body['distanceX']
        distanceY = body['distanceX']
        units = body['units']
       
        
    if type(distanceX).__name__ != int or type(distanceY).__name__ != int :
	    if units != m1:
		    return("Currently Supporting only unit as meters")
	    else:
	       return {'statusCode': 200,'body': json.dumps(calculate(distanceX,distanceY,units))}
    else:
	    print("400 Invalid Operand")

#calculate defined 
def calculate(distanceX,distanceY,units):
    result=0
    result = distanceX + distanceY
    finalresult = str(result) + ' ' + units
    return finalresult
    
  