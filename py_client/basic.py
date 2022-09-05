import requests

endpoint = 'http://127.0.0.1:8000/api/'

get_response = requests.get(
    endpoint, json={'query': 'Hello world'})  # HTTP Request
print(get_response.text)  # print raw text response

# HTTP Reqeust -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json()['message'])
print(get_response.status_code)
