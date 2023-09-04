import telebot

bot = telebot.TeleBot("6666873066:AAHrhSZnUTbyPm3KkxAnhRqOelrDVVwyxFs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я эхо бот.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
