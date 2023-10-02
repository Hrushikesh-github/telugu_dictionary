from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import json
class TeluguDictionaryScraper:
    def __init__(self):
        self.driver = None

    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://andhrabharati.com/dictionary/")

    def stop(self):
        if self.driver:
            self.driver.quit()

    def refresh(self):
        if self.driver:
            self.driver.refresh()
            
    def search_word(self, word):
        if not self.driver:
            print("Driver not initialized. Call start() first.")
            return

        text_box = self.driver.find_element(By.NAME, "strSearch")
        button_element = self.driver.find_element(By.ID, "button2")

        # Click the text box to focus on it
        text_box.click()
        text_box.clear()

        # Clear the text box by selecting all existing text and pressing delete
        text_box.send_keys(Keys.CONTROL + "a")
        text_box.send_keys(Keys.DELETE)

        text_box.send_keys(word)
        button_element.click()
        time.sleep(4)
        div_elements = self.driver.find_elements(By.CLASS_NAME, "MeaningEC")
        return div_elements

    def extract_text(self, div_elements):
        for div_element in div_elements:
            html_text = div_element.get_attribute("outerHTML")
            soup = BeautifulSoup(html_text, 'html.parser')

            dict_name_elements = soup.find_all('span', class_='dict')

            # Iterate over the dictionary name elements and print their text
            for dict_name_element in dict_name_elements:
                dict_name = dict_name_element.text
                print("Dictionary Name:", dict_name)

            # Find all <dd> elements (dictionary meanings)
            meaning_elements = soup.find_all('dd')

            # Iterate over the meaning elements and print their text
            for meaning_element in meaning_elements:
                meaning = meaning_element.text.strip()
                print("Meaning:", meaning)

    def extract_text_to_json(self, div_elements):
        result = {}
        for div_element in div_elements:
            html_text = div_element.get_attribute("outerHTML")
            soup = BeautifulSoup(html_text, 'html.parser')

            dict_name_elements = soup.find_all('span', class_='dict')
            meaning_elements = soup.find_all('dd')

            # Iterate over the dictionary name elements and meaning elements
            for dict_name_element, meaning_element in zip(dict_name_elements, meaning_elements):
                dict_name = dict_name_element.text
                meaning = meaning_element.text.strip()

                # Add the dictionary name and meaning to the result dictionary
                result[dict_name] = meaning

        return json.dumps(result, ensure_ascii=False)

    def extract_text_ignore_some_dict(self, div_elements):
        result = {}
        for div_element in div_elements:
            html_text = div_element.get_attribute("outerHTML")
            soup = BeautifulSoup(html_text, 'html.parser')

            dict_name_elements = soup.find_all('span', class_='dict')
            meaning_elements = soup.find_all('dd')

            # Iterate over the dictionary name elements and meaning elements
            for dict_name_element, meaning_element in zip(dict_name_elements, meaning_elements):
                dict_name = dict_name_element.text
                meaning = meaning_element.text.strip()

                # Check if the dictionary name contains the phrase "పర్యాయపద నిఘంటువు" and skip it
                if "పర్యాయపద నిఘంటువు" not in dict_name:
                    # Add the dictionary name and meaning to the result dictionary
                    result[dict_name] = meaning

        return json.dumps(result, ensure_ascii=False)

# Example usage:
# scraper = TeluguDictionaryScraper()
# scraper.start()
# div_elements = scraper.search_word("కపటము")
# scraper.extract_text(div_elements)
# scraper.stop()
