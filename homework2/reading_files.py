with open('referat.txt', 'r', encoding='utf-8') as myfile:
    text = myfile.read()
    print(f'Длина строки {len(text)}')
    print(f'Количество слов {len(text.split())}')
    for line in text.split('\n'):
        line = line.replace('\n', '')
        print(line)
        line = line.replace('.', '!')
        with open('referat2.txt', 'a', encoding='utf-8') as my_second_file:
            my_second_file.write(line + '\n')
