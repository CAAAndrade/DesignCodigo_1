from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

# A partir de uma classe consigo definir a regra de construção de outras classes
# Definir a regra de construção
class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'Email message -> {message}')

# Definir a regra de construção
class SMSNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print (f'SMS message - {message}')

class Notificator:
    def __init__(self, notification_sender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        # Validaçâo de dados
        self.__notification_sender.send_notification(message)

obj = Notificator(EmailNotificationSender())
obj.send('Hello')

obj2 = Notificator(SMSNotificationSender())
obj2.send('Hello')

# colocar uma classe dentro de outra é uma prática chamada injeção de dependência