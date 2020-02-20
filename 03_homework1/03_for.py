"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
list_for_school = [{'school_class': '4a', 'scores': [3, 4, 5, 5, 4]},
                   {'school_class': '4б', 'scores': [5, 5, 5, 5, 5]},
                   {'school_class': '4а', 'scores': [4, 4, 4, 4, 4]},
                   {'school_class': '4г', 'scores': [2, 2, 3, 4, 4]}]
all_summary = []


def main(list_from_school):
    for element in list_from_school:
        print(f'Для класса {element["school_class"]}:')
        print(f"Оценки в списке: {element['scores']}")
        print(f"Средняя оценка класса {sum(element['scores']) / len(element['scores'])}\n")
        for numbers in element['scores']:
            all_summary.append(numbers)
    print(f'Средняя оценка по школе: {sum(all_summary) / len(all_summary)}')


if __name__ == "__main__":
    main(list_for_school)
