import requests

def call_telugu_words_api(word):
    # Define the API URL with the word as a query parameter
    api_url = f"link-to-my-api/?word={word}"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            print(f"API request failed with status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error making API request: {str(e)}")
        return None

# Example usage:
word = "పరమేశ్వరుడు"
word = "నిర్మముడు"
result = call_telugu_words_api(word)
if result:
    print("API response:")
    print(result)
