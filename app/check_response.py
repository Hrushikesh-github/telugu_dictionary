import requests

# Define the base URL of your FastAPI server
base_url = 'http://127.0.0.1:8000'

# Define the sentence you want to pass as a parameter
sentence = 'గాణ స్వాజన్యము abc'
sentence = 'ఈ ధర్మము పరమేశ్వరుడు నిర్మించాడు. పరమేశ్వరుడే లేడనే వాడు పరమేశ్వరుడు నిర్మించాడంటే ఒప్పుకోడు . భగవంతుడుంటే చూపించాలంటాడు. ఇంతకంటే తెలివి తక్కువ మాట ఉండదు'

# Construct the full URL with the sentence parameter
url = f'{base_url}/sentence_all_words/?sentence={sentence}'
url = f'{base_url}/sentence/?sentence={sentence}'
url = f'{base_url}/sentence_check/?sentence={sentence}'

# Make a GET request to the endpoint
response = requests.get(url)

# Check the response status code and content
if response.status_code == 200:
    print('Success! Response content:')
    print(response.text)
else:
    print(f'Error: {response.status_code}')
