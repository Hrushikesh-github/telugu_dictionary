from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from typing import List, Dict
from db_connection import connect_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# CORS Configuration
origins = ["http://localhost", "http://localhost:8000"]  # Add other allowed origins as needed
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],  # You can specify the HTTP headers you want to allow
)



db_connection = connect_db()

# @app.get("home/")
# async def read_root_home(request: Request):
#     meanings = db_connection.query_meanings_for_word('స్వాజన్యము')
#     return f'HI IS THIS WORKING?? -> {meanings}'
#     return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/get_meanings_home/{word}")
# async def fetch_meanings_home(request: Request, word: str):
#     meanings = db_connection.query_meanings_for_word(word)
#     # meanings = get_meanings(word)
#     return meanings
#     return f'THE  MEANING of the word {word} IS {meanings}'
#     # return templates.TemplateResponse("index.html", {"request": request, "word_meanings": meanings})

# Simulate a function to query meanings from the database
def query_meanings_for_word(word):
    meanings = db_connection.query_meanings_for_word(word)
    # meanings = get_meanings(word)
    return meanings

def get_word_meanings(sentence):
    # Split the sentence into words on the server side
    words = sentence.split()

    # Query meanings for each word
    word_meanings = {}
    for word in words:
        meanings = query_meanings_for_word(word)
        word_meanings[word] = meanings

    return word_meanings

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_sentence_meanings", response_class=HTMLResponse)
async def fetch_sentence_meanings(request: Request):
    sentence = request.form["sentence"]
    word_meanings = get_word_meanings(sentence)
    return templates.TemplateResponse("display_sentence_meanings.html", {"request": request, "sentence": sentence, "word_meanings": word_meanings})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
