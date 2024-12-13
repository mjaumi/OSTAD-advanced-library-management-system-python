from restore_borrower_details import restore_borrower_details
from save_all_books import save_all_books
from save_borrower_details import save_borrower_details

# function to implement return book feature declared here
def return_book(book_list):
    print('\n---------------------------')
    print('RETURN BOOK')
    print('---------------------------\n')

    name = input("Enter Borrower's Name: ")
    title = input('Enter Book Title the Borrower Returning: ')

    borrower_details_list = restore_borrower_details()

    for borrower in borrower_details_list:
        if borrower['name'] == name and borrower['book_title'] == title:

            for book in book_list:
                if book['title'] == title:

                    # removing & saving borrower details here
                    borrower_details_list.remove(borrower)
                    response = save_borrower_details(borrower_details_list)

                    if response:
                        # increasing book quantity after returning here
                        book['quantity'] += 1
                        save_all_books(book_list)

                        print('Book Returned Successfully!!\n')

                        return book_list

    print('Borrower Not Found!!\n')