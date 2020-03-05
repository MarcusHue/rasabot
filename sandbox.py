import requests as re 
import json

joke = re.get('https://api.chucknorris.io/jokes/random').json()['value']


print(joke)