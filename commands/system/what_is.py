import datetime

from TTS import to_say
from logs.log import log
from constants import to_say as words_say




def is_what(arg):
    text = ""
    if arg is "time":
        date = str(datetime.datetime.now())
        text = words_say["español"]["what_time_is_it"] + date[11:16]
    to_say(text)
    log("WHAT_IS", "is_what(time)", "text: " + text)
