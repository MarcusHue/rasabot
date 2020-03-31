import requests as re 
import json
import api_creds as ac




search_string = "pood"
search_breed_id_url = 'https://api.thedogapi.com/v1/breeds/search?q=' + search_string
dog = re.get(search_breed_id_url, headers={"x-api-key":ac.dog_key}).json()
if len(dog) > 1:
    dogs_list = [x['name'] for x in dog]
    buttons = [{'title':dog,'payload':'/fav_breed{"fav_breed":'+dog+"}"} for dog in dogs_list]
elif len(dog) == 1:
    dog = dog[0]
    dog_name = dog['name']
    try:
        dog_temp = dog['temperament'].split(",")
        dog_temp = [x.strip(' ') for x in dog_temp]
    except: 
        dog_temp = []
    search_img_breed_id_url = 'https://api.thedogapi.com/v1/images/search?breed_id=' + str(dog['id'])
    dog_pic_json = re.get(search_img_breed_id_url, headers={"x-api-key":ac.dog_key}).json()
    if dog_pic_json:
        dog_pic_url = dog_pic_json[0]['url']
else:
    dogs = ''

print('bla')
