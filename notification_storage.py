import datetime
import pickle

from bluetoothNearBy import near_by
from TTS import to_say
from logs.log import log
import constants

pwd = constants.attributes['pwd']

all_notifications = []
notifications_to_say_now = []


def check_notifications():
    global all_notifications
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'rb') as f:  # Python 3: open(..., 'rb')
        all_notifications = pickle.load(f)
    log("NOTIFICATION_STORAGE", "CHECK_NOTIFICATION", "OBTENIENDO NOTIFICACIONES DEL FICHERO")
    notification_time_out()


def notification_time_out():
    global all_notifications, notifications_to_say_now
    log("NOTIFICATION_STORAGE", "NOTIFICATION_TIME_OUT", "COMPROBANDO SI HAY NOTIFICACIONES QUE DECIR")
    for notification in all_notifications:
        if notification.get_title() == "Test":
            continue
        notification_date = datetime.datetime.strptime(str(notification.get_date()), '%Y-%m-%d %H:%M:%S')
        notification_reminder = datetime.datetime.strptime(str(notification.get_reminder()), '%Y-%m-%d %H:%M:%S')
        time_delta_notification = datetime.datetime.now() - notification_reminder
        out_of_date = bool(notification.get_out_of_date())
        print("NOTIFICATION_TIME_OUT: " + str(notification.get_out_of_date()))
        if out_of_date:
            log("NOTIFICATION_STORAGE", "NOTIFICATION_TIME_OUT", "HAY UNA NOTIFICACION DESACTUALIZADA")
            add_notifications_to_say_now(notification)
            continue
        try:
            if check_five_minutes_before(time_delta_notification):
                add_notifications_to_say_now(notification)
                continue

        except:
            pass
        try:
            if check_five_minutes_after(time_delta_notification):
                add_notifications_to_say_now(notification)
                continue
        except:
            pass
    notify()


def add_notifications_to_say_now(notification):
    log("NOTIFICATION_STORAGE", "ADD_NOTIFICATIONS_TO_SAY_NOW", "AÑADIENDO LA NOTIFICACION AL ARRAY PARA NOTIFICAR "
                                                                "Y BORRANDOLA DEL TOTAL")

    notifications_to_say_now.append(notification)
    print("Notificacion notificada? ", notification.get_notified(), notification.get_title())
    all_notifications.remove(notification)


def check_five_minutes_before(time_delta_notification):
    # Si la fecha esta por detras de la hora actual, el formato es 23:55:00 (05 minutos atras)
    hours = int(str(time_delta_notification)[8:(len(str(time_delta_notification)) - 13)])
    minutes = int(str(time_delta_notification)[11:(len(str(time_delta_notification)) - 10)])

    return hours == 23 and minutes > 55


def check_five_minutes_after(time_delta_notification):
    # Si la fecha esta por delante de la hora actual, el formato es 00:05:00 (dentro de 05 minutos)
    hours = int(str(time_delta_notification)[0:1])
    minutes = int(str(time_delta_notification)[2:(len(str(time_delta_notification)) - 10)])

    return hours == 0 and minutes < 5


def update_notification_storage():
    global all_notifications, pwd
    log("NOTIFICATION_STORAGE", "UPDATE_NOTIFICATION_STORAGE", "ACTUALIZANDO FICHERO DE NOTIFICACIONES")
    for notification in all_notifications:
        print("NOTIFICACIONES;", notification.get_title(), str(notification.get_notified()),
              notification.get_reminder())
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(all_notifications, f)
    with open(pwd + 'ImportantFiles/notifications.pkl',
              'rb') as f:  # Python 3: open(..., 'rb')
        all_notifications = pickle.load(f)


def checks_to_notify():
    global notifications_to_say_now
    if not len(notifications_to_say_now) != 0:
        log("NOTIFICATION_STORAGE", "CHECKS_TO_NOTIFY", "NO HAY NOTIFICACIONES PARA DECIR AHORA")
        return False
    if not near_by():
        log("NOTIFICATION_STORAGE", "CHECKS_TO_NOTIFY", "LA PULSERA NO ESTA CERCA")
        return False
    return True


def notify():
    global notifications_to_say_now, all_notifications
    text_to_say = ""
    log("NOTIFICATION_STORAGE", "NOTIFY", "COMPROBANDO QUE ES MOMENTO DE NOTIFICAR")
    if checks_to_notify():
        for notification in notifications_to_say_now:
            if not notification.get_notified():
                print(notification.get_notified())
                if notification.get_source() == "calendar":
                    hour = notification.get_date()[11:16]
                    text_to_say = text_to_say + "Tienes un evento. " + str(notification.get_title()) + ". A las " + hour
                notification.set_notified(True)

                all_notifications.append(notification)
                to_say(text_to_say)
            else:
                print("notificacion ya notificada")
                all_notifications.append(notification)
            text_to_say = ""
        log("NOTIFICATION_STORAGE", "NOTIFY", "ACTUALIZANDO ARRAYS")

        notifications_to_say_now.clear()
        update_notification_storage()
    else:
        log("NOTIFICATION_STORAGE", "NOTIFY", "NO ES MOMENTO DE NOTIFICAR")
        save_notifications()


def save_notifications():
    global notifications_to_say_now
    log("NOTIFICATION_STORAGE", "SAVE_NOTIFICATIONS", "SE GUARDAN LAS NOTIFICACIONES PARA LUEGO")

    for notification in notifications_to_say_now:
        notification.set_out_of_date(True)
        all_notifications.append(notification)
    notifications_to_say_now.clear()
    update_notification_storage()
