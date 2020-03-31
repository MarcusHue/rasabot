from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests as re 
import json
import time
import api_creds

class TellDadJoke(Action):

    def name(self) -> Text:
        return "action_tell_dad_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        joke = re.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"}).json()['joke']
        dispatcher.utter_message(text=joke)

        return []

class ShowDog(Action)

    def name(self) -> Text:
        return "action_show_dog"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_string = tracker.get_slot('dog_breed')
        search_breed_id_url = 'https://api.thedogapi.com/v1/breeds/search?q=' + search_string
        dog = re.get(search_breed_id_url, headers={"x-api-key":ac.dog_key}).json()
        if len(dog) > 1:
            dogs_list = [x['name'] for x in dog]
            buttons = [{'title':dog,'payload':'/fav_breed{"fav_breed":'+dog+"}"} for dog in dogs_list]
            dispatcher.utter_button_message(text='Which breed do you mean?',buttons=buttons)
        else if len(dog) == 1:
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
            dog = []

        return []