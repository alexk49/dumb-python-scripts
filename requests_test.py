import requests

url = "https://httpbin.org"

payload = {"firstName" : "John", "lastName" : "Smith"}

response = requests.get(url, params = payload)

print(response.url)
print(response.status_code)
# print(response.content)
# print(response.text)

response = requests.post(url + "/post", data=payload)

print(response.url)
print(response.status_code)
# print(response.content)

files = {"file" : open('file_to_upload.txt', 'rb')}

response = requests.post(url + "/post", files=files)

print(response.status_code)
# print(response.text)