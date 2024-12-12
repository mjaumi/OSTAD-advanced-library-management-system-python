import random
from datetime import datetime

from save_all_books import save_all_books


# function to add new book declared here
def add_book(book_list):
    print('\n---------------------------')
    print('ADD NEW BOOK')
    print('---------------------------\n')

    title = input('Enter Book Title: ')
    author = input('Enter Author Name: ')
    year = int(input('Enter Publishing Year: '))
    price = int(input('Enter Book Price: '))

    while True:
        try:
            quantity = int(input('Enter Quantity: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    # generating random ISBN here
    isbn = random.randint(10000, 99999)
    
    # picking book added time here
    book_added_at = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    # creating new book dictionary here
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'price': price,
        'quantity': quantity,
        'isbn': isbn,
        'book_added_at': book_added_at
    }

    book_list.append(new_book)

    save_all_books(book_list)

    print('Book Added Successfully!!\n')