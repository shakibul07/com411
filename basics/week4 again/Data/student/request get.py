# method get

import requests

response = requests.get("https://somesite.com/data.json")
print(response.json())

# ------------------------------------------------------------------------------------------------------
# method post
# --------------------------------------------------------------------------------------------------
import json
import requests

data = {
    "name" : " prins",
    "job": "lecturer"
}

json_data = json.dumps(data)
requests.post("https://somesite.com/post",json=json_data)