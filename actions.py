# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import requests


#get the weather of a location from an api
class Actionweather(Action):
	def name(self):
		return 'action_weather'
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		loc = tracker.get_slot('location')
		#print(loc)
		#replace ACCESS_KEY with your access key. Visit weatherstack.com to get an access key
		request = json.loads(requests.get("http://api.weatherstack.com/current?access_key=ACCESS_KEY&query="+loc).text) # make an api call
		country = request['location']['country']
		city = request['location']['name']
		condition = request['current']['weather_descriptions'][0].lower()
		temperature = request['current']['temperature']
		humidity = request['current']['humidity']
		wind_kmh = request['current']['wind_speed']
		response = """It is currently {} in {} at the moment. The temperature is {} degrees Celsius, the humidity is {}% and the wind speed is {} kmh.""".format(condition, city, temperature, humidity, wind_kmh)
		dispatcher.utter_message(response)
		return []
		

#query an api for a joke	
class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        request = json.loads(
            requests.get("https://api.chucknorris.io/jokes/random").text
        )  # make an api call
        joke = request["value"]  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []
        
