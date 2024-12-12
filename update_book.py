from _datetime import datetime

from save_all_books import save_all_books


def update_book(book_list):
    print('\n---------------------------')
    print('UPDATE BOOK')
    print('---------------------------\n')

    search_book = input('Enter Book Title to Update: ')
    
    for book in book_list:
        if book['title'] == search_book:
            title = input('Enter Book Title: ')
            author = input('Enter Author Name: ')
            year = int(input('Enter Publishing Year: '))
            price = int(input('Enter Book Price: '))
            quantity = int(input('Enter Quantity: '))

            # capturing updated time from datetime here
            book_last_updated_at = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            book['title'] = title or book['title']
            book['author'] = author or book['author']
            book['year'] = year or book['year']
            book['price'] = price or book['price']
            book['quantity'] = quantity or book['quantity']
            book['last_updated_at'] = book_last_updated_at

            save_all_books(book_list)

            print('Book Updated Successfully!!\n')

            return book_list

    print('Book Not Found!!\n')