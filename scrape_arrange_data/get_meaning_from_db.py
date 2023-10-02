import boto3
from boto3.dynamodb.conditions import Key  # Import the Key object
import os

# Define your AWS region and DynamoDB table name
aws_region = 'us-east-1'
table_name = 'telugu-word-meanings'

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
                          region_name=aws_region)
# Define the DynamoDB table
table = dynamodb.Table(table_name)

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

# Custom function to check if an attribute begins with a value
def begins_with_attr(attr_name, value):
    return attr_name.startswith(value)

def query_words_with_prefix(prefix):
    response = table.scan(
        FilterExpression=begins_with_attr('word', prefix)
    )
    items = response.get('Items', [])
    return items

if __name__ == '__main__':
    # word_to_query = input('Enter a word to query for meanings: ')
    word_to_query = 'స్వాజన్యము'
    meanings = query_meanings_for_word(word_to_query)
    
    if meanings:
        print(f"Meanings for '{word_to_query}':")
        for idx, meaning in enumerate(meanings, start=1):
            print(f"{idx}. {meaning}")
    else:
        print(f"No meanings found for '{word_to_query}'.")
