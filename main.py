from add_book import add_book

book_list = []

while True:
    print('Welcome To Library Management System!!')
    print('0. Exit')
    print('1. Add A Book')
    print('2. Update A Book')
    print('3. Delete A Book')
    print('4. View All Books')

    option = input('\nChoose An Option: ')

    if option == '0':
        print('\n----------------------------------------')
        print('EXITING LIBRARY MANAGEMENT SYSTEM')
        print('----------------------------------------\n')

        print('Thank You For Using Library Management System!!\n')
        break

    elif option == '1':
        add_book(book_list)

    else:
        print('Please, Select A Valid Option!!\n')