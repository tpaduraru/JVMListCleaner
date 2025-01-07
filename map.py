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
    for dropdown in dropdown_options:
        dropdown['values'] = headers
        dropdown.set('')

    # Keywords for each dropdown field
    dropdown_keywords = {
        0: ["first", "name"],         
        1: ["last", "name"],    
        2: ["email", "e-mail"],     
        3: ["phone", "mobile"],        
        4: ["address", "street"],   
        5: ["city"],                  
        6: ["state"],                  
        7: ["zip"],                    
        8: ["county"] 
    }

    # Iterate through headers and assign best matches to dropdowns
    for idx, keywords in dropdown_keywords.items():
        for header in headers:
            h = header.lower()

            # Check for keywords
            if all(keyword in h for keyword in keywords): # for ANDed keywords
                dropdown_options[idx].set(header) 
                break
            elif any(keyword in h for keyword in keywords): # for ORed keywords
                dropdown_options[idx].set(header) 
                break


            


'''    for idx, dropdown in enumerate(dropdown_options):
        dropdown['values'] = headers
        h = headers[idx].lower() # cleans
        dropdown.set('')
        
        #try to map first name
        if ( h.find("first") and h.find("name")):
            dropdown_options[0].set(headers[idx])
        #try to map last name
        elif ( h.find("last") and h.find("name")):
            dropdown_options[1].set(headers[idx])
        #try to map email
        elif ( h.find("e-mail") or h.find("email")):
            dropdown_options[2].set(headers[idx])
        #try to map phone
        elif ( h.find("phone") or h.find("mobile")):
            dropdown_options[3].set(headers[idx])
        #try to map street
        elif ( h.find("street") or h.find("address")):
            dropdown_options[4].set(headers[idx])
       #try to map city
        elif ( h.find("city") ):
            dropdown_options[5].set(headers[idx])
        # try to map state
        elif ( h.find("state") ):
            dropdown_options[5].set(headers[idx])
        # try to map zip
        elif ( h.find("zip") ):
            dropdown_options[5].set(headers[idx])
        # try to map county
        elif ( h.find("county") ):
            dropdown_options[5].set(headers[idx])'''
        
