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
        input_file_label_var.set(file_name_short)
    else:
        jl.input_file_path.set("") 
        input_file_label_var.set("No files selected")

'''def check_status():
    if check_var.get() == 1:
        print("Checkbox is checked")
    else:
        print("Checkbox is not checked") '''

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
input_file_title = tk.Label(root, text="Input File Select", font=('Arial', 14))
input_file_title.pack(anchor="w", padx=20, pady=5)

input_select_title = tk.Label(root, text="Choose File: ", font=('Arial', 12))
input_select_title.pack(anchor="w", padx=20, pady=5)

jl.input_file_path = tk.StringVar()
input_file_label_var = tk.StringVar()
input_file_label_var.set("No files selected")

input_select_button = tk.Button(root, text="Select File", command=select_files)
input_select_button.pack(anchor="w", padx=40, pady=2)

input_file_label = tk.Label(root, textvariable=input_file_label_var, font=('Arial', 10), anchor="w", wraplength=1000)
input_file_label.pack(anchor="w", padx=40, pady=5)


# File Uploads Section
output_file_title = tk.Label(root, text="Output File Select", font=('Arial', 14))
output_file_title.pack(anchor="w", padx=20, pady=5)

output_select_title = tk.Label(root, text="Choose File: ", font=('Arial', 12))
output_select_title.pack(anchor="w", padx=20, pady=5)

jl.output_file_path = tk.StringVar()
output_file_label_var = tk.StringVar()
output_file_label_var.set("No files selected")

output_select_button = tk.Button(root, text="Select File", command=select_files)
output_select_button.pack(anchor="w", padx=40, pady=2)

output_file_label = tk.Label(root, textvariable=output_file_label_var, font=('Arial', 10), anchor="w", wraplength=1000)
output_file_label.pack(anchor="w", padx=40, pady=5)



# Map Button
map_button = tk.Button(root, text='Map', command=lambda: map(jl))
map_button.pack(anchor="w", padx=20, pady=20)


# Verify Button
verify_button = tk.Button(root, text='Verify', command=lambda: verify(jl))
verify_button.place(x=600, y=375)


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
