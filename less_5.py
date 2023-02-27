"""Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии."""

#
# def degree_n(numb_1, numb_2):
#     if numb_2 == 1:
#         return numb_1
#     else:
#         return numb_1 * degree_n(numb_1, numb_2 - 1)
#
# numb_1 = int(input("Введите первое число :"))
# numb_2 = int(input("Введите второу число :"))
# print(degree_n(numb_1, numb_2))
#





"""Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы."""


def sum(a, b):
    if b == 0:
        return a
    else:
       return sum(a + 1, b - 1)


a = int(input("Number 1 :"))
b = int(input("Number 2 :"))

print(sum(a, b))


