import requests

headers = {
    'Authorization': 'Bearer a3de223e4ce2ea31aa1dd689413109f4af995045',
}
endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    'title': 'This field is done',
    'price': 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
