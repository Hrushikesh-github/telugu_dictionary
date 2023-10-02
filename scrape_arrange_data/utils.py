import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

class TeluguWordMeaningScraper:
    def __init__(self):
        self.base_url = "https://te.wiktionary.org"
        self.driver = None

    def start(self):
        self.driver = webdriver.Chrome()

    def stop(self):
        if self.driver:
            self.driver.quit()

    def extract_data_for_word(self, word_url):
        self.driver.get(word_url)

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

    def process_words(self, start_url):
        self.driver.get(start_url)

        # Locate the div with the ID "mw-pages" that contains the list of words
        word_div = self.driver.find_element(By.ID, "mw-pages")

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(word_div.get_attribute("outerHTML"), "html.parser")
        word_data_dict = {}
        # Extract and process data for each word
        for i, word_element in enumerate(soup.find_all("li")):
            word_a = word_element.find("a")
            if word_a:
                word_text = word_a.get_text()
                word_link = word_a.get("href")
                word_url = f"{self.base_url}{word_link}"

                print(f"Processing Word {i + 1}: {word_text}")
                word_data = self.extract_data_for_word(word_url)
                # self.get_text_only(word_data)                  
                # Extract and store the cleaned text
                cleaned_text = self.get_text_only(word_data)

                # Store the cleaned text in the word_data_dict with the word as the key
                word_data_dict[word_text] = cleaned_text

        # Save the word_data_dict as a JSON file
        with open('word_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(word_data_dict, json_file, ensure_ascii=False, indent=4)

    def get_text_only(self, data_dict):
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
        # Print the cleaned text from all elements
        # for text_content in cleaned_text_list:
        #     print('THE MEANING ISS:::: ',text_content)
        # time.sleep(10)
        


# Example usage:
scraper = TeluguWordScraper()
scraper.start()
scraper.process_words("https://te.wiktionary.org/w/index.php?title=వర్గం:తెలుగు_పదాలు&from=క", iterations=5)
# scraper.stop()
