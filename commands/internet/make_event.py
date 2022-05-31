"""from __future__ import print_function
import httplib2
import os

import commands.voice_recognition as vr
from commands.text2speech import to_say
from constants import to_hear as words_hear
from constants import to_say as words_say
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from interpreter.time import get_hour
from interpreter.time import get_date
from logs.log import log
from logs.log import exception

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.events'
CLIENT_SECRET_FILE = '../../credentials.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def make_event(arg):

    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


    1: blue
    2: green
    3: purple
    4: red
    5: yellow
    6: orange
    7: turquoise
    8: gray
    9: bold blue
    10: bold green
    11: bold red
    event = get_event()
    event = {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'colorId': '3',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2020-04-24T08:15:00',
            'timeZone': 'Europe/Madrid',
        },
        'end': {
            'dateTime': '2020-04-24T08:16:00',
            'timeZone': 'Europe/Madrid',

        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
        
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    to_say(words_say["español"]["calendar"]["event_created"])
    print('Event created: %s' % (event.get('htmlLink')))
    log("MAKE_EVENT", "make_event", "Evento creado con éxito: " + str(event))
    


def get_event():
    event = {
        'summary': '',
        'location': '',
        'colorId': '',
        'description': '',
        'start': {
            'dateTime': '',
            'timeZone': 'Europe/Madrid',
        },
        'end': {
            'dateTime': '',
            'timeZone': 'Europe/Madrid',

        },
        'recurrence': [
        ],
        'attendees': [

        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                # {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 30},
            ],
        },
    }
    done = False
    to_fill = ""
    while not done:
        if event["summary"] is "":
            to_fill = "summary"
        elif event["colorId"] is "":
            to_fill = "colorId"
        elif event["start"]["dateTime"] is "":
            to_fill = "start time"
        elif event["end"]["dateTime"] is "":
            to_fill = "end time"
        else:
            if not done:
                to_say(words_say["español"]["anything_else"])
                voice_command = vr.time_recognition()
                voice_words = voice_command.split()
                if voice_command is not "":
                    for word in voice_words:
                        if word in words_hear["calendar"]:
                            to_fill = words_hear["calendar"][word]
                            break
                        if "no" in voice_command:
                            done = True
                            to_fill = ""
                            break
                continue
        if to_fill is not "":
            to_say(words_say["español"]["calendar"][to_fill])
            voice_command = vr.time_recognition()
            if voice_command is not "":
                if to_fill is "colorId":
                    try:
                        event[to_fill] = words_hear["calendar_type"][voice_command]
                    except:
                        to_say(words_say["español"]["calendar"]["bad_type"])
                        continue
                    continue
                if "time" in to_fill:
                    if "a las" in voice_command:
                        event[to_fill.split()[0]]["dateTime"] = get_date(voice_command.split("a las")[0]) \
                                                                + get_hour(voice_command.split("a las")[1])
                    elif "a la" in voice_command:
                        event[to_fill.split()[0]]["dateTime"] = get_date(voice_command.split("a la")[0]) \
                                                                + get_hour(voice_command.split("a la")[1])
                    else:
                        to_say(words_say["español"]["time"]["bad_format"])
                else:
                    event[to_fill] = voice_command
    return event

"""