from bot import Bot

class TelegramBotAPI(Bot):    
    
    def __init__(self, token: str) -> None:
        super().__init__(token)

        @self.bot.message_handler(commands=['start'])
        def __start_handler(message):
            self.start_handler(message)
        
        @self.bot.message_handler(content_types=['text'])
        def __send_message(message):
            self.send_message(message)
        
        self.infinity_polling()

    def send_message(self, message):
        chat_id = message.chat.id
        if message.text == "Hi!":
            self.bot.send_message(chat_id, "How you doing?")
    
    def start_handler(self, message):
        chat_id = message.chat.id
        self.bot.send_message(chat_id, "Hello!")

    def infinity_polling(self):
        self.bot.infinity_polling()