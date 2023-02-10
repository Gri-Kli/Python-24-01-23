"""Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X"""

# from random import randint
#
#
# elements = int(input("Write quantity elements: "))
# number_x = int(input("Number X: "))
# my_list = []
# for i in range(elements):
#     my_list.append(randint(1, elements))
#
# print(my_list)
# idx = 0
# for i in my_list:
#     if i == number_x:
#         idx += 1
#
# print(f'Число {number_x} встречается в списке {idx} раз.')

"""Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X"""


# from random import randint
#
#
# elements = int(input("Write quantity elements: "))
# number_x = int(input("Number X: "))
# my_list = []
# number = None
# number_2 = None
# for i in range(elements):
#     my_list.append(randint(1, elements))
#
# print(my_list)
# my_list.append(number_x)
# print(my_list)
# my_list.sort()
# print(my_list)
# print(len(my_list))
# idx = my_list.index(number_x)
# print(idx)
# if idx == 0:
#     number = 1
#     number_2 = None
# elif idx == len(my_list) - 1:
#     number = idx - 1
#     number_2 = None
# else:
#     number = my_list[idx - 1]
#     number_2 = my_list[idx + 1]
#
# print(f'Самый близкий по величине элемент {number} и {number_2}')

"""В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы."""

my_dict = {1: {'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'},
          2: {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'},
          3: {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'},
          4: {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'},
          5: {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'},
          8: {'J', 'X', 'Ш', 'Э', 'Ю'},
          10: {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}}

word = None
leter_dict = None
my_scores = 0
data_dict = my_dict.items()
for key, value in data_dict:
    print(key, value)

while True:
    word = input("Напишите слово русскими или английскими буквами. Для окончания игры нажмите '0' :")
    word = word.upper()
    if word == "0":
        break
    for letter in word:
        for key, value in data_dict:
            for letter_dict in value:
                if letter == letter_dict:
                    my_scores += key
    print(my_scores)
    my_scores = 0

