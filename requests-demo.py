import requests

req = requests.get("https://xkcd.com/353/")

image_req = requests.get("https://imgs.xkcd.com/comics/python.png")

user_info = {"username": "hello", "password": "testing"}

post = requests.post("https://httpbin.org/post", data=user_info)

r_dict = post.json()

print(r_dict["form"])
