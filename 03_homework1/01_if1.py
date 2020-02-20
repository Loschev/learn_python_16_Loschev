"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main(age):
    if 0 < age <= 6:
        print('Скорее всего вы ходите в детский сад.')
    elif 6 < age <= 18:
        print('Скорее всего вы школьник.')
    elif 18 < age <= 22:
        print('Скорее всего вы учитесь в ВУЗе.')
    elif 22 < age <= 65:
        print('Скорее всего вы работаете.')
    elif 65 < age <= 100:
        print('Скорее всего вы на пенсии.')
    elif 100 < age:
        print('Вы точно живы?!')


if __name__ == "__main__":
    your_age = input('Введите ваш возраст:\n')

    while not your_age.isdigit():
        your_age = input('Вы ввели не число. Введите число:\n')

    your_age = int(your_age)

    main(your_age)
