from save_all_books import save_all_books

# function to delete book from JSON file declared here
def delete_book(book_list):
    print('\n---------------------------')
    print('DELETE BOOK')
    print('---------------------------\n')

    search_book = input('Enter Book Title to Delete: ')

    for book in book_list:
        if book['title'] == search_book:
            book_list.remove(book)

            save_all_books(book_list)

            print('Book Deleted Successfully!!\n')
            return

    print('Book Not Found!!\n')