"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
dict_of_questions = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'Вопрос': 'Ответ'
}


def ask_user_dict():
    while True:
        try:
            question = input('Введите ваш вопрос:\n')
            for key in dict_of_questions:
                if question == key:
                    print(dict_of_questions[key])
        except KeyboardInterrupt:  # Если запускать с консоли, то ко Ctrl+C выходит. Но если с IDE - не реагирует
            print('Вы выходите из программы')
            break


if __name__ == "__main__":
    ask_user_dict()
