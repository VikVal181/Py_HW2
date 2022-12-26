# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для
# и получения случайного int
from random import randint

number = int(input('Введите количество элементов: '))
sequence = []
mix_param = 20

for i in range(number):
    sequence.append(randint(0, 100))
print(sequence)

for i in range(mix_param):
    index_1 = randint(0, number-1)
    index_2 = randint(0, number-1)
    temp_var = sequence[index_1]
    sequence[index_1] = sequence[index_2]
    sequence[index_2] = temp_var

print(sequence)