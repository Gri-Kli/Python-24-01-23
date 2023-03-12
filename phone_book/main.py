from find_request import find_request
from print_all_book import print_book
from add_data import add_data
from del_data import del_data
from change_data import change_data


def perform_operation(operation_number):
    if operation_number == '1':
        print_book()
    elif operation_number == '2':
        add_data(get_data())
    elif operation_number == '3':
        print('\n'.join(find_request(input('Имя, Фамилия, Отчество, Телефон ').strip())))
    elif operation_number == '4':
        us_req_1 = input('Имя, Фамилия, Отчество, Телефон ')
        print('\n'.join(find_request(us_req_1.strip())))
        numb_str = int(input('Какую запись хотите отредактировать? \n'))
        us_req_2 = input('Изменить - 1\nУдалить - 2 \n')
        if us_req_2 == '1':
            i = 0
            new_name_list = []
            while i != 4:
                new_name_list.append(input('Вводите поочереди данные: \nИмя, Фамилия, Отчество, Телефон\n'))
                i += 1
            change_data(us_req_1, numb_str, new_name_list)
        elif us_req_2 == '2':
            del_data(us_req_1, numb_str)


def get_data():
    name = input('Имя ')
    surname = input('Фамилия ')
    patronymic = input('Отчество ')
    phone_numb = input('Телефон ')
    return (name, surname, patronymic, phone_numb)


def get_operation_numb():
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        print('ERROR, TRY AGAIN ')
        operation = input()
    return operation


print('ТЕЛЕФОННЫЙ СПРАВОЧНИК\nРаспечатать весь словарь - 1\nДобавить запись - 2\nПоиск записи - 3\nПоиск и редактирование записи - 4')

perform_operation(get_operation_numb())