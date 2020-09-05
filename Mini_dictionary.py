import json
from difflib import get_close_matches
data= json.load(open("data.json"))
def find_meaning(word):
    word=word.lower();
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice=input("Did you  mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if choice=="Y" or choice=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif choice=="N" or choice=="n":
            return "Wrong word entered. Please try again"
        else:
            return "Unable to process your request. Try Again!!"
    else:
        return "Wrong word entered. Please try again"

query = input("Enter word: ")
output = find_meaning(query)
if type(output) == list:
    for item in output:
        print(item)
else:
    print("Meaning:- "+ output)

