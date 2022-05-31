import wikipedia
import random

from TTS import to_say
from constants import to_say as words_say


def search_wiki(text):
    to_say(random.choice(words_say["español"]["response"]))
    result = wikipedia.summary(text, sentences=2)
    to_say(text)
    return
