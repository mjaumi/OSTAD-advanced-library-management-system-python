from datetime import datetime
from datetime import timedelta
import json

from save_all_books import save_all_books


def lend_book(book_list):
    print('\n---------------------------')
    print('LEND BOOK')
    print('---------------------------\n')

    search_book = input('Enter Book Title to Lend: ')

    for book in book_list:
        if book['title'] == search_book:
            if book['quantity'] > 0:
                print('\nBook Found!!\n')

                name = input("Enter Borrower's Name: ")
                phone = input("Enter Borrower's Phone Number: ")

                current_datetime = datetime.now()

                borrowed_at = current_datetime.strftime('%d-%m-%Y %H:%M:%S')

                # adding 7 days to borrowed date as return due date automatically here
                return_due_date = (current_datetime + timedelta(days=7)).strftime('%d-%m-%Y %H:%M:%S')

                # creating lender details dictionary here
                lender_details = {
                    'name': name,
                    'phone': phone,
                    'book_title': search_book,
                    'borrowed_at': borrowed_at,
                    'return_due_date': return_due_date
                }

                try:
                    with open('lender_details.json', 'w') as lender_details_file:
                        json.dump(lender_details, lender_details_file, indent=4)

                    # decreasing book quantity after lending here
                    book['quantity'] -= 1
                    save_all_books(book_list)

                    print('Book Lent Successfully!!\n')

                    return book_list
                except Exception as e:
                    print('Something Went Wrong While Lending Books!!\n')

            else:
                print('Insufficient Quantity!!\n')

    print('Book Not Found!!\n')