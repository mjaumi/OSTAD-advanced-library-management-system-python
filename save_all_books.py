import json

# function to save book list into a JSON file declared here
def save_all_books(book_list):
    try:
        with open('books.json', 'w') as books_file:
            json.dump(book_list, books_file, indent=4)

    except Exception as e:
        print('Something Went Wrong While Saving The Books!!\n')