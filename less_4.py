"""Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств."""


# from random import randint
#
#
# elements_1 = int(input("Write quantity elements 1: "))
# elements_2 = int(input("Write quantity elements 2: "))
# my_list_1 = []
# my_list_2 = []
#
# """Этот кусок кода по условию написал, при отладки пользовался randint"""
# # while elements_1 > 0:
# #     number = int(input("Введите число для первого списка :"))
# #     my_list_1.append(number)
# #     elements_1 -= 1
# #
# # while elements_2 > 0:
# #     number = int(input("Введите число для второго списка :"))
# #     my_list_2.append(number)
# #     elements_2 -= 1
#
#
# for i in range(elements_1):
#     my_list_1.append(randint(1, elements_1))
# print(my_list_1)
#
# for i in range(elements_2):
#     my_list_2.append(randint(1, elements_2))
# print(my_list_2)
#
# my_set_1 = set(my_list_1)
# print(my_set_1)
# my_set_2 = set(my_list_2)
# print(my_set_2)
# my_list = list(my_set_1 & my_set_2)
# my_list.sort()
#
# print(my_list)

"""В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки."""
from random import randint

elements = int(input("Напишите общее количество кустов : "))
my_list = []
for i in range(elements):
    my_list.append(randint(1, elements))
print(my_list)
max_berry = 0
total_max_berry = 0
index_bush = 0
for i in my_list:
    if index_bush + 1 != elements:
       max_berry = i + my_list[index_bush - 1] + my_list[index_bush + 1]
       # print(max_berry)
       if max_berry > total_max_berry:
           total_max_berry = max_berry
    else:
        max_berry = i + my_list[index_bush - 1] + my_list[0]
        # print(max_berry)
        if max_berry > total_max_berry:
            total_max_berry = max_berry
    index_bush += 1
print(f'Максимальное количество ягод за один подход : {total_max_berry}')