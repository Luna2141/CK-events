import json

file = open("words.json")

content = file.read()
words = json.loads(content)

more_words = ""

words.append(more_words)
json_obj = json.dumps(words, indent=4)

file = open("words.json", "w")
file.write(json_obj)

file.close()
