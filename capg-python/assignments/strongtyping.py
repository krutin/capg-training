
# Create multiple classes representing different notification channels (Email, SMS, and Push).
# Each channel class should implement the send method.
# Create a function that accepts any object and calls its send method.
#  The object should be able to handle the notification, even if its class is unknown
# demonstrate the above irrespective of type


class Email:
    def send(self):
        print("New Email Send")

class Sms:
    def send(self):
        print("New sms sent")

class Push:
    def send(self):
        print("Push message sent")

def myfunction(obj):
    obj.send()

d = Email()
myfunction(d)

h = Sms()
myfunction(h)

c = Push()
myfunction(c)