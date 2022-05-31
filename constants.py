to_hear = {
    "verb": {
        # ESTAR
        "estás": "are",
        "tal": "are",
        # SER
        "es": "is",
        # CIERRA
        "cierra": "close",
        "quita": "close",
        # PONER
        "pon": "play",
        # ABRIR
        "ábreme": "open",
        "abre": "open",
        "enséñame": "open",
        # NADA
        "nada": "nothing",
        # HACER
        "añade": "make",
        "haz": "make",
        "realiza": "make",
        "crea": "make",
        # COPIAR
        "copia": "copy",
        # REVISAR
        "léeme": "check",
        "leer": "check",
        "revisa": "check",
        "revista": "check",
        "revisar": "check",
        "mira": "check",
        "mirar": "check"
    },
    "noun": {
        # CALENDARIO
        "calendario": "calendar",
        "proximo": "next",
        # EVENTO
        "evento": "event",
        "eventos": "event",
        # ARCHIVOS
        "archivos": "thunar",
        # TERMINAL
        "terminal": "terminal",
        "consola": "terminal",
        # MÚSICA
        "música": "spotify",
        "spotify": "spotify",
        "cancion": "song",
        # CONTROL MULTIMEDIA
        "play": "play",
        "para": "stop",
        "baja": "volume_down",
        "sube": "volume_up",
        "cambia": "next_song",
        "cambio": "next_song",
        "pasa": "next_song",
        "siguiente": "next_song",
        "anterior": "previous_song",
        # HORA
        "hora": "time",
        # COPIA
        "copia": "copy",
        # EMAIL
        "email": "email",
        "correo": "email",
        # CARPETA
        "carpeta": "folder",
        "directorio": "folder",
    },
    "conjunction": {
        # CÓMO
        "cómo": "how",
        # QUÉ
        "qué": "what",
    },
    "args": {
        "seguridad": "backup",
        "folder": {
            "universidad": "Universidad",
            "cuarto": "4º",
            "tercero": "3º",
            "segundo": "2º",
            "primero": "1º",
            "descargas": "Descargas",
            "documentos": "Documentos"
        },
        # APPS
        "apps": {
            # SPOTIFY
            "música": "spotify",
            "spotify": "spotify",
            # YOUTUBE
            "youtube": "brave-browser https://www.youtube.com/",
            # CALENDARIO
            "calendario": "https://calendar.google.com/calendar/r",
            # EMAIL
            "email": "brave-browser https://mail.google.com/mail/u/0/?pli=1#inbox",
            "alcor": "brave-browser https://mail.google.com/mail/u/0/?pli=1#inbox",
            "correo": "brave-browser https://mail.google.com/mail/u/0/?pli=1#inbox",
            # ECLIPSE
            "eclipse": "eclipse",
            # BROWSER
            "navegador": "brave-browser",

        }
    },
    "music_context": {
        "spotify": "music_context",
        # CONTROL MULTIMEDIA
        "play": "music_context",
        "para": "music_context",
        "baja": "music_context",
        "sube": "music_context",
        "cambia": "music_context",
        "cambio": "music_context",
        "pasa": "music_context",
        "siguiente": "music_context",
        "anterior": "music_context",

    },
    "time": {
        "un": "1",
        "una": "1",
        "hoy": "today",
        "dia": "day",
        "semana": "week",
        "semanas": "week",
        "mes": "month",
        "mañana": "tomorrow",
        "pasado": "day_after_tomorrow",
        "minutes": {
            "punto": "00",
            "media": "30",
            "cuarto": "15",
            "menos": "45"
        },

        "days": {
            "lunes": 0,
            "martes": 1,
            "miercoles": 2,
            "jueves": 3,
            "viernes": 4,
            "sabado": 5,
            "domingo": 6
        },
        "months": {
            "enero": "01",
            "febrero": "02",
            "marzo": "03",
            "abril": "04",
            "mayo": "05",
            "junio": "06",
            "julio": "07",
            "agosto": "08",
            "septiembre": "09",
            "octubre": "10",
            "noviembre": "11",
            "diciembre": "12",
        },
        "hora": "hour",
        "horas": "hour",
        "minuto": "minute",
        "minutos": "minute",
        "tarde": "afternoon",
    },
    "calendar": {
        "título": "title",
        "descripción": "description",
        "tipo": "type",
        "dirección": "location",
        "localización": "location",
        "recordatorio": "reminder",
        "duración": "duration",
        "empieza": "start_time",
        "acaba": "end_time"
    },
    "calendar_type": {
        "universidad": "10",
        "personal": "2",
        "persona": "2",
        "ocio": "1",
        "entrega": "4",
        "examen": "4",
        "irene": "3",
        "otros": "8",
        "indefinido": "8"
    },
    "ahora": "now",
    "hoy": "today",
    "no": "no",
    "sí": "yes",
    "si": "yes",
    "vale": "yes",
    "venga": "yes",
    "hugo": "name",
    "hotword": "asistente",
    "asistente": "name",
}
to_say = {
    "english": {
        "what_time_is_it": "It's",
        "how_are_you": ["I'm great, thank you!", "I'm fine"],
        "wrong_call": ["Ok", "I'm here if you need me"],
        "response": ["Yes sir", "Ready", "I'm here", "I'm listening"],
        "ok": ["Ok", "Done", "I'm on it"],
        "listening": "I'm listening",
        "email": {
            "check_email": "Ok, Checking your email",
            "no_email": "There is no new emails",
            "one_email": "You have one new email",
            "many_emails1": "You have ",
            "many_emails2": "new emails"
        },
        "backup": {
            "connected_device": "Device connected",
            "no_device": ["Connect the device please", "The device is not connected", "You need to connect the device first"],
            "problem_backup": "There was a problem doing the backup, check the logs",
            "init_backup": "Making a new backup of your system",
            "end_backup": "Backup finished",
            "title_ask_backup": "¿Do you want to add a title?"
        }
    },
    "español": {
        "anything_else": "¿Quieres añadir alguna opción más?",
        "what_time_is_it": "Son las",
        "how_are_you": ["Estoy muy bien, ¡Gracias!", "Estiy bien"],
        "wrong_call": ["De acuerdo", "Estoy aquí si necesitas algo"],
        "response": ["¿Sí?", "¿Sí?" "Lista", "Aquí estoy", "Te escucho"],
        "ok": ["Vale", "¡Vale!", "De acuerdo", "Hecho"],
        "listening": "Te escucho",
        "email": {
            "check_email": "Okay, revisando el correo",
            "no_email": "No tienes nuevos correos",
            "one_email": "Tienes un correo nuevo",
            "many_emails1": "Tienes ",
            "many_emails2": "correos nuevos"
        },
        "time": {
            "get_date_problem": "Perdona, ¿puedes repetir la fecha?",
            "bad_format": "Necesito que me digas el dia y la hora por favor",
        },
        "calendar": {
            "bad_type": "El tipo es inválido.",
            "make_event_problem": "Ha ocurrido un problema creando el evento. Por favor, consulta las trazas",
            "event_created": "Perfecto, tu evento ya está creado",
            "summary": "¿Cuál es el título del evento?",
            "description": "¿Cuál es la descripción?",
            "colorId": "¿De qué tipo es?",
            "location": "¿Dónde es el evento?",
            "recordatorio": "reminder",
            "start time": "¿A qué hora empieza?",
            "end time": "¿Cuándo acaba?"

        },
        "backup": {
            "connected_device": "Disco duro detectado",
            "no_device": ["Conecta el disco duro por favor", "El disco duro no está conectado",
                          "Necesito que primero conectes el disco duro"],
            "problem_backup": "Ha ocurrido un problema haciendo la copia de seguridad, revisa las trazas",
            "init_backup": "Se ha empezado ha hacer la copia de seguridad",
            "end_backup": "Copia de seguridad acabada",
            "title_ask_backup": "¿Quieres poner un título?"
        }
    },
}

attributes = {
    "context": "",
    "context_flag": False,
    "alarms": [],
    "reminders": {},
    'hotword': 'asistente',
    "pwd": "/home/javi/Programs/PycharmProjects/pyAssistant/"

}
