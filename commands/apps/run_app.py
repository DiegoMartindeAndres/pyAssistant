import os
import subprocess
import time
import random

from TTS import to_say
from constants import to_say as words_say

from logs.log import log
from logs.log import exception


def open_apps(app):
    try:
        to_say(random.choice(words_say["español"]["ok"]))

        if app is "spotify":
            from main import set_context
            set_context("music_context")
            log("PLAY_MUSIC", "play_music", "Contexto cambiado a music_context")
            ps = subprocess.Popen(('ps', 'aux'), stdout=subprocess.PIPE)
            output = subprocess.check_output(('grep', 'spotify'), stdin=ps.stdout)
            ps.wait()
            if len(output.decode("utf-8").split("\n")) == 2:
                return_path = subprocess.check_output(['pwd']).decode("utf-8").split("\n")
                os.system(app + " &")
                os.chdir(return_path[0])
            time.sleep(1)
            os.system("playerctl play")
        else:
            return_path = subprocess.check_output(['pwd']).decode("utf-8").split("\n")
            os.system(app + " &")
            os.chdir(return_path[0])
        log("RUN_APP", "run_app", "Abriendo el programa: " + app)
        return
    except Exception as e:
        exception("RUN_APP", "run_app", str(e))
        return


