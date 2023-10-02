from telugu_word_meaning_scraper import TeluguWordMeaningScraper
import logging
import sys


# Set up logging to both terminal and a log file
log_filename = "scraping_log.txt"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filename)
    ]
)
# Create a logger for this module
logger = logging.getLogger(__name__)

# Create an instance of the scraper
meaning_scraper = TeluguWordMeaningScraper()

# Start the WebDriver
meaning_scraper.start()

try:
    # Load the list of words from your CSV file (assuming you have it)
    with open("/Users/hrushikeshkyathari/sri/andhrabharthi/complete_words_without_gap.csv", "r", encoding="utf-8") as csvfile:
        words = [line.strip() for line in csvfile]

    # Set the output directory where batch JSON files will be saved
    output_directory = "word_data_batches"

    # Process and save words in batches
    meaning_scraper.process_words(words[32835:], output_directory)

finally:
    # Stop the WebDriver
    meaning_scraper.stop()
