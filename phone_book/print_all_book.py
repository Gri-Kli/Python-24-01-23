def print_book():
    with open('phone_book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

