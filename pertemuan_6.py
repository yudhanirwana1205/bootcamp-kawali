import requests
from pprint import pprint


r = requests.get('https://jsonplaceholder.typicode.com/posts/101')
data = r.json()
pprint(data)

post = {
    'body': "Lorem ipsum",
    'title': "Title",
    'userId': 5,
}

# Post data and Return data
req = requests.post('https://jsonplaceholder.typicode.com/posts', json=post)
print(req.json())
print('Status Code: ', req.status_code)
print(req.text)
print(req)

update_post = post
update_post['id'] = 5

req = requests.put(
    'https://jsonplaceholder.typicode.com/posts/5', json=update_post)
print(req.json())

"""

Client -> API -> Backend(Server)

web Method:

Get -> Ambil Data
Post -> Buat Data di Server
Patch/Put -> Update data di server
Delete -> Hapus data di server

"""


def square(x): return x ** 2


print(square(2))
