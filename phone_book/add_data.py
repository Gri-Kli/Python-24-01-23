

def add_data(data):
    with open('phone_book.txt', 'a', encoding='utf-8') as f:
        f.write(' '.join(data) + '\n')
        # f.write('\n')

