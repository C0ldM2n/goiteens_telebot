import telebot
import sqlite3

bot = telebot.TeleBot('6071863213:AAEmCqtglY6HbR7_tlkluXa9ZlbcW8alHZk')
gigi = None
mints = None
sms = None
svc = None
hots = None
bud = None

@bot.message_handler(commands=['start'])  # start message
def start(message):
    conn = sqlite3.connect('user_inputs.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user_inputs (id int auto_increment primary key, gigi varchar(50), mints varchar(50), sms varchar(50), svc varchar(50), hots varchar(50), bud varchar(50))')

    conn.commit()
    cur.close()
    conn.close()
# Юзер вводит гиги а потом..
    bot.send_message(message.chat.id, 'привет мы тебя зарегаем введи gigi')
    bot.register_next_step_handler(message, user_gigi)
# А потом он ответ идет в гиги, а ему надо писать новый ответ... И так до 6 категории
def user_gigi(message):
    global gigi
    gigi = message.text.strip()
    bot.send_message(message.chat.id, 'Введите minuti')
    bot.register_next_step_handler(message, user_mints)

def user_mints(message):
    global mints
    mints = message.text.strip()
    bot.send_message(message.chat.id, 'Введите sms')
    bot.register_next_step_handler(message, user_sms)

def user_sms(message):
    global sms
    sms = message.text.strip()
    bot.send_message(message.chat.id, 'Введите service')
    bot.register_next_step_handler(message, user_svc)

def user_svc(message):
    global svc
    svc = message.text.strip()
    bot.send_message(message.chat.id, 'Введите hotspot')
    bot.register_next_step_handler(message, user_hots)

def user_hots(message):
    global hots
    hots = message.text.strip()
    bot.send_message(message.chat.id, 'Введите Budget')
    bot.register_next_step_handler(message, user_bud)

# Последний ввод сообщения
def user_bud(message):
    bud = message.text.strip()

    conn = sqlite3.connect('user_inputs.sql')
    cur = conn.cursor()
#global = импорт в других переменных в сообщение и перевод их в базу данных
    cur.execute("INSERT INTO user_inputs (gigi, mints, sms, svc, hots, bud) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (gigi, mints, sms, svc, hots, bud))
    conn.commit()
    cur.close()
    conn.close()

#Предложение посмотреть все данные из БД (чем то надо заменить)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Tarifo fil', callback_data='user_inputs'))
    bot.send_message(message.chat.id, 'Polzovatel geniy', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('user_inputs.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM user_inputs')
    user_inputs = cur.fetchall()

    info = ''
    for el in user_inputs:
        info += f'Gigs: {el[1]}, Minutes: {el[2]}, SMS: {el[3]}, Service: {el[4]}, hotspot: {el[5]}, Budget: {el[6]}\n'

    cur.close()
    conn.close()


    bot.send_message(call.message.chat.id, info)
bot.polling(none_stop=True)
