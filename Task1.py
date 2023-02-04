# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from functools import reduce

number = (input('Введите число: '))
#sum = 0

print(reduce(lambda x, y: int(x) + int(y), list(filter(lambda x: x.isnumeric(), list(number)))))

# for i in range(len(number)):
#     if number[i].isnumeric():
#         number_int = int(number[i])
#         sum = sum + number_int
print(sum)