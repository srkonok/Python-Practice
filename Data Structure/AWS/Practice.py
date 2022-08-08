import json

def lambda_handler(event, context):
    print(event)
    http_method=event['httpMethod']
    if http_method=='GET':
        first_num=int(event["queryStringParameters"]["first_num"])
        second_num=int(event["queryStringParameters"]["second_num"])
        operator=event["queryStringParameters"]["operator"]
    elif http_method=='POST':
        body=json.loads(event['body'])
        first_num=body['first_num']
        second_num=body['second_num']
        operator=body['operator']

    return {
        'statusCode': 200,
        'body': json.dumps(calculator(first_num,second_num,operator))
    }
def calculator(first_num,second_num,operator):
    result=0
    if operator=="add":
        result=first_num+second_num
    elif operator=="subtract":
        result=first_num-second_num
    elif operator=="multiply":
        result=first_num*second_num
    elif operator=="divide":
        if(second_num!=0):
            result=first_num/second_num
    return result
    http_method=event['httpMethod']
    if http_method=='GET':
        first_num=int(event['queryStringParameters']['first_num'])
        second_num=int(event['queryStringParameters']['second_num'])
       
    elif http_method=='POST':
        body=json.loads(event['body'])
        first_num=body['first_num']
        second_num=body['second_num']
       
    result=first_num+second_num