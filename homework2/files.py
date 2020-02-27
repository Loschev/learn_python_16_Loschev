with open('text.txt', 'a', encoding='utf-8') as myfile:
    myfile.write('\nworld!')

with open('text.txt', 'r', encoding='utf-8') as myfile:
    # text = myfile.read()
    # print(text)
    for line in myfile:
        line = line.replace('\n', '')
        print(line)
