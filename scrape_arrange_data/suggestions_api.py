import requests

def call_dictionary_api(word):
    # Define the API URL
    url = "https://andhrabharati.com/dictionary/getWM.php"

    # Define the payload data
    payload = {
        'w': word,
        'token': '',  # Replace with the appropriate token if required
        'opt': 'W|E|N|N|2|6|7|8|35|50|10|13|14|29|52|1|11|4|12|51|48|49|43|55|54|56|34|36|37|9|44|58|17|18|19|20|21|22|23|24|25|33|15|41|31|32|3|39|38|40|42|45|46|47',
    }

    # Make the POST request
    response = requests.post(url, data=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the API response content
        print("THEH RSPNOE IS: ", response.text)
    else:
        print("Failed to fetch data. Status code:", response.status_code)

# Replace 'నిఘంటు' with the word you want to look up
word_to_lookup = 'నిఘంటు'
call_dictionary_api(word_to_lookup)
