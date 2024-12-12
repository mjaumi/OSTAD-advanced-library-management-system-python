from add_book import add_book
from delete_book import delete_book
from lend_book import lend_book
from restore_all_books import restore_all_books
from return_book import return_book
from update_book import update_book
from view_all_books import view_all_books

book_list = []

while True:
    print('Welcome To Library Management System!!')
    print('0. Exit')
    print('1. Add A Book')
    print('2. Update A Book')
    print('3. Delete A Book')
    print('4. View All Books')
    print('5. Lend A Book')
    print('6. Return Book')

    # restoring all the books while application starts here
    book_list = restore_all_books()

    option = input('\nChoose An Option: ')

    if option == '0':
        print('\n----------------------------------------')
        print('EXITING LIBRARY MANAGEMENT SYSTEM')
        print('----------------------------------------\n')

        print('Thank You For Using Library Management System!!\n')
        break

    elif option == '1':
        add_book(book_list)

    elif option == '2':
        update_book(book_list)

    elif option == '3':
        delete_book(book_list)

    elif option == '4':
        view_all_books()

    elif option == '5':
        lend_book(book_list)

    elif option == '6':
        return_book(book_list)

    else:
        print('Please, Select A Valid Option!!\n')