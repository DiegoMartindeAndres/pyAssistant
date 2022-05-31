import datetime

from constants import to_hear as words_hear
from constants import to_say as words_say
from TTS import to_say
from logs.log import log
from logs.log import exception


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def get_date(voice_command):
    try:
        now = datetime.datetime.now()
        weekday = datetime.datetime.today().weekday()
        # format = "2020-04-24T08:16:00"
        year = datetime.datetime.now().year
        day = datetime.datetime.now().day
        to_day = 0
        slot = 1
        if voice_command is "hoy":
            return str(year) + "-" + str(datetime.datetime.now().month) + "-" + str(day) + "T"
        voice_words = voice_command.split()
        for word in voice_words:
            if word in words_hear["time"]["months"]:
                month = words_hear["time"]["months"][word]
                return str(year) + "-" + str(month) + "-" + str(slot) + "T"
            if word in words_hear["time"]["days"]:
                to_day = words_hear["time"]["days"][word] - weekday
            if is_number(word):
                slot = int(word)
            if word in words_hear["time"]:
                if words_hear["time"][word] is "tomorrow":
                    to_day = to_day + 1
                if words_hear["time"][word] is "day_after_tomorrow":
                    to_day = to_day + 1
                if words_hear["time"][word] is "week":
                    to_day = slot * 7 + to_day
        date = now + datetime.timedelta(days=to_day)
        day = date.day
        month = date.month
        if date.month < 10:
            month = "0" + str(date.month)
        if date.day < 10:
            day = "0" + str(date.day)
        date_str = str(date.year) + "-" + str(month) + "-" + str(day) + "T"
        log("TIME", "get_date", "Fecha interpretada: " + date_str + " Comando: "+ voice_command)
        return date_str
    except Exception as e:
        to_say(words_say["español"]["time"]["get_date_problem"])
        exception("TIME", "get_date", str(e))
        return ""


def get_hour(voice_command):
    try:
        hour = datetime.datetime.now().hour
        minutes = "00"
        hours = 0
        if voice_command in words_hear and words_hear[voice_command] is "now":
            return str(hour) + ":" + str(datetime.datetime.now().minute) + ":00"
        voice_words = voice_command.split()
        for word in voice_words:
            if is_number(word):
                hours = int(word)
                if int(word) < 10:
                    hour = "0" + word
            if word in words_hear["time"]["minutes"]:
                minutes = words_hear["time"]["minutes"][word]
                if words_hear["time"]["minutes"][word] is "45":
                    hours -= 1
                    minutes = words_hear["time"]["minutes"][word]
                    break
        if hours < 10:
            hour = "0" + str(hours)
        if "tarde" in voice_command or "noche" in voice_command:
            hour = str(hours + 12)
        hour_str = str(hour) + ":" + str(minutes) + ":00"
        log("TIME", "get_hour", "Hora interpretada: " + hour_str + " Comando: "+ voice_command)
        return hour_str
    except Exception as e:
        to_say(words_say["español"]["time"]["get_date_problem"])
        exception("TIME", "get_hour", str(e))
        return ""

