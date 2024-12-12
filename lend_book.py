from datetime import datetime
from datetime import timedelta
import json

from restore_borrower_details import restore_borrower_details
from save_all_books import save_all_books
from save_borrower_details import save_borrower_details


# function to lend book declared here
def lend_book(book_list):
    print('\n---------------------------')
    print('LEND BOOK')
    print('---------------------------\n')

    search_book = input('Enter Book Title to Lend: ')

    for book in book_list:
        if book['title'] == search_book:
            if book['quantity'] > 0:
                print('\nBook Found!!\n')

                borrower_details_list = restore_borrower_details()

                name = input("Enter Borrower's Name: ")
                phone = input("Enter Borrower's Phone Number: ")

                current_datetime = datetime.now()

                borrowed_at = current_datetime.strftime('%d-%m-%Y %H:%M:%S')

                # adding 7 days to borrowed date as return due date automatically here
                return_due_date = (current_datetime + timedelta(days=7)).strftime('%d-%m-%Y %H:%M:%S')

                # creating borrower details dictionary here
                borrower_details = {
                    'name': name,
                    'phone': phone,
                    'book_title': search_book,
                    'borrowed_at': borrowed_at,
                    'return_due_date': return_due_date
                }

                borrower_details_list.append(borrower_details)

                # saving borrower details here
                response = save_borrower_details(borrower_details_list)

                if response:
                    # decreasing book quantity after lending here
                    book['quantity'] -= 1
                    save_all_books(book_list)

                    print('Book Lent Successfully!!\n')

                    return book_list


            else:
                print('Insufficient Quantity!!\n')

    print('Book Not Found!!\n')