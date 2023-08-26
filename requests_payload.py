import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post", json=payload)

print(r.text)