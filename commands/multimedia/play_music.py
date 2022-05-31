import os
import subprocess
import time
import random

from logs.log import log
from constants import to_say as words_say
from TTS import to_say


def play_music(arg):
    from main import set_context

    to_say(random.choice(words_say["español"]["ok"]))
    set_context("music_context")
    log("PLAY_MUSIC", "play_music", "Contexto cambiado a music_context")
    ps = subprocess.Popen(('ps', 'aux'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('grep', 'spotify'), stdin=ps.stdout)
    ps.wait()
    if len(output.decode("utf-8").split("\n")) == 2:
        return_path = subprocess.check_output(['pwd']).decode("utf-8").split("\n")
        os.system("spotify &")
        os.chdir(return_path[0])
        time.sleep(1)
        os.system("playerctl play")
    else:
        os.system("playerctl play")
