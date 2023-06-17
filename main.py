import telebot
from telebot import types

bot = telebot.TeleBot('6052072835:AAGW8CGANoe2lexM0mm_R5kRCGvXel8xZiM')  # use token from config for token


@bot.message_handler(commands=['start'])  # start message
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Пройти опрос')
    btn2 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, вітаю 👋. З чим можу допомогти?')
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMLZIz0ROIeKV5cHYSaiDWUdIdpFOcAAjgLAAJO5JlLMrFH0tlPjNAvBA", reply_markup=markup)
    #bot.register_next_step_handler(message, on_click)

#def on_click(message):
 #   if message.text == 'Перейти на сайт':
  #      bot.

#@bot.callback_query_handlers(func=lambda callback: True)
#def callback_message(callback):
 #   if callback.data == 'delete':
  #      bot.delete_message()


bot.polling(none_stop=True)  # nonstop working
