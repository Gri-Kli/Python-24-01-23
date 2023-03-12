

def change_data(name, numb_str, new_name_list):
    with open('phone_book.txt', 'r', encoding='utf-8') as f:
        found_list = []
        phone_list =[]
        new_phone_list = []
        my_score = 0
        for line in f:
            phone_list.append(line)
        for x in phone_list:
            found_list.append(x.strip('/n').split())
        # print(found_list)
        for i, val in enumerate(found_list):
            # print(found_list.index(y))
            for j in val:
                if j == name:
                    my_score += 1
                    if my_score == numb_str:
                        found_list[i] = new_name_list
                        # found_list[found_list.index(y)] = new_name_list
        print(found_list)
    for z in found_list:
        new_phone_list.append(' '.join(z) + '\n')

    add_data(new_phone_list)


def add_data(data):
    with open('phone_book.txt', 'w', encoding='utf-8') as f:
        f.writelines(data)
        # f.write('\n')
