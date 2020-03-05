from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests as re 
import json

class TellChuckNorrisJoke(Action):

    def name(self) -> Text:
        return "action_tell_chuck_norris_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        joke = re.get('https://api.chucknorris.io/jokes/random').json()['value']
        dispatcher.utter_message(text=joke)

        return []