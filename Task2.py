# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input('Введите число: '))
sequence = []
sum_seq = 0

for i in range(1, number+1):
    sequence.append(round((1+1/i)**i, 2))
    sum_seq += sequence[i-1]
print(sequence)
print(f'Сумма: {sum_seq}')