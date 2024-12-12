import random
from datetime import datetime

from save_all_books import save_all_books


# function to add new book declared here
def add_book(book_list):
    print('\n---------------------------')
    print('ADD NEW BOOK')
    print('---------------------------\n')


    while True:
        title = input('Enter Book Title: ')

        if not title:
            print('Invalid Input. Title Cannot Be Empty!!\n')
            continue

        break


    while True:
        author = input('Enter Author Name: ')

        if not author:
            print('Invalid Input. Author Cannot Be Empty!!\n')
            continue

        break


    while True:
        year = input('Enter Publishing Year: ')

        if not year.isdigit():
            print('Invalid Input. Publishing Year Must Be A Number!!\n')
            continue

        break


    while True:
        try:
            price = int(input('Enter Book Price: '))

            if price < 1:
                print('Invalid Input. Price Must Greater Than Zero!!\n')
                continue

            break
        except ValueError:
            print('Invalid Input. Price Must Be An Integer!!\n')


    while True:
        try:
            quantity = int(input('Enter Quantity: '))

            if quantity < 0:
                print('Invalid Input. Quantity Cannot Be Negative!!\n')
                continue

            break
        except ValueError:
            print('Invalid Input. Quantity Must Be An Integer!!\n')

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
        'book_added_at': book_added_at,
        'last_updated_at': ''
    }

    book_list.append(new_book)

    save_all_books(book_list)

    print('Book Added Successfully!!\n')