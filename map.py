# need to be able to validate the different fields like address and email
# populate the column drop downs and make sure that the email and such are valid
# verify the emails have @ and . e.g. "aaaa@aaa.a" is valid 
# create a function called "proper" that will make the first letter capitalized of every name, including in emails and addresses

import csv
#from tkinter import ttk

def map(file_path, dropdowns):
    if not file_path:
        print("No file selected for mapping.")
        return

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Populate dropdowns with headers from the CSV
    for dropdown in dropdowns:
        dropdown['values'] = headers
        dropdown.set('')
        