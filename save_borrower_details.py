import json

# function to save borrower details declared here
def save_borrower_details(borrower_details_list):
    try:
        with open('borrower_details.json', 'w') as borrower_details_file:
            json.dump(borrower_details_list, borrower_details_file, indent=4)

        return 1
    except Exception as e:
        print('Something Went Wrong While Saving Borrower Details!!\n')
        return 0