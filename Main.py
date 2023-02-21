import json

# Opens json file and sets data to variable
with open('words.json') as f:
   data = json.load(f)

print(data)

