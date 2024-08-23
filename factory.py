from abc import ABC, abstractmethod


# Define the Product Interface:
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass



# Implement Concrete Products:
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending email with message: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS with message: {message}")



#Define the Creator (Factory):
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

# Implement Concrete Creators:
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()


# Client Code:
def send_notification(factory: NotificationFactory, message: str):
    notification = factory.create_notification()
    notification.send(message)

# Usage
email_factory = EmailNotificationFactory()
sms_factory = SMSNotificationFactory()

send_notification(email_factory, "Hello via Email!")
send_notification(sms_factory, "Hello via SMS!")
