# DevOps Engineer - Developer has an API (Application Programmable Interface)

import requests # type: ignore

def get_api_data():
    url_demo = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=url_demo)
    if response == 200:
        return response.json()
    else:
        return

print(get_api_data()[0])