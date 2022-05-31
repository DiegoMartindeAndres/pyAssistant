import pickle
import datetime
import time
import constants

from logs.log import log
from logs.log import exception

from notification_storage import check_notifications
from NotificationUpdater import calendar_check

pwd = constants.attributes['pwd']

def main():
    from main import mutex
    from main import check_context
    while True:
        #mutex.acquire(1)
        check_context()
        calendar_check.main()
        remove_past_notifications()
        check_notifications()

        #mutex.release()
        time.sleep(60)



def remove_past_notifications():
    all_notifications = get_notification_from_file()

    for notification in all_notifications:
        if is_notification_in_past(notification.get_date()):
            all_notifications.remove(notification)

    update_notification_file(all_notifications)


def update_notification_file(all_notifications):
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(all_notifications, f)


def get_notification_from_file():
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'rb') as f:  # Python 3: open(..., 'rb')
        return pickle.load(f)


def is_notification_in_past(notification_date):
    now = datetime.datetime.now()
    notification_date_formatted = datetime.datetime.strptime(notification_date, '%Y-%m-%d %H:%M:%S')
    time_delta_notification = now - notification_date_formatted
    # Si la fecha esta por detras de la hora actual, el formato es 23:55:00 (05 minutos atras)
    try:

        hours = int(str(time_delta_notification)[0:1])
        minutes = int(str(time_delta_notification)[2:(len(str(time_delta_notification)) - 10)])

        return hours >= 1
    except Exception as e:
        return False
