from commands.system.open_terminal import open_terminal
from commands.system.open_folder import open_folder
from commands.system.what_is import is_what
from commands.system.how_are import are_how
from commands.apps.time_shift import config_backup as make_copy
from commands.apps.run_app import open_apps
from commands.apps.close_app import close_apps
from commands.multimedia.volume_up import volume_up as _volume_up
from commands.multimedia.volume_down import volume_down as _volume_down
from commands.multimedia.next_song import next_song as play_next_song
from commands.multimedia.previous_song import previous_song as play_previous_song
from commands.multimedia.play_music import play_music as play_spotify
from commands.multimedia.volume_up import volume_up as _volume_up
from commands.internet.search_wiki import search_wiki
#from commands.internet.make_event import make_event
from commands.internet.read_email import read_email_from_gmail as check_email
from logs.log import log
from logs.log import exception


def run_command(command, voice_command):
    try:
        if command[1] is "next_song" or command[1] is "previous_song":
            command[0] = "play"
        evaluation = command[0] + "_" + command[1] + "(" + '\'' + command[len(command) - 1] + '\'' + ")"
        eval(evaluation)
        command.clear()
        log("RUN_COMMAND", "run_command", "Ejecutando la funcion:" + evaluation)
        return
    except Exception as e:

        exception("RUN_COMMAND", "run_command", str(e))


""" if "open" in command:
        query = ""
        voice_words = voice_command.split()
        for word in voice_words:
            query = query + word + '+'
        query = query[0:len(query) - 1]
        query = "https://duckduckgo.com/?q=" + query + "&t=brave&ia=web"
        open_apps("brave-browser " + query)
        
        
        
        
        if "folder" in command:
            to_say(random.choice(words_say["ok"]))
            open_folder(command.pop())
        if "apps" in command:
            to_say(random.choice(words_say["ok"]))
            open_apps(command.pop())
    if "make" in command:
        if "backup" in command:
            to_say(random.choice(words_say["ok"]))
            config_backup()
    if "check" in command:
        if "email" in command:
            to_say((words_say["email"]["check_email"]))
            read_email() 
            """
