import json

# function to restore all books from JSON file declared here
def restore_all_books():
    try:
        with open('books.json', 'r') as books_file:
            books = json.load(books_file)
            book_list = books

        return book_list
    except Exception as e:
        print('Something Went Wrong While Restoring The Books!!\n')