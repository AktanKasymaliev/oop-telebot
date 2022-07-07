from abc import abstractmethod

from telebot import TeleBot

class Bot:

    def __init__(self, token: str) -> None:
        self.bot = self.create_bot(token)

    @abstractmethod
    def start_handler(self, message):
        pass

    @abstractmethod
    def send_message(self, message):
        pass
    
    @abstractmethod
    def create_bot(self, token: str):
        return TeleBot(token, parse_mode='html')

    @abstractmethod
    def infinity_polling(self):
        pass