import json

def view_all_books():
    print('\n---------------------------')
    print('VIEW ALL BOOKS')
    print('---------------------------\n')

    try:
        with open('books.json', 'r') as books_file:
            books = json.load(books_file)
            book_list = books

        if len(book_list):
            for index, book in enumerate(book_list, 1):
                print(str(index) + '.')
                print(f'Title: {book['title']}')
                print(f'Author: {book['author']}')
                print(f'ISBN: {book['isbn']}')
                print(f'Publishing Year: {book['year']}')
                print(f'Price: {book['price']}')
                print(f'Quantity: {book['quantity']}')
                print(f'Added At: {book['book_added_at']}')
                print(f'Last Updated At: {book['last_updated_at'] if book['last_updated_at'] else 'N/A'}')
                print('\n')
        else:
            print('No Books Found!!')

        print('\n')

    except Exception as e:
        print('No Books Found!!\n')