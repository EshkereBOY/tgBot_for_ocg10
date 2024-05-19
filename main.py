import telebot
from telebot import types
from random import randint




# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Информация")
    item2 = types.KeyboardButton("Стоп")
    item3 = types.KeyboardButton("Гифка")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=markup)
    bot.reply_to(message, "Привет!")

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Информация":
        bot.send_message(message.chat.id, "Данный бот сделан студентами группы Б9123-01.03.02ии: \n 😎 Мишиным Андреем и Мутиным Артуром 😎")
    elif message.text == "Стоп":
        bot.send_message(message.chat.id, "До встречи!")
        bot.stop_bot()
    elif message.text == "Гифка":
        # Отправляем гифку
        with open(f'gifs/{randint(1, 4)}.gif', 'rb') as gif:
            bot.send_animation(message.chat.id, gif)
    else:
        bot.send_message(message.chat.id, "Извините, я не понимаю вашего сообщения.")


# Запускаем бота
if __name__ == '__main__':

    bot = telebot.TeleBot('7082771455:AAEB0IBowxpXnvf6yFSpA5wCmaoCsA_WhtU')
    bot.polling()