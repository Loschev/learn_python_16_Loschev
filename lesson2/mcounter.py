# Как работает счетчик из библиотеки коллекшнс.
from collections import Counter

my_list = ['A', 'A', 'B', 'C']

my_counter = Counter(my_list)
print(my_counter)
