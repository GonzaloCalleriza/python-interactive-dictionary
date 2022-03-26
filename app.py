import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no")
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "That word is not in our dictionary. Please double check it."
    else:
        return "That word is not in our dictionary. Please double check it."

word= input("What word would you want to know?\n")

print(define(word))