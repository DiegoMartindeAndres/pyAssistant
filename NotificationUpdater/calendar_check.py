from __future__ import print_function

import datetime

import pickle
import os.path
from logs.log import log
from logs.log import exception
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from calendar_notification import CalendarNotification
import constants

pwd = constants.attributes['pwd']
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    global pwd
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(pwd + 'ImportantFiles/token_calendar.pickle'):
        with open(pwd + 'ImportantFiles/token_calendar.pickle', 'rb') as token:
            creds = pickle.load(token)
            print(creds)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                pwd + 'ImportantFiles/credentials_calendar.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(pwd + 'ImportantFiles/token_calendar.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    log("CALENDAR_CHECK", "MAIN", "OBTENIENDO LOS SIGUIENTES 10 EVENTOS DEL CALENDARIO")
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        log("CALENDAR_CHECK", "MAIN", "NO HAY EVENTOS ENCONTRADOS")
    """
    os.system("rm ImportantFiles/notifications.plk'; touch ImportantFiles/notifications.plk")
    test1 = CalendarNotification("0", "Test", "Test", "Test", "Test")
    test2 = CalendarNotification("0", "Test", "Test", "Test", "Test")
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([test1, test2], f)
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([], f)"""
    for event in events:
        log("CALENDAR_CHECK", "MAIN", "EVENTO: " + event['summary'])
        start = format_calendar_date(event['start'].get('dateTime', event['start'].get('date')))
        if len(start) < 12:
            start = start + " 00:00:00"
        id_notification = str(event["id"])
        title = event['summary']
        source = "calendar"
        try:
            reminder = format_reminder_date(event['reminders'], start)

        except Exception as e:
            exception("CALENDAR_CHECK", "MAIN", "EL EVENTO NO TIENE RECORDATORIO, SE ASIGNA LA FECHA DE COMIENZO: "
                      + str(e))
            reminder = start
        notification_to_add = CalendarNotification(id_notification, title, source, start, reminder)
        if check_if_added(notification_to_add):
            log("CALENDAR_CHECK", "MAIN", "EVENTO: " + event['summary'])
            add_notification(notification_to_add)


def add_notification(notification_to_add):
    log("CALENDAR_CHECK", "ADD_NOTIFICATION", "ACTUALIZANDO EL FICHERO DE NOTIFICATIONES")
    try:
        with open(pwd + 'ImportantFiles/notifications.pkl',
                'rb') as f:  # Python 3: open(..., 'rb')
            all_notifications = pickle.load(f)
    except Exception as e:
        exception("CALENDAR_CHECK", "ADD_NOTIFICATION", "NO HAY NOTIFICACIONES GUARDADAS TODAVIA: " + str(e))
        all_notifications = []
    all_notifications.append(notification_to_add)
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(all_notifications, f)



def check_if_added(notification_to_add):
    log("CALENDAR_CHECK", "CHECK_IF_ADDED", "COMPROBANDO SI LA NOTIFICACION YA ESTABA DESCARGADA")

    try:
        with open(pwd + 'ImportantFiles/notifications.pkl',
                  'rb') as f:  # Python 3: open(..., 'rb')
            all_notifications = pickle.load(f)

        for notification in all_notifications:
            if str(notification_to_add.get_id()) == notification.get_id():
                log("CALENDAR_CHECK", "CHECK_IF_ADDED", "LA NOTIFICACION YA ESTABA DESCARGADA")
                return False
        log("CALENDAR_CHECK", "CHECK_IF_ADDED", "LA NOTIFICACION NO ESTABA DESCARGADA")
        return True
    except Exception as e:
        exception("CALENDAR_CHECK", "CHECK_IF_ADDED", "EL DOCUMENTO ESTABA VACIO, SE AÑADE LA NOTIFICACION: " + str(e))
        os.system("touch " + pwd + "ImportantFiles/notifications.pkl; sleep 1")
        return True


def format_reminder_date(reminder, start):
    start_formatted = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    if reminder['useDefault']:
        minutes = 30
    else:
        minutes = int(reminder['overrides'][0]['minutes'])
    reminder_date = start_formatted - datetime.timedelta(minutes=minutes)
    log("CALENDAR_CHECK", "FORMAT_REMINDER_DATE", "OBTENIENDO LA HORA DEL RECORDATORIO: " + str(reminder_date))

    return reminder_date


def format_calendar_date(calendar_date):
    date = calendar_date[0:10] + " "
    time = calendar_date[11:19]
    log("CALENDAR_CHECK", "FORMAT_CALENDAR_DATE",
        "FORMATEANDO LA FECHA DE GOOGLE: " + calendar_date + ", A: " + date + time)
    return date + time


if __name__ == '__main__':
    main()
