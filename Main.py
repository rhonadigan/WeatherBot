# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Imports
import datetime as dt
import json
import requests
import pandas as pd
import time
import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"
responses = {
    "What is your name?": ["My name is Bot", "Bot is my name", "I'm called Bot"],
    "What is the weather?": ' ',
    "Where are you?": "I am in 1 Creechruch Place"
}

weather_key = '25d741bd-8efa-40f6-a93a-ef72f478f85f'
weatherTypes = {'temperature': 'T', 'weather type': 'W', 'precipitation': 'Pp', 'wind speed': 'W'}


def respond(message):
    time.sleep(0.5)

    if message in responses:

        if message.find('weather') != -1:

            weatherMessage = weather(0, 'temperature')

            return weatherMessage

        else:

            return random.choice(responses[message])

    else:
        return "I do not know, sorry :("


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


def weather(forecastday, Wtype):
    forecastday = 0
    Wtype = 'temperature'
    # Getting the pokemon url
    url = r'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/513?res=3hourly&key={}'.format(weather_key)

    # get weather type code
    weathertype = weatherTypes[Wtype]

    # Doing the request
    r = requests.get(url)

    data = json.loads(r.text)

    # T = temperature, W = weather type, Pp = precip prob, S = wind Speed
    temp = data['SiteRep']['DV']['Location']['Period'][forecastday]['Rep'][0][weathertype]
    rain = data['SiteRep']['DV']['Location']['Period'][forecastday]['Rep'][0]['Pp']

    message = 'The current temperature is {} degress. The propbaility of rain is {}%'.format(temp, rain)

    return message


send_message('What is your name?')
send_message("What is the weather?")

#    sitelist = r'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/sitelist'
