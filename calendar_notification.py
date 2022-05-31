from notification import Notification


class CalendarNotification(Notification):

    def __init__(self, id_notification="", title="", source="", date="", reminder=""):
        super().__init__(id_notification, title, source)
        self.date = date
        self.reminder = reminder

    """     GETTERS     """

    def get_date(self):
        return self.date

    def get_reminder(self):
        return self.reminder

    """     SETTERS     """

    def set_date(self, date):
        self.date = date

    def set_reminder(self, reminder):
        self.reminder = reminder

