

def find_request(us_req):
    with open('phone_book.txt', 'r', encoding='utf-8') as f:
        found_list = []
        for line in f:
            if us_req in line.split():
                found_list.append(line)
    return found_list
    # print(found_list)

