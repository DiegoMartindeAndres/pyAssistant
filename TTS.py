import os
import subprocess

from google_speech import Speech
#from gtts import gTT
saying = False
import constants

pwd = constants.attributes['pwd']

def to_say(text):
    global saying
    saying = True
    playing = False
    player_status = subprocess.run(['playerctl', 'status'], stdout=subprocess.PIPE)
    playing = "Playing" in str(player_status.stdout)
    os.system("playerctl stop")
    print("saying", saying)

    lang = "es"
    speech = Speech(text, lang)

    speech.play()

    saying = False
    if playing:
        os.system("playerctl play")
    print("saying", saying)
    return



