import telebot

token = '5181869878:AAEJvx_0qNkXOdVk0Og-BpNIUwCv-hAEWzY'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
  if 'Alex' in message.text:
    message.text = 'Ба! Знакомые все лица!'
  bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)