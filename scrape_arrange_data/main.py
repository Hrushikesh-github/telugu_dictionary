import json
from selenium_adapter import TeluguDictionaryScraper

scraper = TeluguDictionaryScraper()
scraper.start()
word_list = ['అంగనా','కపటము', 'కిరణము', 'సం.సంస్కృత సమ']
results = {}
json_count = 0

for i, word in enumerate(word_list):
    if (i+1) % 10 == 0:
        scraper.refresh()
    div_elements = scraper.search_word(word)
    try:
        output = scraper.extract_text_ignore_some_dict(div_elements)
        if output and output != {} and output != '{}':
            results[word] = output
            if (i + 1) % 250 == 0:
                file_name = f'saved_files/file_{json_count}.json'
                with open(file_name, 'w', encoding='utf-8') as json_file:
                    json.dump(results, json_file, ensure_ascii=False, indent=4)
                results = {}
                json_count += 1
    except:
        print(f"SOMETHING WRONG WITH THIS WORD {word}")
    

print(results)
with open('test1_ignored_dictionary_results.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

# print(output)
scraper.stop()
