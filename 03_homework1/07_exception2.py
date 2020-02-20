"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_summ(num_one, num_two):
    if isinstance(num_one, (int, float)) and isinstance(num_two, (int, float)):
        return num_one + num_two
    elif is_number(num_one) and is_number(num_two):
        return float(num_one) + float(num_two)
    elif ValueError:
        return 'Переменная не является цифровым значением'


if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3.0, "3"))
    print(get_summ("3", 3.0))
    print(get_summ("4", "4.0"))
    print(get_summ("4", "-4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))
