from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
c = []
for class_ in students:
    c.append(class_['first_name'])
my_counter = Counter(c)
print(my_counter)
for key in my_counter:
    print(f'{key}: {my_counter.get(key)}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
c = []
for class_ in students:
    c.append(class_['first_name'])
my_counter = Counter(c).most_common()
print(f'Самое часто встречающееся имя среди учеников: {my_counter[0][0]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
n = 0
for students in school_students:
    c = []
    for class_ in students:
        c.append(class_['first_name'])
    my_counter = Counter(c).most_common()
    n += 1
    print(f'Самое часто встречающееся имя в {n} классе: {my_counter[0][0]}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Яна'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '3а', 'students': [{'first_name': 'Олег'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
    'Яна': False,
}
for class_ in school:
    male = []
    female = []
    for students in class_['students']:
        if is_male[students['first_name']]:
            male.append(students['first_name'])
        else:
            female.append(students['first_name'])
    print(f'В классе {class_["class"]} {len(female)} девочки и {len(male)} мальчика.')
# Надо попробовать через Counter

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс,
# в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Яна'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '3а', 'students': [{'first_name': 'Олег'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
    'Яна': False,
}

for class_ in school:
    male = []
    female = []
    for students in class_['students']:
        if is_male[students['first_name']]:
            male.append(students['first_name'])
        else:
            female.append(students['first_name'])
    if len(female) > len(male):
        counter_of_students = 'больше девочек'
    elif len(male) > len(female):
        counter_of_students = 'больше мальчиков'
    else:
        counter_of_students = 'девочек и мальчиков поровну'
    print(f'В классе {class_["class"]} {counter_of_students}.')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
