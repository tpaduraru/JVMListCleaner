import csv
import re
import tkinter as tk
from jvmlist import JVMList

# general proper function def verify(file_path, field_dict, jl):
def verify(jl):
    updated_rows = [] # initialized list all

    with open(jl.input_file_path.get(), "r", newline="", encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        headers = list(reader[0].keys())
        
        if "Errors" not in headers:
            headers.append("Errors")
        
        for row in reader:
            updated_row = row.copy()
            row_be_good = True  # Assume row is valid until proven otherwise
            error_msg = ""

            for header, column in jl.field_dict.items():
                if column not in headers: continue
                if not row[column]: continue

                updated_value = ''
                value = row[column].strip()
                if header == "First Name":
                    updated_value = proper_name(value)
                elif header == "Last Name":
                    updated_value = proper_name(value)
                elif header == "Email":
                    updated_value = value if valid_email(value) else ""
                    if updated_value == "":
                        row_be_good = False
                        error_msg += 'Invalid email, '
                elif header == "Phone":
                    updated_value = valid_phone(value)
                    if bool(re.search(r'[^0-9]', updated_value)):
                        row_be_good = False
                        error_msg += 'Invalid phone, '
                elif header == "Street Address":
                    updated_value = format_street(value)
                elif header == "City":
                    updated_value = proper_name(value)
                elif header == "State":
                    if value.upper() in state_abbreviations.values():
                        updated_value = value.upper()
                    else:
                        updated_value = state_abbreviations.get(value.title(), "")
                        if updated_value == "":
                            row_be_good = False
                            error_msg += 'Invalid state, '
                elif header == "Zip Code":
                    updated_value = format_zip(value)
                elif header == "County":
                    updated_value = proper_name(value)
                else:
                    updated_value = value  # No change if the field is unrecognized

                updated_row[column] = updated_value

            updated_row["Errors"] = error_msg.strip(", ") if not row_be_good else ""
        
            updated_rows.append(updated_row)

            # Track the number of successesful and error rows
            if row_be_good:
                jl.successful_rows += 1
            else:
                jl.error_rows += 1
                print(f"Row {jl.read_rows} failed formatting: {error_msg}") # Temporary fstring printout until implementation of errors.py 
                print(f"Invalid Row: {row}")

    input_file_path_str = jl.input_file_path.get()
    output_file = input_file_path_str.replace(".csv", "_output.csv")
    with open(output_file, "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_rows)
        
    jl.row_count_str.set(jl.read_rows)
    jl.successful_rows_str.set(jl.successful_rows)
    jl.error_count_str.set(jl.error_rows)
    print(f"File saved in: {output_file}")
    print(f"Rows read: {jl.read_rows}, Successful rows: {jl.successful_rows}, Errors: {jl.error_rows}") # temp until we print out in errors.py

    jl.row_count_str.set(jl.read_rows)
    jl.successful_rows_str.set(jl.successful_rows)
    jl.error_count_str.set(jl.error_rows)
    print(f"File saved in: {output_file}")
    print(f"Rows read: {jl.read_rows}, Successful rows: {jl.successful_rows}, Errors: {jl.error_rows}") # temp until we print out in errors.py



def proper_name(name):
    out =" ".join(word.capitalize() for word in name.split()) # capitalizes each word
    out = re.sub(r"(?<!\w)(mc)(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)# capitalizes McXxxx
    out = re.sub(r"(?<!\w)(')(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)# capitalizes O'Xxxx
    return out

def valid_email(email):
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)) 

def valid_phone(phone):
    phone = re.sub("[^0-9]", "", phone) 
    return phone

def format_street(address):
    out =" ".join(word.capitalize() for word in address.split()) # capitalizes each word
    out = re.sub(r"(?<!\w)(mc)(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)# capitalizes McXxxx
    out = re.sub(r"(?<!\w)(o')(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)# capitalizes O'Xxxx
    out = re.sub(r"(?<!\w)(#)(\w)", lambda m: m.group(1).capitalize() + m.group(2).upper(), out, flags=re.IGNORECASE)# capitalizes #A33
    out = re.sub(r"(\s[ns][ew]\b)", lambda m: m.group(1).upper(), out, flags=re.IGNORECASE)# capitalizes NE,NW,SE,SW
    return out

def format_zip(zip):
    zip = re.sub(r"\D", "", zip)  
    return zip[:5]


state_abbreviations = {
    "Alabama" : "AL",
    "Alaska" : "AK",
    "Arizona" : "AZ",
    "Arkansas" : "AR",
    "American Samoa" : "AS",
    "California" : "CA",
    "Colorado" : "CO",
    "Connecticut" : "CT",
    "Delaware" : "DE",
    "District of Columbia" : "DC",
    "Florida" : "FL",
    "Georgia" : "GA",
    "Guam" : "GU",
    "Hawaii" : "HI",
    "Idaho" : "ID",
    "Illinois" : "IL",
    "Indiana" : "IN",
    "Iowa" : "IA",
    "Kansas" : "KS",
    "Kentucky" : "KY",
    "Louisiana" : "LA",
    "Maine" : "ME",
    "Maryland" : "MD",
    "Massachusetts" : "MA",
    "Michigan" : "MI",
    "Minnesota" : "MN",
    "Mississippi" : "MS",
    "Missouri" : "MO",
    "Montana" : "MT",
    "Nebraska" : "NE",
    "Nevada" : "NV",
    "New Hampshire" : "NH",
    "Kentucky" : "KY",
    "Louisiana" : "LA",
    "Maine" : "ME",
    "Maryland" : "MD",
    "Massachusetts" : "MA",
    "Michigan" : "MI",
    "Ohio" : "OH",
    "Oklahoma" : "OK",
    "Oregon" : "OR",
    "Pennsylvania" : "PA",
    "Puerto Rico" : "PR",
    "Rhode Island" : "RI",
    "South Carolina" : "SC",
    "South Dakota" : "SD",
    "Tennessee" : "TN",
    "Texas" : "TX",
    "Trust Territories" : "TT",
    "Utah" : "UT",
    "Vermont" : "VT",
    "Virginia" : "VA",
    "Virgin Islands" : "VI",
    "Washington" : "WA",
    "West Virginia" : "WV",
    "Wisconsin" : "WI",
    "Wyoming" : "WY"
}
