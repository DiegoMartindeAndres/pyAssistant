import datetime
import email
import imaplib
import random

from TTS import to_say
from constants import to_say as words_say


from logs.log import log
from logs.log import exception

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "muirst20" + ORG_EMAIL
FROM_PWD = "2021-muirst"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


def read_email_from_gmail(arg):
    log("READ_EMAIL", "read_email_from_gmail", "Accediendo a correos sin leer")
    to_say(random.choice(words_say["español"]["ok"]))

    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')
        type1, data = mail.search(None, 'UNSEEN')
        mail_ids = data[0]
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        if data is None:
            return
        emails = []
        text_to_say = words_say["español"]["email"]["no_email"]
        if first_email_id == latest_email_id:
            typ, data = mail.fetch(str(latest_email_id), '(RFC822)')
            text_to_say = words_say["español"]["email"]["one_email"]
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject: ' + email_subject + '\n')
                    emails.append(msg)

        else:
            for i in range(latest_email_id, first_email_id - 1, -1):
                typ, data = mail.fetch(str(i), '(RFC822)')
                text_to_say = words_say["español"]["email"]["many_emails1"] + str(latest_email_id - first_email_id + 1) + \
                    words_say["español"]["email"]["many_emails2"]
                if latest_email_id - first_email_id == 0:
                    text_to_say = words_say["español"]["email"]["one_email"]
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print('From : ' + email_from + '\n')
                        print('Subject : ' + email_subject + '\n')
                        emails.append(msg)
        to_say(text_to_say)

    except Exception as e:
        to_say(words_say["español"]["email"]["no_email"])
        exception("READ_EMAIL", "read_email_from_gmail", str(e))
