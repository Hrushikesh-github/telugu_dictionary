import boto3
from boto3.dynamodb.conditions import Key  
import os

# Define your AWS region and DynamoDB table name
aws_region = 'us-east-1'
table_name = 'telugu-word-meanings'

# # Initialize the DynamoDB resource
# dynamodb = boto3.resource('dynamodb',
#                           aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
#                           aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
#                           region_name=aws_region)

# # Define the DynamoDB table
# table = dynamodb.Table(table_name)

# Function to query meanings for a word
def query_meanings_for_word(word):
    response = table.get_item(
        Key={
            'word': word
        }
    )
    item = response.get('Item')
    if item:
        meanings = item.get('meanings', [])
        if meanings:
            return meanings
    return None

class connect_db():
    def __init__(self) -> None:
        # Define your AWS region and DynamoDB table name
        aws_region = 'us-east-1'
        table_name = 'telugu-word-meanings'

        # Initialize the DynamoDB resource
        dynamodb = boto3.resource('dynamodb',
                                aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
                                aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
                                region_name=aws_region)

        # Define the DynamoDB table
        self.table = dynamodb.Table(table_name)

    def query_meanings_for_word(self, word):
        response = self.table.get_item(
            Key={
                'word': word
            }
        )
        item = response.get('Item')
        if item:
            meanings = item.get('meanings', [])
            if meanings:
                return meanings
        return None
 


if __name__ == '__main__':
    # word_to_query = input('Enter a word to query for meanings: ')
    word_to_query = 'స్వాజన్యము'
    db_connection = connect_db()
    meanings = db_connection.query_meanings_for_word(word_to_query)
    
    if meanings:
        print(f"Meanings for '{word_to_query}':")
        for idx, meaning in enumerate(meanings, start=1):
            print(f"{idx}. {meaning}")
    else:
        print(f"No meanings found for '{word_to_query}'.")
