
import telebot

import Terpenie
import binbin

bot = telebot.TeleBot(token='5356466421:AAE_S4fHJkjqn7QUP29GzP31paUO3ViO90o', parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global a
    global chat_id
    chat_id = message.chat.id
    if message.from_user.id == 469828334:
        global a
        a = bot.send_message(text='Hi', chat_id=chat_id)
        Terpenie.sen(chat_id, a.id)
        binbin.ATAS().websoset()


bot.polling()

