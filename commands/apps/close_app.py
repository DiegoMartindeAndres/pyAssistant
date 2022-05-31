import datetime
import os
import subprocess
import time
import random

from TTS import to_say
from constants import to_say as words_say

from logs.log import log
from logs.log import exception


def close_apps(app):
    try:
        to_say(random.choice(words_say["español"]["ok"]))
        if app is "spotify":
            from main import set_context
            set_context("")

        os.system("pkill " + app)
        log("CLOSE_APP", "close_app", "Cerrando el programa: " + app)

    except Exception as e:
        exception("RUN_APP", "run_app", str(e))
        return
