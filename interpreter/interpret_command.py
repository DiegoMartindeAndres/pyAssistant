import datetime

from constants import to_hear as words_hear
from interpreter.run_command import run_command
from logs.log import log


def static_phrases(voice_command):
    text = ""
    if ' '.join(str(e) for e in voice_command) is "cómo estás" or ' '.join(str(e) for e in voice_command) is "qué tal":
        text = "Bien, ¡gracias!"
    elif ' '.join(str(e) for e in voice_command) is "qué hora es":
        date = str(datetime.datetime.now())
        text = "son las " + date[11:16]
    if text is not "":
        to_say(text)
        log("interpret_command", "static_phrases", "text: " + text)


def get_command(voice_words, voice_command):
    command = []
    verb = ""
    noun = ""
    noun2 = ""
    arg = ""
    for word in voice_words:
        if word in words_hear["verb"] and verb is "":
            verb = words_hear["verb"][word]
        if word in words_hear["noun"] and noun is "":
            noun = words_hear["noun"][word]
        if word in words_hear["noun"] and noun2 is "" and noun is not "":
            noun2 = words_hear["noun"][word]
        if word in words_hear["conjunction"] and noun is "":
            noun = words_hear["conjunction"][word]
        if word in words_hear["args"]["folder"] and arg is "":
            if "folder" not in noun and "terminal" not in noun:
                noun = "folder"
            arg = words_hear["args"]["folder"][word]
        if word in words_hear["args"]["apps"] and verb == "open" or word in words_hear["args"]["apps"] and verb == "close":

            noun = "apps"
            arg = words_hear["args"]["apps"][word]
        if word in words_hear["args"]:
            arg = words_hear["args"][word]
    if noun is "what" and verb is "are":
        arg = noun
        noun = words_hear["conjunction"]["cómo"]
    elif noun is "what" and verb is "is":
        arg = noun2
    command.append(verb)
    command.append(noun)
    command.append(arg)
    log("INTERPRET_COMMAND", "get_command", "Comando interpretado: " + ' '.join(str(e) for e in command))
    print(command)
    run_command(command, voice_command)
