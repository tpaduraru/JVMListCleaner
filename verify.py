import csv
import re
import tkinter as tk
from jvmlist import JVMList

def verify(jl):
    updated_rows = []

    with open(jl.input_file_path.get(), "r", newline="", encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        headers = list(reader[0].keys())

        required_columns = ["Listing Price", "Loan Amount", "Credit Amount", "Errors"]
        for col in required_columns:
            if col not in headers:
                headers.append(col)

        header_order = ["Email", "Phone", "Street Address", "City", "State", "Zip Code", "County",
                        "Listing Price", "Loan Amount", "Credit Amount", "First Name", "Last Name", "Errors"]

        updated_headers = {
            "Email": "Email",
            "Phone": "Phone",
            "Street Address": "Marketing Address Street",
            "City": "Marketing Address City",
            "State": "Marketing Address State",
            "Zip Code": "Marketing Address Zip",
            "County": "Marketing Address County",
            "Listing Price": "Listing Price",
            "Loan Amount": "Loan Amount",
            "Credit Amount": "Credit Amount",
            "First Name": "FirstName",
            "Last Name": "LastName",
            "Errors": "Errors"
        }

        for row in reader:
            updated_row = {updated_headers.get(col, col): row.get(col, "").strip() for col in header_order}
            row_be_good = True  
            error_msg = "" 

            for header, column in jl.field_dict.items():
                if column not in headers:
                    continue
                if not row[column]:
                    continue

                value = row[column].strip()
                updated_value = value  
                error = None

                if header == "First Name":
                    updated_value, error = proper_name(value, 'firstname')
                elif header == "Last Name":
                    updated_value, error = proper_name(value, 'lastname')
                elif header == "Email":
                    updated_value, error = valid_email(value)
                elif header == "Phone":
                    updated_value, error = valid_phone(value)
                elif header == "Street Address":
                    updated_value = format_street(value)
                elif header == "City":
                    updated_value, error = proper_name(value, 'city')
                elif header == "State":
                    updated_value, error = format_state(value)
                elif header == "Zip Code":
                    updated_value = format_zip(value)
                elif header == "County":
                    updated_value, error = proper_name(value, 'county')

                if error:
                    error_msg += error + ', '
                    row_be_good = False

                updated_row[updated_headers[header]] = updated_value

            updated_row["Errors"] = error_msg.strip(", ") if not row_be_good else ""
            updated_rows.append(updated_row)

            if row_be_good:
                jl.successful_rows += 1
                print(f"Row {jl.successful_rows + jl.error_rows} read successfully")
            else:
                jl.error_rows += 1
                print(f"Row {jl.successful_rows + jl.error_rows} failed formatting: {error_msg}")
                print(f"Invalid Row: {row}")

    final_rows = [{updated_headers[col]: row.get(updated_headers[col], "") for col in header_order} for row in updated_rows]

    output_file = jl.input_file_path.get().replace(".csv", "_output.csv")
    with open(output_file, "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[updated_headers[col] for col in header_order])
        writer.writeheader()
        writer.writerows(final_rows)

    jl.row_count_str.set(jl.read_rows)
    jl.successful_rows_str.set(jl.successful_rows)
    jl.error_count_str.set(jl.error_rows)

    print(f"File saved in: {output_file}")
    print(f"Rows read: {jl.read_rows}, Successful rows: {jl.successful_rows}, Errors: {jl.error_rows}")

def proper_name(name, type):
    error = ''
    out = " ".join(word.capitalize() for word in name.split())  
    out = re.sub(r"(?<!\w)(mc)(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)
    out = re.sub(r"(?<!\w)(o')(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)
    out = re.sub(r"-(\w)", lambda m: '-' + m.group(1).capitalize(), out, flags=re.IGNORECASE)

    if re.search(r"[\(\)]", out): 
        error += 'Removed (' + re.findall(r"\((.*?)\)", out)[0] + ') from ' + type 
        out = re.sub(r"\(.*?\)", "", out) 

    if type in {'firstname', 'lastname'}:
        for word in name.lower().split():
            if word in {'the', 'team', 'group', 'true'}:
                error += 'Invalid '+ type
                break
    if type == 'firstname' and len(re.sub(r"[^a-zA-Z]", "", name)) <= 2:
        error += 'Verify ' + type
    if type == 'lastname':
        out = re.sub(r"\s(iii|ii|iv|jr|sr)", '', out, flags=re.IGNORECASE)  
        out = re.sub(r"[,\.]", '', out)

    return out, error

def valid_email(email):
    error = ''
    if not email:
        error += 'Missing email'
    elif ';' in email or not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        error += 'Invalid email'
    return email, error

def valid_phone(phone):
    error = None
    phone = re.sub("[^0-9]", "", phone) 
    if len(phone) < 10 or len(phone) > 11:
        error = 'Invalid phone'
    return phone, error

def format_street(address):
    out = " ".join(word.capitalize() for word in address.split()) 
    out = re.sub(r"(?<!\w)(mc)(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)
    out = re.sub(r"(?<!\w)(o')(\w)", lambda m: m.group(1).capitalize() + m.group(2).capitalize(), out, flags=re.IGNORECASE)
    return out

def format_state(state):
    error = None
    if state.upper() in state_abbreviations.values():
        return state.upper(), error
    updated_value = state_abbreviations.get(state.title(), "")
    if not updated_value:
        error = 'Invalid state'
    return updated_value, error

def format_zip(zip):
    return re.sub(r"\D", "", zip)[:5]

state_abbreviations = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "American Samoa": "AS",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District Of Columbia": "DC",
    "Florida": "FL",
    "Georgia": "GA",
    "Guam": "GU",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Puerto Rico": "PR",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Trust Territories": "TT",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Virgin Islands": "VI",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}