"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings  # Настройки прокси и ключ от телеграма лежат в файле настроек, чтобы не передавать в git.
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def greet_user(update, context):
    """
    Приветствуем нового пользователя в ответ на команду /start
    """
    text = f'Привет, {update.message.chat["first_name"]}! Вызван /start \nДля получения справки можете набрать /help'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    """
    Отвечаем на любое сообщение пользователя дублированием сообщения, а также подтягиваем
    имя пользователя, фамилию и ник.
    """
    up = update.message
    user_text = f'Спасибо за сообщение, {up.chat["first_name"]} {up.chat["last_name"]}! \n' \
                f'Ваш ник @{up.chat["username"]}\n' \
                f'Вы написали сообщение: {up.text}'
    logging.info(f'User: {up.chat["username"]}, Chat id: {up.chat["id"]}, '
                 f'Message: {up.text}')
    print(up)
    up.reply_text(user_text)


def planet(update, context):
    """
    Отвечаем на команду /planet *планета* в каком созвездии находится планета сегодня
    """
    up = update.message
    splitted = up.text.split()[1]
    print(splitted)
    planet_url = getattr(ephem, splitted)()
    planet_url.compute()
    const = ephem.constellation(planet_url)
    reply = f'Планета {splitted} находится в созвездии {const}'
    up.reply_text(reply)


def helping(update, context):
    """
    Выводим список планет в ответ на команду help. Список планет берется из библиотеки ephem
    """
    up = update.message
    list_of_planet = []
    for element in ephem._libastro.builtin_planets():
        if element[1] == 'Planet':
            list_of_planet.append(element[2])
    reply = f'Вы пожете узнать, в каком созвездии находится планета ' \
            f'если наберете /planet *планета* \nНапример, /planet Venus' \
            f'\nСписок планет: {list_of_planet}'
    up.reply_text(reply)


def main():
    mybot = Updater(settings.api_key, request_kwargs=settings.PROXY, use_context=True)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('help', helping))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
