from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

class TeluguWordScraper:
    def __init__(self):
        self.driver = None

    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://te.wiktionary.org/w/index.php?title=వర్గం:తెలుగు_పదాలు&from=అ")

    def stop(self):
        if self.driver:
            self.driver.quit()

    def extract_words(self, url, max_iterations=5):
        word_list = []
        current_url = url

        for _ in range(max_iterations):
            self.driver.get(current_url)
            time.sleep(4)

            word_div = self.driver.find_element(By.ID, "mw-pages")
            soup = BeautifulSoup(word_div.get_attribute("outerHTML"), "html.parser")

            for ul in soup.find_all("ul"):
                for li in ul.find_all("li"):
                    word = li.get_text()
                    word_list.append(word)

            next_page_link = soup.find("a", title="వర్గం:తెలుగు పదాలు", text="తరువాతి పేజీ")

            if not next_page_link:
                break

            next_page_url = next_page_link.get("href")
            full_next_page_url = f"https://te.wiktionary.org{next_page_url}"
            current_url = full_next_page_url
            if _ % 20 == 0 and _ != 0:
                print('THE NEXT URL is: ', current_url)
        return word_list, current_url

    def save_words_to_csv(self, words, filename="telugu_words.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["word"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for word in words:
                writer.writerow({"word": word})

# Example usage:
scraper = TeluguWordScraper()
scraper.start()
url = "https://te.wiktionary.org/w/index.php?title=వర్గం:తెలుగు_పదాలు&from=అ"
words, next_url = scraper.extract_words(url, max_iterations=2000)
scraper.save_words_to_csv(words, filename="2000_telugu_words.csv")
scraper.stop()

print(len(words))