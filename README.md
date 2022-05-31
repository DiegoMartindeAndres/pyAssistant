# Virtual Assistant made in Python aiming to facilitate learning this language.
The idea is to make a virtual assistant that doesn't need to recieve voice commands.

It detects when my Mi Band is nearby throught bluetooth and notify about new emails, events in the calendar...

It can also interpret commands, differenciating between verbs and nouns, just to be able to interpret the same order said with different words and to give it the ability to interpret different parameters for the same command.

### Features
     Check email and notify them
     Check for events on Google Calendar and notify when needed
     Add events to Google Calendar
     Make a backup to external drive
     Open file explorer on specific path
     Open terminal on specific path
     In the evening, suggest an alarm for the next day dependiong on events in calendar (not finished)
     Play Spotify music and control volume
     Run specific app
     Check whenever Mi Band is close by Bluetooth scanning to notify new events, making a buffer of notifications not notified yet.


### Dependencies

* For sox:
```
sudo apt-get install sox libsox-fmt-mp3
* ```

* For PyAudio:
```
sudo apt-get install portaudio19-dev python-pyaudio
```