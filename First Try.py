#We have already fucked this code for [3] hour
#When we started writing this code, only we and God understood what was written here. 

import telebot
from telebot import types

#1768045491:AAHwrAOzQU9oOQvGpK0Lb4egMmIrt4ihT7k

bot = telebot.TeleBot("1768045491:AAHwrAOzQU9oOQvGpK0Lb4egMmIrt4ihT7k")

basket = ''
name = ''
number = ''
@bot.message_handler(commands=['start'])
def send_welcome(message):  #здесь мы хотим вывести Привет
	#bot.reply_to(message, "Привет, чтобы узнать, что я умею вбей /skills")
    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот магазина...\nЧтобы узнать мой функционал вбей <b>/skills</b>".format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['skills', 'help'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Купить")
    item2 = types.KeyboardButton("О нас")
    item3 = types.KeyboardButton("Помощь")
    item4 = types.KeyboardButton("Каталог")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Что ты хочешь сделать?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
        if message.text == "Купить":
            bot.send_message(message.chat.id, "Какой товар хотите купить?")
            if bot.message_handler(message):
                def basket(message):
                    global basket
                    basket = message.text
                    bot.send_message(message.chat.id, "Как вас зовут?")
                    bot.register_next_step_handler(message, name)

            def reg_name(message):
                global name
                name = message.text
                bot.send_message(message.from_user.id, "Какой у вас номер телефона?")
                bot.register_next_step_handler(message, number)

            def reg_number(message):
                global number
                # age = message.text
                while number == 0:
                    try:
                        number = int(message.text)
                    except Exception:
                        bot.send_message(message.from_user.id, "Вводите цифрами!")




        elif message.text == 'О нас':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


bot.polling()

#Now only God remains

