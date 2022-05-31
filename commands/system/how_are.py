import random

from TTS import to_say
from logs.log import log
from constants import to_say as words_say




def are_how(arg):
    text = random.choice(words_say["español"]["how_are_you"])
    to_say(text)
    log("WHAT_IS", "is_what(time)", "text: " + text)
