import telebot
bot = telebot.TeleBot('885748551:AAFykPTT0t0yjAe4HBvKbL_Pco129q7xQ-Q')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Здарова!')
    else:
        bot.send_message(message.from_user.id, 'Я не врубаюсь, что ты говоришь')

bot.polling(none_stop=True, interval=0)