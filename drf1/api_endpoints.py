import requests

url = 'http://127.0.0.1:8000/'
endpoint = 'api1/all'

response = requests.get(url + endpoint)

if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except ValueError as e:
        print("Error decoding JSON:", e)
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.content)
