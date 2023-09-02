import haslib
from pprint import pprint

import requests
from bs4 import BeautifulSoup

def get_md(s):
    return hashlib.md5(bytes(s, encoding='utf8')).hexdigest()

def main():
    url = 'https://sevashoes.com/en/login'

    with requests.session() as session:
        response = session.post(url, auth=(username, password))

        md5_pass = get_md5(password) + ":"
        email = username + ":"

        soup = BeautifulSoup(response.text, 'lxml')
        challenge = soup.find('input', id='challenge').get('value')

        result = email + md5_pass + challenge
        response = get_md5(result)

        data = {'username' : username,
                'password' : '',
                'challenge' : '',
                'response' : response
            }

        r_post = session.post(url, data=data)
        pprint(r_post.text)

        with open('index.html', 'w') as file:
            file.write(r_post.text)

    
if __name == '__main__':
    main()