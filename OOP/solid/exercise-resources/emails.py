from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format_text(self):
        pass


class MyContent(IContent):
    def format_text(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class Sender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def format_sender(self):
        pass


class ISender(Sender):
    def format_sender(self):
        return ''.join(["I'm ", self.sender])


class Receiver(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def format_receiver(self):
        pass


class IReceiver(Receiver):
    def format_receiver(self):
        return ''.join(["I'm ", self.receiver])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format_text()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
