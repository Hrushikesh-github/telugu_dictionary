from app.utils import list_cases

def get_meaning(word: str, db_connection):
    '''
    word: str
    output: List if meaning found or None Type
    '''
    meaning = db_connection.query_meanings_for_word(word)
    return meaning

def get_prefix(word: str, db_connection):
    '''Returns a list of words with common prefix in DB'''
    words_with_prefix = db_connection.find_words_with_prefix(word)
    return words_with_prefix

def get_multiple_meanings(word: str, db_connection):
    new_word_list = list_cases(word)
    # print(new_word_list, type(new_word_list))
    # return
    new_word_dict = {}
    for new_word in new_word_list:
        if new_word:
            new_word_meaning = get_meaning(new_word, db_connection)
            if new_word_meaning:
                new_word_dict[new_word] = new_word_meaning
            else:
                new_word_dict[new_word] = None

    return new_word_dict

def filter_multiple_meanings(word: str, db_connection):
    new_word_dict = get_multiple_meanings(word, db_connection)
    filtered_data = {key: value for key, value in new_word_dict.items() if value is not None}
    return filtered_data

def get_meaning_sentence(sentence: str, db_connection):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning = get_meaning(word, db_connection)
        word_dict[word] = meaning
    return word_dict

def get_multiple_meaning_sentence(sentence: str, db_connection):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning_dict = filter_multiple_meanings(word, db_connection)
        for modified_word, meaning in meaning_dict.items():
            word_dict[word] = []
            word_dict[word].append(meaning)
    return word_dict

def get_multiple_meaning_sentence(sentence: str, db_connection):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning_dict = filter_multiple_meanings(word, db_connection)
        if len(meaning_dict) != 0:
            for modified_word, meaning in meaning_dict.items():
                word_dict[word] = []
                word_dict[word].append(meaning)
        else:
            word_dict[word] = get_prefix(word)
    return word_dict

def get_meaning_sentence(sentence: str, db_connection):
    words = sentence.split()
    word_dict = {}
    for word in words:
        meaning = get_meaning(word, db_connection)
        if meaning:
            word_dict[word] = meaning
    return word_dict

def obtain_meaning_prefix(word: str, db_connection):
    word_dict = {}
    meaning_dict = filter_multiple_meanings(word, db_connection)
    if len(meaning_dict) != 0:
        for modified_word, meaning in meaning_dict.items():
            word_dict[word] = []
            word_dict[word].append(meaning)
        return word_dict
    else:
        prefix_list = get_prefix(word)
        return {'similar words' :prefix_list}
    

def list_cases(word):
    if len(word) < 3:
        return word
    
    if word[-1]  in ['!', '.', '?', '`', "'", '"']:
        #print("CASE 0")
        word = word[:-1]
    # చట్టానికి
    if word[-5:] == 'ానికి':
        #print("CASE 1")
        new_word = word[:-5] + 'ము'
        return new_word, word

    # అవినీతిపై
    elif word[-2:] == 'పై':
        #print("CASE 2")
        new_word = word[:-2]
        return new_word, word

    # ఖాయమని
    # TODO CHECK MORE
    elif word[-2:] == 'ని':
        #print("CASE 3")
        new_word = word[:-2]
        new_word_3 = word[:-3]
        if new_word[-1] != 'ు':
            new_word_2 = new_word + 'ు'
            return word, new_word, new_word_2, new_word_3
        else:
            return word, new_word, new_word_3

    # Suryudu mitrudu -> surya mitra
    elif word[-3:] == 'ుడు' or word[-3:] =='ూడు':
        #print("CASE 4")
        new_word = word[:-3]
        return new_word, word

    # chetthamtho
    elif word[-2:] == 'తో':
        #print('CASE 5')
        new_word = word[:-2]
        # TODO CHECK MORE
        new_word = word + 'ము'
        return new_word, word

    # Asurulu Devathalu, ఆరోపణలు, సాక్ష్యాలు
    elif word[-2:] in ['లు', 'ను', 'కు']:
        #print('CASE 6')
        # Try the original Otherwise
        new_word = word[:-3] 
        new_word_2 = word[:-2]
        new_word_3 = word[:-2] + 'ము'
        new_word_4 = word[:-3] + 'ము'
        return  new_word, new_word_2, word, new_word_3, new_word_4

    
    # Soundaryam
    elif word[-1] == 'ం':
        #print('CASE 7')
        new_word = word[:-1] + 'ము'
        return new_word, word

    # అధికారుల
    elif word[-1] == 'ల':
        #print('CASE 8')
        new_word = word[:-2] + 'ి'
        return word, new_word
    # ధర్నాలే
    elif word[-2:] == 'లే':
        #print('CASE 9')
        # TODO
        new_word = word[:-2] + 'లు'
        return new_word, word
    # రాష్ట్రవ్యాప్తంగా
    elif word[-2:] == 'గా':
        #print('CASE 10')
        new_word = word[:-2]
        return new_word, word
        
    else:
        #print('NO CASE')
        return [word]

def process_prefix(word):
    if len(word) >= 7 and len(word) < 10:
        #print("THE WORD IS Between 6-10")

        new_word = word[:3]
    elif len(word) >= 10:
        #print("The word is > 10")
        new_word = word[:5]
    else:
        #print("The word is less than 6")
        new_word = word[:3]
    return new_word

if __name__ == "__main__":
    from db_connection import connect_db
    db_connection = connect_db()
    meaning = get_meaning(word='గాణ', db_connection=db_connection)
    print(f"THE MEANING IS {meaning}")
    print("DONE")
