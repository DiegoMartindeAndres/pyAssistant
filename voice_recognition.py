import speech_recognition as sr
from constants import attributes

r = sr.Recognizer()


def voice2speech(threshold=200):
    global r
    hot_word = attributes['hotword']
    hotword_flag = False
    r.pause_threshold = 5
    with sr.Microphone() as source:
        audio = r.listen(source)
        #audio = r.record(source, duration=5)
        said = ""

        try:
            print("Empieza a reconocer")
            hotword_flag = False
            said = r.recognize_google(audio, language="es-ES")
            print("Reconoce")
            print(said)
            if hot_word in said.lower:
                hotword_flag = True

        except Exception as e:
            pass
            #print("Error:", str(e))
    return said.lower(), hotword_flag


def time_recognition():
    global r
    r.energy_threshold = 200
    r.dynamic_energy_threshold = False
    with sr.Microphone() as source:
        print("Empieza a escuchar")
        audio = r.record(source, duration=4)
        said = ""

        try:
            print("Empieza a reconocer")
            said = r.recognize_google(audio, language="es-ES")
            print("Reconoce")
            print(said)
        except Exception as e:
            print("E2rror:", str(e))
    return said.lower()
"""
    r = sr.Recognizer()
    r.energy_threshold = 400
    r.dynamic_energy_threshold = False
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-ES")
            return text

        except:
            print("Sorry could not recognize what you said")
            return ""
"""
