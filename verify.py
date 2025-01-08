import csv
import re
from jvmlist import JVMList

# do verify with the fact that it will change all of the formatting for the the rows in the selected column for the hard coded format that is for each one
# need to be able to validate the different fields like address and email
# populate the column drop downs and make sure that the email and such are valid
# verify the emails have @ and . e.g. "aaaa@aaa.a" is valid 
# create a function called "proper" that will make the first letter capitalized of every name, including in emails and addresses

# global variables to be accessed in errors.py

# general proper function def verify(file_path, field_dict, jl):
def verify(jl):
    updated_rows = [] # initialized list all


    with open(jl.input_file_path, "r", newline="", encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        headers = reader[0].keys()
        
        for row in reader:
            jl.read_rows += 1  # Increment rows read counter
            updated_row = row.copy()
            jl.successful_rows = True  # Assume row is valid until proven otherwise

            for field, column in jl.field_dict.items():
                if column not in headers:
                    continue

                value = row[column].strip()
                if field == "First Name":
                    updated_value = proper_name(value)
                elif field == "Last Name":
                    updated_value = proper_name(value)
                elif field == "Email":
                    updated_value = value if valid_email(value) else "INVALID"
                    if updated_value == "INVALID":
                        jl.successful_rows = False
                elif field == "Phone":
                    updated_value = valid_phone(value) or "INVALID"
                    if updated_value == "INVALID":
                        jl.successful_rows = False
                elif field == "Street Address":
                    updated_value = proper_case(value)
                elif field == "City":
                    updated_value = proper_case(value)
                elif field == "State":
                    updated_value = state_abbreviations.get(value.title(), "INVALID")
                    if updated_value == "INVALID":
                        jl.successful_rows = False
                elif field == "Zip Code":
                    updated_value = format_zip(value)
                elif field == "County":
                    updated_value = proper_case(value)
                else:
                    updated_value = value  # No change if the field is unrecognized

            updated_rows.append(updated_row)

        # Track the number of successesful and error rows
        if jl.successful_rows:
            pass
        else:
            jl.error_rows += 1
            print(f"Row {jl.read_rows} failed formatting: {row}") # Temporary fstring printout until implementation of errors.py 

    # Write back updated rows to the file or a new file
    output_file = jl.input_file_path.replace(".csv", "_updated.csv")
    with open(output_file, "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f"File saved in: {output_file}")
    print(f"Rows read: {jl.read_rows}, Successful rows: {jl.read_rows - jl.error_rows}, Errors: {jl.error_rows}") # temp until we print out in errors.py


def proper_case(text):
    return " ".join(word.capitalize() for word in text.split())

def proper_name(name):
    name = name.strip()
    name = re.sub(r"(?<!\w)(mc)(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), name, flags=re.IGNORECASE)
    name = re.sub(r"(?<!\w)(o')(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), name, flags=re.IGNORECASE)
    return "-".join(proper_case(part) for part in name.split("-"))

def valid_email(email):
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))

def valid_phone(phone):
    phone = re.sub(r"\D", "", phone)  # Strip of everything but numbers
    return phone if len(phone) in [10, 11] else None

def format_zip(zip):
    return zip.split("-")[0] if "-" in zip else zip[:5]  


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
