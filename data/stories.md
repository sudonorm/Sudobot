## happy path
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
* mood_unhappy
  - action_joke
  - utter_did_that_help
* affirm
  - utter_happy
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye
 
## sad path 2
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
* mood_unhappy
  - action_joke
  - utter_did_that_help
* deny
  - action_joke
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## story_location_01
* inform{"location": "Hamburg"}
 - action_weather
	
## story_location_02
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
* inform{"location": "Hamburg"}	
 - action_weather
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye
 
## story_greet 
* greet 
 - utter_name 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
 
## story_joke_01
* joke
 - action_joke
 
## story_joke_02
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 

## interactive_story_1
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
* joke
  - action_joke

## interactive_story_2
* greet
  - utter_name
* name{"name": "A"}
  - utter_greet
* mood_unhappy
  - action_joke
  - utter_did_that_help
* deny
  - utter_cheer_up
  - action_joke
* thanks
  - utter_thanks

## interactive_story_3
* inform{"location": "Hamburg"}
    - slot{"location": "Hamburg"}
    - action_weather
