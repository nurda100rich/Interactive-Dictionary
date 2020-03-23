import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirmation = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(word, data.keys())[0])
        if confirmation == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
            return data[w.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif confirmation == "N":
            return "The word doesn't exist. Please double check it."
        else:
            "I didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
word2 = word.lower()

output = translate(word2)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
