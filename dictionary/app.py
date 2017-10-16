import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))
debug = True

def translate(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    else:
        word = word.lower()
        ls_matches = get_close_matches(word,data.keys(),n=1,cutoff=0.6)
        if not ls_matches:
            return "The word doesn't exits. Please double check it"
        else:
            response = input('Did you mean: %s ? Yes[Y] or No[N]' % ls_matches[0])
            if response == 'Y':
                return data[ls_matches[0]]
            else:
                return "Bye"

word = input("Enter word: ")

print(translate(word))
