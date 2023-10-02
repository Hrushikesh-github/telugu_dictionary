# Function to remove common suffixes like 'ము', 'లు', 'తో', etc.
def remove_common_suffix(word, suffixes):
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

# Function to remove specific suffix 'దు'
def remove_specific_suffix(word, specific_suffix):
    if word.endswith(specific_suffix):
        return word[:-len(specific_suffix)]
    return word

# Function to add a custom suffix like 'ము'
def add_custom_suffix(word, custom_suffix='ము'):
    remove_specific_suffix(word, specific_suffix='ం')
    return word + custom_suffix

def list_cases(word):
    if word[-1]  in ['!', '.', '?', '`', "'", '"']:
        word = word[:-1]
    #print("INSIDE LIST_CASES")
    # చట్టానికి
    if word[-5:] == 'ానికి':
        #print('CASE 1')
        new_word = word[:-5] + 'ము'
        return new_word, word

    # అవినీతిపై
    elif word[-2:] == 'పై':
        #print('CASE 2')
        new_word = word[:-2]
        return new_word, word

    # ఖాయమని
    # TODO CHECK MORE
    elif word[-2:] == 'ని':
        #print('CASE 3')
        new_word = word[:-2]
        new_word_3 = word[:-3]
        # OR TRY
        if new_word[-1] != 'ు':
            new_word_2 = new_word + 'ు'
            return word, new_word, new_word_2, new_word_3
        else:
            return word, new_word, new_word_3

    # Suryudu mitrudu -> surya mitra
    elif word[-3:] == 'ుడు' or word[-3:] =='ూడు':
        #print('CASE 4')
        new_word = word[:-3]
        return new_word, word
        # OR TRY word = word[:-3] + 'ా'

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
        return  new_word, new_word_2, word

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
        # #print('NO CASE')
        return word

if __name__ == "__main__":
    # Example usage:
    input_sentence = "చట్టానికి Suryudu"
    tokens = input_sentence.split()
    processed_tokens = [remove_common_suffix(token) for token in tokens]
    processed_tokens[1] = remove_specific_suffix(processed_tokens[1], 'దు')
    processed_sentence = ' '.join(processed_tokens)
    #PRINT(processed_sentence)
    # Now, you can look up the meanings of the processed words in your Telugu dictionary.
