import telebot
TOKEN = "845739116:AAHTjdzhhe526OLCj1uycnJG6jg2H3NXxfk"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду делать полезные штуки')
@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я абсолютно бесполезный бот.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Насяльника, моя твоя нипониль :(')
bot.polling()