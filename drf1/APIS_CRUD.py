import requests
import json
url = 'http://127.0.0.1:8000/api4/'
headers = {'Content-Type': 'application/json'}

def get_data(url=url, id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    r = requests.get(url, data=json.dumps(data), headers=headers)
    res = r.json()
    print(res)

# data = {
#     'id': 2
#     }

data = {
    'roll':123,
    'name': 'Manisha'
}

json_data  = json.dumps(data)

def post_data(json_data=json_data):
    r = requests.post(url, data=json_data, headers=headers)
    res = r.json()
    print(res)

def update_data(url=url, json_data=json_data):
    r = requests.put(url=url, data=json_data)
    res = r.json()
    print(res)

def delete_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    print(data)
    r = requests.delete(url=url, data=json.dumps(data), headers=headers)
    res = r.json()
    print(res)

#post_data()
delete_data(id=1)