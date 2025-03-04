class Notification:
    def send(self):
        print("Sending a notification.")


class EmailNotification(Notification):
    def send(self):
        print("Sending an email notification.")


class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification.")

notification = Notification()
email_notification = EmailNotification()
sms_notification = SMSNotification()

notification.send()
email_notification.send()
sms_notification.send()