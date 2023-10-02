from fastapi import FastAPI
from app.db_connection import connect_db
from app.utils import list_cases
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db_connection = connect_db()

origins = ["http://localhost", "http://localhost:8000"]  # Add other allowed origins as needed
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],  # You can specify the HTTP headers you want to allow
)

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.get("/words/{word}")
def get_meaning(word: str):
    '''
    word: str
    output: List if meaning found or None Type
    '''
    meaning = db_connection.query_meanings_for_word(word)
    return meaning


@app.get("/prefix/{word}")
def get_prefix(word: str):
    '''Returns a list of words with common prefix in DB'''
    words_with_prefix = db_connection.find_words_with_prefix(word)
    return words_with_prefix

@app.get("/multiple_words/{word}")
def get_multiple_meanings(word: str):
    new_word_list = list_cases(word)
    print(new_word_list, type(new_word_list))
    # return
    new_word_dict = {}
    for new_word in new_word_list:
        if new_word:
            new_word_meaning = get_meaning(new_word)
            if new_word_meaning:
                new_word_dict[new_word] = new_word_meaning
            else:
                new_word_dict[new_word] = None

    return new_word_dict

@app.get("/filter_multiple_words/{word}")
def filter_multiple_meanings(word: str):
    new_word_dict = get_multiple_meanings(word)
    filtered_data = {key: value for key, value in new_word_dict.items() if value is not None}
    return filtered_data

@app.get("/sentence_all_words/")
def get_meaning_sentence(sentence: str):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning = get_meaning(word)
        word_dict[word] = meaning
    return word_dict

@app.get("/sentence_check/")
def get_multiple_meaning_sentence(sentence: str):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning_dict = filter_multiple_meanings(word)
        for modified_word, meaning in meaning_dict.items():
            word_dict[word] = []
            word_dict[word].append(meaning)
    return word_dict

@app.get("/prefix_sentence_check/")
def get_multiple_meaning_sentence(sentence: str):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning_dict = filter_multiple_meanings(word)
        if len(meaning_dict) != 0:
            for modified_word, meaning in meaning_dict.items():
                word_dict[word] = []
                word_dict[word].append(meaning)
        else:
            word_dict[word] = get_prefix(word)
    return word_dict

@app.get("/simplesentence/")
def get_meaning_sentence(sentence: str):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning = get_meaning(word)
        if meaning:
            word_dict[word] = meaning
    return word_dict

@app.get("/get_word_or_prefix/{word}")
def obtain_meaning_prefix(word: str):
    word_dict = {}
    meaning_dict = filter_multiple_meanings(word)
    if len(meaning_dict) != 0:
        for modified_word, meaning in meaning_dict.items():
            word_dict[word] = []
            word_dict[word].append(meaning)
        return word_dict
    else:
        prefix_list = get_prefix(word)
        return {'similar words' :prefix_list}
    

    