# Импортируем нужные компоненты
from telegram.ext import Updater


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота

def main():
    my_first_telebot = Updater("599222255:AAHLQC2dWsQZeAIMfaA2J-hdzmMiJ1jh3pA")
    my_first_telebot.start_polling()
    my_first_telebot.idle()


# Вызываем функцию - эта строчка собственно запускает бота
main()
