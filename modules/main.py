from telebot import TeleBot
from user import User
from locale.localization import Locale
class Bot:
    def __init__(self):
        lang = 'en'
        self._supported_langs = ['ru', 'en']
        self.loc = Locale(lang).message
        self.bot = TeleBot(input())
        self.__connect()
    def __connect(self):
        self.bot.polling(none_stop=True)
    def __del__(self):
        self.bot.stop_polling()
    def send_message(self, id, message):
        self.bot.send_message(id, message)
    
    @bot.message_handler(commands=['lang'])
    def get_command(self, cmd):
        try:
            lang = cmd.text.split()[1]
        except:
            lang = ''
        if lang != '' or lang not in self._supported_langs:
            self.loc = Locale(lang).message
            self.send_message(cmd.chat.id, self.loc['setup-lang'])
        else:
            self.send_message(cmd.chat.id, self.loc['lang-error'])
    
    @bot.message_handler(content_types=['text'])
    def get_message(self, message):
        if message.text.lower() == 'привет':
            self.send_message(message.chat.id, self.loc['greeting'])
        else:
            self.send_message(message.chat.id, self.loc['unknow-mes'])