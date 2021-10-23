import json

json_data = {
    "name": "prins",
    "job":"lecturer"
}

json_file = open("output.json","w")
json.dump(json_data,json_file,indent=4)

json_file.close()