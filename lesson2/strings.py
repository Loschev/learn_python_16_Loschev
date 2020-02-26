# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
list_of_alphabet = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
print('Количество гласных букв в слове Архангельск:', word.lower().count(list_of_alphabet[0]))  # Пока разбираюсь.
# word.lower().count('а') + word.lower().count('е')
# Можно составит список и для каждого элемента списка применить ловер каунт. Пока разбираюсь.

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sent_split = sentence.split()
for i in sent_split:
    print(i[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sent_split = sentence.split()
m = []
for i in sent_split:
    m.append(len(i))
print(sum(m) / len(m))
