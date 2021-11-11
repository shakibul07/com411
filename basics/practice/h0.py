import csv

with open("h0.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',',quotech='"')
    for row in csv_reader:
       print(row[0])

print("|||||||||||||||||||||||||||||")
print("_____________________________")

import json

with open("songs.json") as json_file:
    data = json.load(json_file)

print(data)

print("|||||||||||||||||||||||||||||")
print("_____________________________")

import json

json_data = {
    "name": "prins",
    "job" :"lecturer"
}

json_file = open("output.json","w")
json.dump(json_data,json_file,indent=4)

json_file.close()

print("|||||||||||||||||||||||||||||")
print("_____________________________")

