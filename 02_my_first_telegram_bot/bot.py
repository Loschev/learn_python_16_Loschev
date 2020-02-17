# Импортируем нужные компоненты
from telegram.ext import Updater


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота

def main():
    my_first_telebot = Updater("API_Key")
    my_first_telebot.start_polling()
    my_first_telebot.idle()


# Вызываем функцию - эта строчка собственно запускает бота
main()
