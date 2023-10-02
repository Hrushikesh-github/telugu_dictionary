import boto3
import json
import os

# Define your AWS region and DynamoDB table name
aws_region = 'us-east-1'
table_name = 'meanings-table'

dynamodb = boto3.resource('dynamodb',
                                aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
                                aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
                                region_name=aws_region)

# Define the DynamoDB table
table = dynamodb.Table(table_name)

# Function to read and upload JSON files
def upload_json_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            print(f"STARTED WITH THIS FILE {filename} present in {root}")
            if filename.endswith('.json'):
                json_file_path = os.path.join(root, filename)
                with open(json_file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    for word, meanings in data.items():
                        if meanings:  # Check if meanings list is not empty
                            upload_word_meanings_sort_key(word, meanings)
                print(f"COMPLETED UPLOADING FOR {filename}")

# Function to upload word meanings to DynamoDB
def upload_word_meanings(word, meanings):
    response = table.put_item(
        Item={
            'letter': word,
            'meanings': [replace_newline_chars(meaning) for meaning in meanings]
        }
    )
    # print(f"Uploaded word: {word}")

# Function to upload word meanings to DynamoDB
def upload_word_meanings_sort_key(word, meanings):
    response = table.put_item(
        Item={
            'letter': word[0],
            'word': word,  # Set the sort key value to be the same as the word
            'meanings': [replace_newline_chars(meaning) for meaning in meanings]
        }
    )

# Function to replace '\n' with newline character
def replace_newline_chars(text):
    return text.replace('\n', '')

# Specify the directory containing your JSON files
json_directory = '/Users/hrushikeshkyathari/sri/andhrabharthi/complete_data'

# Call the function to upload JSON files
upload_json_files(json_directory)
