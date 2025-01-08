import tkinter as tk
from tkinter import filedialog
import os
from tkinter import ttk
from errors import Error_Window
from map import map
from verify import verify
from jvmlist import JVMList


jl = JVMList()


def select_files():
    file_names = filedialog.askopenfilenames(filetypes=[("CSV Files", "*.csv")])
    if file_names:
        # Use the first file from the selection
        # TO DO error when more than 1 selected
        jl.input_file_path.set(file_names[0])
        jl.input_file_path = file_names[0]
        file_name_short = ", ".join([os.path.basename(file) for file in file_names])
        file_label_var.set(file_name_short)
    else:
        jl.input_file_path.set("") 
        file_label_var.set("No files selected")

def check_status():
    if check_var.get() == 1:
        print("Checkbox is checked")
    else:
        print("Checkbox is not checked")

def update_field_dict(event):
    for idx, dropdown in enumerate(jl.dropdown_options):
        header = dropdown.get()
        if header: 
            jl.field_dict[jl.fields[idx]] = header


# Initialize root window
root = tk.Tk()
root.geometry("1200x700")
root.title("JVM List Cleaner")



# Title
title = tk.Label(root, text="List Cleaner", font=('Arial', 18))
title.pack(anchor="w", padx=20, pady=10)



# File Uploads Section
file_title = tk.Label(root, text="File Select", font=('Arial', 14))
file_title.pack(anchor="w", padx=20, pady=5)

select_title = tk.Label(root, text="Choose File: ", font=('Arial', 12))
select_title.pack(anchor="w", padx=20, pady=5)

jl.input_file_path = tk.StringVar()
file_label_var = tk.StringVar()
file_label_var.set("No files selected")

select_button = tk.Button(root, text="Select File", command=select_files)
select_button.pack(anchor="w", padx=40, pady=2)

file_label = tk.Label(root, textvariable=file_label_var, font=('Arial', 10), anchor="w", wraplength=1000)
file_label.pack(anchor="w", padx=40, pady=5)



# Overwrite Section
overwrite_box = tk.Label(root, text="Overwrite the Original File?", font=('Arial', 12))
overwrite_box.pack(anchor="w", padx=20, pady=5)

check_var = tk.IntVar()
checkbox = tk.Checkbutton(root, variable=check_var, relief="ridge", bd=2)
checkbox.pack(anchor="w", padx=40, pady=2)

overwrite_button = tk.Button(root, text="Save As", command=select_files)
overwrite_button.pack(anchor="w", padx=40, pady=5)



# Map Button
map_button = tk.Button(root, text='Map', command=lambda: map(jl))
map_button.pack(anchor="w", padx=20, pady=20)
# map_button = tk.Button(root, text='Map', command=lambda: map(input_file_path.get(), jl.dropdown_options, jl.fields, jl.field_dict, jl))


# Verify Button
verify_button = tk.Button(root, text='Verify', command=lambda: verify(jl))
verify_button.place(x=600, y=375)
# verify_button = tk.Button(root, text='Verify', command=lambda: verify(input_file_btn.get(), jl.field_dict, jl))


# Errors Section
error_title = tk.Label(root, text="Errors", font=('Arial', 14))
error_title.pack(anchor="w", padx=20, pady=5)

row_count = tk.Label(root, text="Rows Read: ", font=('Arial', 12))
row_count.pack(anchor="w", padx=40, pady=2)

success_count = tk.Label(root, text="Successful: ", font=('Arial', 12))
success_count.pack(anchor="w", padx=40, pady=2)

error_count = tk.Label(root, text="Errors: ", font=('Arial', 12))
error_count.pack(anchor="w", padx=40, pady=2)

error_view = tk.Button(root, text='View Errors', command=Error_Window)
error_view.pack(anchor="w", padx=20, pady=10)



# Dropdown Menus Section
dropdown_frame = tk.Frame(root)
dropdown_frame.place(x=600, y=50)

jl.fields = [
    "First Name", "Last Name", "Email", "Phone", "Street Address", "City", "State", "Zip Code", "County"
]

jl.field_dict = {}  # field type : csv header
                 

jl.dropdown_options = []

# Create labels and dropdown menus
for idx, field in enumerate(jl.fields):
    label = tk.Label(dropdown_frame, text=field, font=('Arial', 12))
    label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

    dropdown = ttk.Combobox(dropdown_frame, width=20) 
    dropdown.grid(row=idx, column=1, padx=10, pady=5)
    jl.dropdown_options.append(dropdown)

    dropdown.bind("<<ComboboxSelected>>", update_field_dict)

# Apply Theme
#sv_ttk.set_theme("dark")

root.mainloop()
