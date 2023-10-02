import json, os

def upload_json_files(directory):
    count, uncount = 0, 0
    for root, _, files in os.walk(directory):
        for filename in files:
            print(f"STARTED WITH THIS FILE {filename} present in {root}")
            if filename.endswith('.json'):
                json_file_path = os.path.join(root, filename)
                with open(json_file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    for word, meanings in data.items():
                        if meanings:  # Check if meanings list is not empty
                            count += 1
                        else:
                            uncount += 1
                print(f"COMPLETED UPLOADING FOR {filename}")
    print(f"TOTAL COUNT IS {count} and UNCOUNT IS {uncount}")

json_directory = '/Users/hrushikeshkyathari/sri/andhrabharthi/complete_data'

# Call the function to upload JSON files
upload_json_files(json_directory)
