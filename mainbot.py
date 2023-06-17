import telebot
from telebot import types

bot = telebot.TeleBot('6052072835:AAGW8CGANoe2lexM0mm_R5kRCGvXel8xZiM')


@bot.message_handler(commands=['start'])  # start message
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('💯 Підібрати тариф')
    btn2 = types.KeyboardButton('💻 Перейти на сайт')

    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, f'{message.from_user.first_name}, вітаю 👋. З чим можу допомогти?')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMLZIz0ROIeKV5cHYSaiDWUdIdpFOcAAjgLAAJO5JlLMrFH0tlPjNAvBA'
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])  # LINK BUTTON
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '💻 Перейти на сайт':
            markup = types.InlineKeyboardMarkup()
            linkbutton = types.InlineKeyboardButton('🌐 Перейти на сайт', url='https://www.lifecell.ua/uk/mobilnij'
                                                                             '-zvyazok/taryfy/')
            markup.add(linkbutton)
            bot.send_message(message.chat.id, 'Натисніть нижче ⬇', reply_markup=markup)

        elif message.text == '💯 Підібрати тариф':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            startt = types.KeyboardButton('🚀 Розпочати')
            back = types.KeyboardButton('🔙 Головне меню')
            markup.add(startt, back)

            bot.send_message(message.chat.id, '💯 Підібрати тариф\n\nПісля проходження цього опитування, я запропоную '
                                              'вам декілька тарифів які мають підійти вам.\n\nВи готові почати?',
                             reply_markup=markup)

        elif message.text == '🔙 Головне меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('💯 Підібрати тариф')
            btn2 = types.KeyboardButton('💻 Перейти на сайт')
            markup.add(btn1, btn2)

            bot.send_message(message.chat.id, '🔙 Головне меню', reply_markup=markup)

        # survey

        elif message.text == '🚀 Розпочати':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('💯 Підібрати тариф')
            btn2 = types.KeyboardButton('💻 Перейти на сайт')
            back = types.KeyboardButton('🔙 Головне меню')
            markup.add(btn1, btn2, back)

            bot.send_message(message.chat.id, '🚀 Початок підбору', reply_markup=markup)
            bot.send_message(message.chat.id, 'Тут должен быть первый вопрос', )


bot.polling(none_stop=True)  # nonstop working
