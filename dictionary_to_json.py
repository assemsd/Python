"""
 Store the dictionary in a json file.
"""
import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

#add new value to dictionary
d["employees"].append(dict(firstName= 'Albert', lastName='Bert'))

#write the dictionary content to the file
with open("company.json", "w") as file:
  json.dump(d, file, indent=4)
