"""Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии:  a
n
 = a1
 + (n-1) * d
Каждое число вводится с новой строки."""

#
# def progression (elem, step, quant):
#     my_list = []
#     my_list.append(elem)
#     while quant != 1:
#         quant -= 1
#         elem += step
#         my_list.append(elem)
#     return my_list
#
#
# elem = int(input('First elem :'))
# step = int(input('Step :'))
# quant = int(input('Quantity :'))
# print(progression(elem, step, quant))

# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

my_list = []
min = int(input('MIN :'))
max = int(input('MAX :'))
index_list = []
index_numb = -1

for i in range(min, max + 1):
    numb = int(input('NUMBER :'))
    my_list.append(numb)
for i in my_list:
    index_numb += 1
    if min <= i <= max:
        index_list.append(index_numb)

print(my_list)
print( index_list)