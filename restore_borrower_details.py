import json

# function to restore borrower details JSON declared here
def restore_borrower_details():
    try:
        with open('borrower_details.json', 'r') as borrower_details_file:
            borrower_details_list = json.load(borrower_details_file)

        return borrower_details_list

    except Exception as e:
        return []