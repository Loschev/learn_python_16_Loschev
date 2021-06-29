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
from glob import glob
import logging
from random import choice
import ephem
import re

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings  # Настройки прокси и ключ от телеграма лежат в файле настроек, чтобы не передавать в git.

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(update, context):
    print(f'Пользователь {update.message.chat["first_name"]} {update.message.chat["last_name"]} написал /start')
    update.message.reply_text(f'Привет, {update.message.chat["first_name"]}! Вызван /start \n'
                              f'Для получения справки можете набрать /help \n'
                              f'Для получения картинки котика можете набрать /cat')


def talk_to_me(update, context):
    if re.search(r'кот|кошка|кошку|котика|кота|котейку|пушистого|пушистика|пушистый|пушистик', update.message.text.lower()):
        send_cat_picture(update, context)

    else:
        user_text = f'Спасибо за сообщение, {update.message.chat["first_name"]} {update.message.chat["last_name"]}! \n' \
                    f'Ваш ник @{update.message.chat["username"]}\n' \
                    f'Вы написали сообщение: {update.message.text}'
        print(update.message)
        update.message.reply_text(user_text)
    logging.info(f'User: {update.message.chat["username"]}, Chat id: {update.message.chat["id"]}, '
                 f'Message: {update.message.text}')


def planet(update, context):
    planet_name = update.message.text.split()[1]
    print(planet_name)

    planet_name_for_ephem = getattr(ephem, planet_name)()
    planet_name_for_ephem.compute()
    constellation_of_the_planet = ephem.constellation(planet_name_for_ephem)

    reply = f'Планета {planet_name} находится в созвездии {constellation_of_the_planet[1]}'
    update.message.reply_text(reply)


def helping(update, context):
    list_of_planets = []
    print(ephem._libastro.builtin_planets())
    for element in ephem._libastro.builtin_planets():
        if element[1] == 'Planet':
            list_of_planets.append(element[2])
    reply = f'Вы пожете узнать, в каком созвездии находится планета, ' \
            f'если наберете /planet *планета* \nНапример, /planet Venus' \
            f'\nСписок планет: {list_of_planets}'
    update.message.reply_text(reply)


def send_cat_picture(update, context):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    context.bot.send_photo(chat_id=update.message.chat["id"], photo=open(cat_pic, 'rb'))


def main():
    mybot = Updater(settings.api_key, request_kwargs=settings.PROXY, use_context=True)
    logging.info('Бот запускается')
    mybot.dispatcher.add_handler(CommandHandler('start', greet_user))
    mybot.dispatcher.add_handler(CommandHandler('planet', planet))
    mybot.dispatcher.add_handler(CommandHandler('help', helping))
    mybot.dispatcher.add_handler(CommandHandler('cat', send_cat_picture))
    mybot.dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
