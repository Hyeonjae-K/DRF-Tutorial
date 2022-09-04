import requests

endpoint = 'https://httpbin.org/anything'

get_response = requests.get(
    endpoint, json={'query': 'Hello world'})  # HTTP Request
print(get_response.text)  # print raw text response

# HTTP Reqeust -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json())
print(get_response.status_code)
