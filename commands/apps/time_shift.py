
import threading
import subprocess
import commands.voice_recognition as vr
from TTS import to_say
from TTS import saying
import random
import os
import datetime
import time

from constants import to_hear as words_hear
from constants import to_say as words_say

from logs.log import log
from logs.log import exception


def on_exit():
    while saying:
        time.sleep(1)
    to_say((words_say["español"]["backup"]["end_backup"]))
    log("TIME_SHIFT", "config_backup", "Copia de seguridad terminada. ")

    return


def init_backup(on_exit, popen_args):
    """
    Runs the given args in a subprocess.Popen, and then calls the function
    on_exit when the subprocess completes.
    on_exit is a callable object, and popen_args is a list/tuple of args that 
    would give to subprocess.Popen.
    """
    try:
        def run_in_thread(on_exit, popen_args):
            proc = subprocess.Popen(popen_args)#popen_args)
            proc.wait()
            on_exit()
            return
        thread = threading.Thread(target=run_in_thread, args=(on_exit, popen_args))
        thread.start()
        # returns immediately after the thread starts
        return thread
    except Exception as e:
        to_say(random.choice(words_say["español"]["problem_backup"]))
        exception("TIMESHIFT", "init_backup", str(e))
        return


def check_device():
    devices = subprocess.check_output(['sudo', '-A', 'fdisk', '-l']).decode("utf-8").split("\n")
    for i in range(len(devices) - 1, 0, -1):
        if "745,2G 83 Linux" in devices[i]:
            return devices[i][0:9]
    return ""


def config_backup(argument):
    device = check_device()
    while device is "":
        to_say(random.choice(words_say["español"]["backup"]["no_device"]))
        time.sleep(5)
        device = check_device()
    to_say((words_say["español"]["backup"]["connected_device"]))
    answered = False
    popen_args = ["sudo", "-A", "timeshift"]
    arg = ""
    to_say((words_say["español"]["backup"]["title_ask_backup"]))
    while not answered:
        voice_command = vr.time_recognition()
        voice_words = voice_command.split()
        print(voice_words)
        for word in voice_words:
            print(word)
            print(word in words_hear)
            print(words_hear["no"])
            if word in words_hear:
                if words_hear[word] == "yes":
                    answered = True
                    to_say((words_say["español"]["listening"]))
                    while True:
                        voice_command = vr.voice2speech()
                        arg = "--create --comments " + voice_command
                        to_say(random.choice(words_say["español"]["ok"]))
                        break
                    break
                elif words_hear[word] == "no":
                    answered = True
                    arg = "--create"
                    break

    if len(arg) is not 0:
        popen_args.append(arg)
        print(popen_args)
        log("TIME_SHIFT", "config_backup", "Haciendo una copia de seguridad. ")
        to_say(words_say["español"]["backup"]["init_backup"])
        init_backup(on_exit, popen_args)
        return
