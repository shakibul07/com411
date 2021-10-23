import json

with open("songs.json")as json_file:
    data = json.load(json_file)

print(data)