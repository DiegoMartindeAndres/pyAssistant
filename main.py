import time
import random
import subprocess
import time
import commands.voice_recognition as vr
import os
from TTS import to_say
from bluetoothNearBy import near_by
from threading import Thread
from threading import Lock
from interpreter.time import get_hour
from constants import to_hear as words_hear
from constants import to_say as words_say
from constants import attributes
from interpreter.interpret_command import get_command
from logs.log import log
from notification_storage import check_notifications
from NotificationUpdater import notification_updater
from logs.log import log
from logs.log import exception
import constants

pwd = constants.attributes['pwd']

call_flag = False
mutex = Lock()


def get_call(voice_command, hotword_flag):
    voice_words = voice_command.split()
    global call_flag
    if call_flag:
        call_flag = False
        get_command(voice_words, voice_command)
    for word in voice_words:
        if attributes["context"] == "music_context" and word in words_hear["music_context"]:
            get_command(voice_words, voice_command)
        if word in words_hear:
            if hotword_flag:
                os.system("play " + pwd + "AudioFiles/time-is-now.mp3 ")

                if len(voice_words) > 1:
                    get_command(voice_words, voice_command)
                    break
                #to_say(random.choice(words_say["español"]["response"]))
                call_flag = True
                break
    return


def set_context(new_context):
    attributes["context_flag"] = True
    attributes["context"] = new_context
    attributes["context_flag"] = False
    log("MAIN", "set_context", "Contexto actualizado a: " + attributes["context"])


def get_context():
    while attributes["context_flag"]:
        time.sleep(0.1)
    return attributes["context"]


def check_context():
    if attributes["context"] == "":
        return
    if attributes["context"] == "music_context":
        ps = subprocess.Popen(('ps', 'aux'), stdout=subprocess.PIPE)
        output = subprocess.check_output(('grep', 'spotify'), stdin=ps.stdout)
        ps.wait()
        if len(output.decode("utf-8").split("\n")) == 2:
            set_context("")
            log("MAIN", "check_context", "Contexto reiniciado")


def main_thread():
    global mutex
    attributes["context"] = ""
    while True:

        mutex.acquire(1)

        if not attributes["context_flag"] and get_context() == "music_context":
            voice_command = vr.time_recognition()
            if not voice_command == "":
                log("MAIN", "main()", "Contexto: music_context:" + voice_command)
                get_call(voice_command)
        else:
            voice_command, hotword_flag = vr.voice2speech()
            if not voice_command == "":
                log("MAIN", "main()", voice_command)
                get_call(voice_command, hotword_flag)
        mutex.release()
        #time.sleep(1)


def main():
    from NotificationUpdater.notification_updater import main as notification_system
    from main import main_thread
    attributes["pwd"] = os.system('pwd')
    voice_recon_thread = Thread(target=main_thread, args=())
    notification_thread = Thread(target=notification_system, args=())
    voice_recon_thread.start()
    notification_thread.start()
    count = 0






# Hora actual
# Comprobar notificaciones
# Comprobar si estoy en la habitacion
# Notificar

# Comprobar aplicaciones (Nuevos correos, nuevos eventos)
# Crear notificacion y guardarla.


if __name__ == '__main__':
    main()
