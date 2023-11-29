import telebot
bot = telebot.TeleBot('6499232570:AAGQuKnk8ZItUch7hHHAa9e-tD67FrAAmDs')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['go'])
def main(message):
    bot.send_message(message.chat.id, '_Поехали!_', parse_mode='Markdown')

@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, '*Программируй [здесь](https://pastebin.com/)', parse_mode='Markdown')

bot.infinity_polling()