import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)


class TeluguWordMeaningScraper:
    def __init__(self):
        self.base_url = "https://te.wiktionary.org"
        self.driver = None
        self.batch_size = 1000  # Set the batch size

    def start(self):
        self.driver = webdriver.Chrome()

    def stop(self):
        if self.driver:
            self.driver.quit()

    def extract_data_for_word(self, word_url):
        # Your existing code for extracting data
        self.driver.get(word_url)
        # time.sleep(2)
        # Extract data from the div with class "mw-parser-output"
        linked_soup = BeautifulSoup(self.driver.page_source, "html.parser")
        mw_parser_output = linked_soup.find("div", class_="mw-parser-output")

        data_dict = {}

        # Process and structure the data as needed
        if mw_parser_output:
            # Find all h2 elements within mw-parser-output
            h2_elements = mw_parser_output.find_all("h2")

            # Iterate through the h2 elements
            for h2 in h2_elements:
                h2_text = h2.get_text(strip=True)  # Get the text content of the h2
                next_element = h2.find_next_sibling()  # Get the next element after h2

                # Initialize a list to store the content associated with the h2
                content_list = []

                # Continue to add content until the next h2 is encountered
                while next_element and next_element.name != "h2":
                    content_list.append(str(next_element))
                    next_element = next_element.find_next_sibling()

                # Add the content list to the data dictionary with h2 as the key
                data_dict[h2_text] = content_list

        return data_dict

    def process_words(self, word_list, output_directory):
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        total_words = len(word_list)
        num_batches = (total_words + self.batch_size - 1) // self.batch_size  # Calculate the number of batches

        for batch_number in range(num_batches):
            start_index = batch_number * self.batch_size
            end_index = min((batch_number + 1) * self.batch_size, total_words)
            batch_words = word_list[start_index:end_index]

            word_data_dict = {}
            # Extract and process data for each word in the batch
            for i, word_text in enumerate(batch_words):
                try:
                    word_url = f"{self.base_url}/wiki/{word_text}"
                    logger.info(f"Batch {batch_number + 1}/{num_batches}, Processing Word {i + 1}/{len(batch_words)}: {word_text}")
                    # log.info(f"Batch {batch_number + 1}/{num_batches}, Processing Word {i + 1}/{len(batch_words)}: {word_text}")
                    word_data = self.extract_data_for_word(word_url)
                    cleaned_text = self.get_text_only(word_data)
                    word_data_dict[word_text] = cleaned_text
                except:
                    logger.warning(f"SOMETHING WRONG WITH THIS WORD {word_text}")
                    # print(f"SOMETHING WRONG WITH THIS WORD {word_text}")
            # Save the word_data_dict as a JSON file
            output_filename = os.path.join(output_directory, f'word_data_batch_{batch_number + 1}.json')
            with open(output_filename, 'w', encoding='utf-8') as json_file:
                json.dump(word_data_dict, json_file, ensure_ascii=False, indent=4)

    def get_text_only(self, data_dict):
        # Your existing code for extracting text from data_dict
        html_elements_list = data_dict['అర్థ వివరణ[<small>మార్చు</small>]']

        # Initialize a list to store cleaned text from each element
        cleaned_text_list = []

        # Iterate through the list of HTML elements
        for html_element in html_elements_list:
            # Create a BeautifulSoup object for each element
            soup = BeautifulSoup(html_element, 'html.parser')
            
            # Extract the text content without hyperlinks or HTML tags for each element
            text_content = soup.get_text()
            
            # Append the cleaned text to the list
            cleaned_text_list.append(text_content)
        return cleaned_text_list
