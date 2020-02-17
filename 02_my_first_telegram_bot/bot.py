# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='Time: %(asctime)s - Name: %(name)s - Level: %(levelname)s - Message: %(message)s',
                    level=logging.INFO,
                    filename='bot.log',
                    )


def greet_user(update, context):
    text = f'Привет, {update.message.chat["first_name"]}! Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    up = update.message
    user_text = f'Спасибо за сообщение, {up.chat["first_name"]} {up.chat["last_name"]}! ' \
                f'Вы написали сообщение: {up.text}'
    logging.info(f'User: {up.chat["username"]}, Chat id: {up.chat["id"]}, '
                 f'Message: {up.text}')
    print(up)
    up.reply_text(user_text)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater('', request_kwargs=PROXY, use_context=True)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


# Вызываем функцию - эта строчка собственно запускает бота
main()
