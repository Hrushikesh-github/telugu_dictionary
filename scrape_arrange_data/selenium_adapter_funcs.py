from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys





def get_driver_text_box():
    driver = webdriver.Chrome()
    driver.get("https://andhrabharati.com/dictionary/")
    text_box = driver.find_element(By.NAME, "strSearch")
    button_element = driver.find_element(By.ID, "button2")
    return driver, text_box, button_element

def obtain_result(driver, text_box, button_element, word):
    # Click the text box to focus on it
    text_box.click()
    text_box.clear()

    # Clear the text box by selecting all existing text and pressing delete
    text_box.send_keys(Keys.CONTROL + "a")
    text_box.send_keys(Keys.DELETE)

    text_box.send_keys(word)
    button_element.click()
    time.sleep(4)
    div_elements = driver.find_elements(By.CLASS_NAME, "MeaningEC")
    return div_elements

def extract_text(div_elements):
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



def quit_selenium(driver):
    driver.quit()