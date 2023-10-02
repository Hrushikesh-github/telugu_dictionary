import json
import boto3
from db_connection import connect_db
from utils import obtain_meaning_prefix
import os


def lambda_handler(event, context):
    word = event['queryStringParameters']['word']
    # word = event['word']
    db_connection = connect_db()
    value = obtain_meaning_prefix(word, db_connection)
    # print(value)
    return {
        'statusCode': 200,
        'body': json.dumps(value, ensure_ascii=False)
    }


# response = lambda_handler(event={'word': 'గాణ'}, context=None)
# print(response)