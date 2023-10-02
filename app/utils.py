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

def old_process_prefix(word):
    new_word = word[:3]
    return new_word
