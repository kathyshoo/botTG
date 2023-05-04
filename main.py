import telebot
import functions
from telebot import types


token = "5591651962:AAGxXHAhVw3q5iG-Kq_JCZpxTr6aThLwQL8"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def welc(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('/weather')
    but2 = types.KeyboardButton('/money')
    but3 = types.KeyboardButton('/help')
    keyboard.add(but1, but2, but3)
    bot.send_message(message.chat.id, "Привет:) Я Нася, а ещё я ботик) Ну... как вы - люди, меня зовёте🤔 Но ничего) Я не обижаюсь. Могу я как-то тебе помочь?)\n"
                                      "Пока, что я умею только:\n"
                                      "• Определять погоду в заданном городе (чтобы задать город введи /weather *нужный город*)\n"
                                      "• Узнавать все курсы валют с сайта ЦБ) экономист😎 /money или /money USD чтобы узнать курс определённой валюты к рублю\n"
                                      "Если тебе сложно с командами, то снизу я добавила тебе кнопочки) Надеюсь разберёшься. Удачи!!",reply_markup=keyboard)

@bot.message_handler(commands=['weather'])
def weather(message):
    mas = message.text.split(' ')
    if len(mas) == 1:
        bot.send_message(message.chat.id, functions.weather())
    elif len(mas) == 2:
        bot.send_message(message.chat.id, functions.weather(mas[1]))
    else:
        bot.send_message(message.chat.id, 'Неправильно введён запрос')

@bot.message_handler(commands=['money'])
def curss(message):
    queue = message.text.split(' ')
    vivod = ''
    if len(queue) == 1:
        vivod = functions.curs()
    elif len(queue) == 2:
        vivod = functions.cursCurMon(queue[1])
    else:
        vivod = 'Неправильно введён запрос'
    bot.send_message(message.chat.id,vivod)

@bot.message_handler(content_types=['text'])
def butt(message):
    if message.text == 'Погода':
        weather(message)
    elif message.text == 'Вывести курсы с сайта ЦБ':
        curss(message)
    elif message.text == 'Помощь':
        welc(message)
    else:
        bot.send_message(message.chat.id, 'Я пока не умею работать с другими командами:(')

bot.infinity_polling()