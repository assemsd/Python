import json
from difflib import get_close_matches

data = json.load(open("/home/assem/Desktop/python_projects/udemy_projects/data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif word.title() in data:
    return data[word.title()]
  elif word.upper() in data:
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys())) > 0:
    print("Did you mean %s instead?" %get_close_matches(word, data.keys())[0])
    decide = input("Press y for yes or n for no: ")
    if decide == "y":
      return data[get_close_matches(word, data.keys())[0]]
    elif decide == "n":
      return("Sorry, this word does not exist.")
    else:
      return("You have entered wrong input. Please enter just y or n") 
  
  else:
    print("You have entered wrong word! Please, check it again.")

word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)    
