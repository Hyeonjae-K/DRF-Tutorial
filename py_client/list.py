import requests
from getpass import getpass

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
# password = getpass()

auth_response = requests.post(
    auth_endpoint,
    json={'username': 'admin', 'password': '1234'},)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }

    endpoint = 'http://127.0.0.1:8000/api/products/'

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())

    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print(results)
    # if next_url:
    #     get_response = requests.get(next_url, headers=headers)
