import telebot

bot = telebot.TeleBot(token='5356466421:AAE_S4fHJkjqn7QUP29GzP31paUO3ViO90o', parse_mode=None)

def sen(ch_id, msg_id):
    global chat_id
    global message_id
    chat_id = ch_id
    message_id = msg_id

def send_data(txt):
    bot.edit_message_text(text=txt, chat_id=chat_id, message_id=message_id)