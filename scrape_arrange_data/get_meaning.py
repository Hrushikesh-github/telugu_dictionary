'''
1. Collect list of words.
2. Send it to selenium and bs4 get the meaning.
3. Save the output to DB.
'''

import json
from selenium_adapter import TeluguDictionaryScraper

scraper = TeluguDictionaryScraper()
scraper.start()
word_list = ['అంగనా','కపటము', 'కిరణము', 'సం.సంస్కృత సమ']
word_list = ['అంగనా', 'సం.సంస్కృత సమ']
# word_list = ['కపటము']
# word_list = ['సం.సంస్కృత సమ']
results = {}

for word in word_list:
    div_elements = scraper.search_word(word)
    # scraper.extract_text(div_elements)
    try:
        output = scraper.extract_text_ignore_some_dict(div_elements)
        if output and output != {} and output != '{}':
            print("OUTPUT VALUE IS: ", output, type(output))
            print('YES HERE: ', results.keys())
            results[word] = output
    except:
        print(f"SOMETHING WRONG WITH THIS WORD {word}")
    

print(results)
with open('test1_ignored_dictionary_results.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

# print(output)
scraper.stop()
