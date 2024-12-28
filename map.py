# need to be able to validate the different fields like address and email
# populate the column drop downs and make sure that the email and such are valid
# verify the emails have @ and . e.g. "aaaa@aaa.a" is valid 
# create a function called "proper" that will make the first letter capitalized of every name, including in emails and addresses

import csv
#from tkinter import ttk

def map(file_path, dropdown_options):
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

    # Populate dropdown_options with headers from the CSV
    for idx, dropdown in dropdown_options:
        dropdown['values'] = headers
        h = headers[idx].lower() # cleans
        dropdown.set('')
        
        #try to map first name
        if ( h.contains("first") and h.contains("name")):
            dropdown_options[0].set(headers[idx])
        #try to map last name
        elif ( h.contains("last") and h.contains("name")):
            dropdown_options[1].set(headers[idx])
        #try to map email
        elif ( h.contains("e-mail") or h.contains("email")):
            dropdown_options[2].set(headers[idx])
        #try to map phone
        elif ( h.contains("phone") or h.contains("mobile")):
            dropdown_options[3].set(headers[idx])
        #try to map street
        elif ( h.contains("street") or h.contains("address")):
            dropdown_options[4].set(headers[idx])
       #try to map city
        elif ( h.contains("city") ):
            dropdown_options[5].set(headers[idx])
        
