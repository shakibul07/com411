# we often need to access and send files from and to remote (web) locations.  We can use the module requests to allow us to send or received files from a remote file server.
#
# We can get data (e.g. a JSON file) from a server using the method get

import requests

response = requests.get("https://somesite.com/data.json")
print(response.json())

#
# We can send data (e.g. JSON) to a server using the method post:

import json
import requests

data = {
    "name": "Prins",
    "job": "Lecturer"
}

json_data = json.dumps(data)
requests.post("https://somesite.com/post", json=json_data)