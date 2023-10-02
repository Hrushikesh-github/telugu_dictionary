import boto3
from boto3.dynamodb.conditions import Key
import os
from utils import process_prefix

class connect_db():
    def __init__(self) -> None:
        # Define your AWS region and DynamoDB table name
        aws_region = 'us-east-1'
        # table_name = 'telugu-word-meanings'
        table_name = 'meanings-table'

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
                'letter': word[0],
                'word': word  # Include the sort key value
            }
        )
        item = response.get('Item')
        if item:
            meanings = item.get('meanings', [])
            if meanings:
                return meanings
        return None

    def find_words_with_prefix(self, word):
        words_with_prefix = []
        new_word = process_prefix(word)
        # print(f"OLD WORD IS {word} and NEW WORD IS {new_word}")
        # Assuming word is 'కంటక' in this example
        partition_key = new_word[0]  # Get the first character as the partition key
        sort_key_prefix = new_word  # Use the full word as the sort key prefix

        response = self.table.query(
            KeyConditionExpression=Key('letter').eq(partition_key) & Key('word').begins_with(sort_key_prefix)
        )

        items = response['Items']
        words = [item['word'] for item in items]
        words_with_prefix.extend(words)

        return words_with_prefix

if __name__ == "__main__":
    db_connection = connect_db()
    # meanings = db_connection.query_meanings_for_word('ఔరా')
    # print(meanings)
    word = 'కంటకద'
    words_with_prefix = db_connection.find_words_with_prefix(word)
    print('***' * 10)
    print(words_with_prefix)