
import os
import subprocess
import random

from constants import to_say as words_say
from TTS import to_say
from logs.log import log
from logs.log import exception


def open_terminal(folder):
    try:
        HOME = "/home/javi"
        to_say(random.choice(words_say["español"]["ok"]))
        return_path = subprocess.check_output(['pwd']).decode("utf-8").split("\n")
        if folder is "":
            dest = HOME
        else:
            dest = ""
            path = subprocess.check_output(['find', HOME, '-name', folder]).decode("utf-8").split("\n")
            for p in path:
                if "/." not in p:
                    dest = p
                    break

        if dest is not "":
            print("Destino:", dest)
            os.chdir(dest)
            os.system("konsole &")
            os.chdir(return_path[0])
            log("OPEN_TERMINAL", "open_terminal", 'Abriendo un terminal en la carpeta: ' + dest)
        return
    except Exception as e:
        exception("change_directory", "ch_dir", str(e))
        return


