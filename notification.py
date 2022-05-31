import datetime


class Notification:
    def __init__(self, id_notification="", title="", source=""):
        self.id_notification = id_notification
        self.title = title
        self.source = source

        self.out_of_date = False
        self.notified = False

    def get_id(self):
        return self.id_notification

    def get_title(self):
        return self.title

    def get_source(self):
        return self.source

    def get_date(self):
        return self.date

    def get_reminder(self):
        return self.reminder

    def get_out_of_date(self):
        return self.out_of_date

    def get_notified(self):
        return self.notified


    def set_id(self, id_notification):
        self.id_notification = id_notification

    def set_title(self, title):
        self.title = title

    def set_source(self, source):
        self.source = source

    def set_date(self, date):
        self.date = date

    def set_reminder(self, reminder):
        self.reminder = reminder

    def set_out_of_date(self, out_of_date):
        self.out_of_date = out_of_date

    def set_notified(self, notified):
        self.notified = notified
