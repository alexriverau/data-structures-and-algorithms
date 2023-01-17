import string

def first_repeated_word(txt):
    words = txt.translate(str.maketrans('', '', string.punctuation)).split()
    count = {}

    for word in words:
        if word.lower() in count:
            return word.lower()
        else:
            count[word.lower()] = 1

    return None
