import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
dynamodb = boto3.resource('dynamodb')


# TRADUCCIÓN A ESPAÑOL

def traducir_es(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
   
    )

    item = result['Item']
    texto = item['text']

    translate = boto3.client(service_name='translate',region_name='us-east-1',use_ssl=True)
   # resultado = translate.translate_text(Text='Hello', SourceLanguageCode='en',TargetLanguageCode='es')
    resultado = translate.translate_text(Text=texto, SourceLanguageCode='en',TargetLanguageCode='es')
     
    
    
    # create a response
    response = {
        "statusCode": 200,
       # "body": json.dumps(result['Item'],
       #                    cls=decimalencoder.DecimalEncoder) + ' La traducción es ' + resultado.get('TranslatedText') + '   
        "body": json.dumps(resultado)
       
       
    }

    return response
    
    # TRADUCCIÓN A FRANCES

def traducir_fr(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
   
    )

    item = result['Item']
    texto = item['text']

    translate = boto3.client(service_name='translate',region_name='us-east-1',use_ssl=True)
   # resultado = translate.translate_text(Text='Hello', SourceLanguageCode='en',TargetLanguageCode='es')
    resultado = translate.translate_text(Text=texto, SourceLanguageCode='en',TargetLanguageCode='es')
     
    
    
    # create a response
    response = {
        "statusCode": 200,
       # "body": json.dumps(result['Item'],
       #                    cls=decimalencoder.DecimalEncoder) + ' La traducción es ' + resultado.get('TranslatedText') + '   
        "body": json.dumps(resultado)
       
       
    }

    return response