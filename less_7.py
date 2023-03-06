
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# input('Print poems :')
# def puhhh(text_poem):
#     vow_count_list = []
#     vowels = ('а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я')
#     rhythm_list = []
#     list_phrase = text_poem.split(' ')
#     for phrase in list_phrase:
#         vow_count = 0
#         for let in vowels:
#             vow_count += phrase.count(let)
#         rhythm_list.append(vow_count)
#     if rhythm_list[0] != rhythm_list[-1]:
#         return print('Пам парам')
#     print('Парам пам-пам')
# text_poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# puhhh(text_poem)

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# def print_operation_table(operation, num_row = 6, num_columns = 6):
#     list_1 = [n + 1 for n in range(num_row)]
#     list_2 = [n + 1 for n in range(num_columns)]
#     for i in range(num_row):
#         list_1 = operation
#         print(list_1)
#
#
#
# print_operation_table(lambda x, y: x * y)

from math import log10

def printOperationTable(operation, numRows=9, numColumns=9):
    if operation(1,1)==2:
        print(1,end='\t')

    colSize = int(log10(operation(numRows+1, numColumns+1)))+2

    for row in range(1, numRows+1):
        for column in range(1, numColumns+1):
            if operation(1,1)==2:
                column=column-1
            print("{:>{}}".format(operation(row,column), colSize), end='\t')
        print()