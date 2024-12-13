from _datetime import datetime

from save_all_books import save_all_books

# function to update books in JSON file declared here
def update_book(book_list):
    print('\n---------------------------')
    print('UPDATE BOOK')
    print('---------------------------\n')

    search_book = input('Enter Book Title to Update: ')
    
    for book in book_list:
        if book['title'] == search_book:
            title = input('Enter Updated Book Title: ')
            author = input('Enter Updated Author Name: ')

            while True:
                year = input('Enter Updated Publishing Year: ')

                if year and not year.isdigit():
                    print('Invalid Input. Publishing Year Must Be A Number!!\n')
                    continue

                break

            while True:
                try:
                    price = input('Enter Updated Book Price: ')

                    if price:
                        price = int(price)
                        if int(price) < 1:
                            print('Invalid Input. Price Must Greater Than Zero!!\n')
                            continue

                    break
                except ValueError:
                    print('Invalid Input. Price Must Be An Integer!!\n')


            while True:
                try:
                    quantity = input('Enter Quantity: ')

                    if quantity:
                        quantity = int(quantity)
                        if quantity < 0:
                            print('Invalid Input. Quantity Cannot Be Negative!!\n')
                            continue

                    break
                except ValueError:
                    print('Invalid Input. Price Must Be An Integer!!\n')

            # checking if similar book title already exists or not
            if title:
                for existing_book in book_list:
                    if existing_book['title'] == title:
                        print('Book With Similar Title Already Exists!!\n')
                        return

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

            return

    print('Book Not Found!!\n')