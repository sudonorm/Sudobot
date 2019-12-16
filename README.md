# :spades: Sudobot

This repo contains the files for a chatbot developed in Python, using the Rasa framework with custom actions.

Currently, Sudobot can tell Chuck Norris jokes and describe the weather in any location.

## 👷‍ Installation

To use the files in this repo, Rasa needs to be installed. Install Rasa by running:
```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```
This will install both Rasa and Rasa X, as well as all the libraries required by the bot.

Note that this bot should be used with python 3.6 or higher.

## 🤖 To run Sudobot:

- Navigate to the cloned repo's folder
- Follow the instructions in the `Endpoints.yml` and `actions.py` files
- Start a `cmd or powershell terminal` in the cloned repo's folder
- Use `rasa train` to train a model.
- To run the bot, first set up your action server in a terminal window using ```rasa run actions```
- Talk to the bot using `rasa shell` or `rasa interactive` to talk to the bot in training mode

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working 
under the hood. To simply talk to the bot, you can remove this flag.

## 👩‍💻 Overview of the files

`data/stories.md` - contains stories 

`data/nlu.md` - contains NLU training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

`endpoints.yml` - contains configuration data for tracker store

`models/` - folder into which trained model is stored

## :bulb: To use Rasa x:
- A tracker store needs to be set up
- Use `migrate_tracker_store_to_rasa_x.py` to migrate your tracker store to Rasa x
