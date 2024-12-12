import json

# function to restore lender details JSON declared here
def restore_lender_details():
    try:
        with open('lender_details.json', 'r') as lender_details_file:
            lender_details_list = json.load(lender_details_file)

        return lender_details_list

    except Exception as e:
        print('Something Went Wrong While Restoring The Lender Details!!\n')
        return []