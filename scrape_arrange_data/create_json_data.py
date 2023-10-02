import pandas as pd
import json
from selenium_adapter import TeluguDictionaryScraper

# Load the list of words from a CSV file
csv_file = 'individual_csv/part_1.csv'
output_csv_file = 'output_csv/part_1.csv'
df = pd.read_csv(csv_file)

# Initialize the scraper
scraper = TeluguDictionaryScraper()
scraper.start()

# Define the batch size and count variables
batch_size = 10000000
json_count = 1
results = {}

# Iterate through each row in the CSV file
for index, row in df.iterrows():
    word = row['word']
    if (index+1) % 10 == 0:
        scraper.refresh()
    
    div_elements = scraper.search_word(word)
    
    try:
        output = scraper.extract_text_to_json(div_elements)
        
        if output and output != {} and output != '{}':
            # Update the "file_path" column with the file name
            df.at[index, 'file_path'] = f'saved_files/json_files/part1/file_{json_count}.json'
            
            # Update the "saved" column to 1
            df.at[index, 'saved'] = 1
            
            results[word] = output
            
            # Check if the batch size limit is reached
            if len(results) >= batch_size:
                file_name = f'saved_files/json_files/part1/file_{json_count}.json'
                print(f"SAVING OUR BATCH RESULTS at {file_name}")
                with open(file_name, 'w', encoding='utf-8') as json_file:
                    json.dump(results, json_file, ensure_ascii=False, indent=4)
                results = {}
                json_count += 1
        else:            
            # Update the "saved" column to 2
            df.at[index, 'saved'] = 2

    
    except Exception as e:
        print(f"ERROR WITH {word} -> {e}")
        df.at[index, 'saved'] = -1

# Save any remaining results after processing
if results:
    file_name = f'saved_files/json_files/part1/file_{json_count}.json'
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

# Save the updated DataFrame to the CSV file
df.to_csv(output_csv_file, index=False)

# Stop the scraper
scraper.stop()
