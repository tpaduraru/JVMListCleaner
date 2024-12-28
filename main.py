import tkinter as tk
from tkinter import filedialog
import os
from tkinter import ttk
import time
from errors import Error_Window
from map import map
from verify import verify

''' 
Model = the list/array that you are manipulating. View = tkinter + output csv. Controller = tkinter buttons
'''


def select_files():
    filenames = filedialog.askopenfilenames(filetypes=[("CSV Files", "*.csv")])
    if filenames:
        # Use the first file from the selection
        input_file.set(filenames[0])
        file_names = ", ".join([os.path.basename(file) for file in filenames])
        file_label_var.set(file_names)
    else:
        input_file.set("") 
        file_label_var.set("No files selected")

def check_status():
    if check_var.get() == 1:
        print("Checkbox is checked")
    else:
        print("Checkbox is not checked")


# Initialize root window
root = tk.Tk()
root.geometry("1200x700")
root.title("JVM List Cleaner")

# Title
Title = tk.Label(root, text="List Cleaner", font=('Arial', 18))
Title.pack(anchor="w", padx=20, pady=10)

# File Uploads Section
File_Title = tk.Label(root, text="File Select", font=('Arial', 14))
File_Title.pack(anchor="w", padx=20, pady=5)

Select_Title = tk.Label(root, text="Choose File: ", font=('Arial', 12))
Select_Title.pack(anchor="w", padx=20, pady=5)

input_file = tk.StringVar()
file_label_var = tk.StringVar()
file_label_var.set("No files selected")

select_button = tk.Button(root, text="Select File", command=select_files)
select_button.pack(anchor="w", padx=40, pady=2)

file_label = tk.Label(root, textvariable=file_label_var, font=('Arial', 10), anchor="w", wraplength=1000)
file_label.pack(anchor="w", padx=40, pady=5)

# Overwrite Section
Overwrite_Box = tk.Label(root, text="Overwrite the Original File?", font=('Arial', 12))
Overwrite_Box.pack(anchor="w", padx=20, pady=5)

check_var = tk.IntVar()
checkbox = tk.Checkbutton(root, variable=check_var, relief="ridge", bd=2)
checkbox.pack(anchor="w", padx=40, pady=2)

overwrite_button = tk.Button(root, text="Save As", command=select_files)
overwrite_button.pack(anchor="w", padx=40, pady=5)

# Map Button
map_button = tk.Button(root, text='Map', command=lambda: map(input_file.get(), dropdown_options))
map_button.pack(anchor="w", padx=20, pady=20)

# Verify Button
verify_button = tk.Button(root, text='Verify', command=lambda: verify(input_file.get(), dropdown_options))
verify_button.place(x=600, y=375)

# Errors Section
Error_Title = tk.Label(root, text="Errors", font=('Arial', 14))
Error_Title.pack(anchor="w", padx=20, pady=5)

Row_Count = tk.Label(root, text="Rows Read: ", font=('Arial', 12))
Row_Count.pack(anchor="w", padx=40, pady=2)

Success_Count = tk.Label(root, text="Successful: ", font=('Arial', 12))
Success_Count.pack(anchor="w", padx=40, pady=2)

Error_Count = tk.Label(root, text="Errors: ", font=('Arial', 12))
Error_Count.pack(anchor="w", padx=40, pady=2)

ErrorView = tk.Button(root, text='View Errors', command=Error_Window)
ErrorView.pack(anchor="w", padx=20, pady=10)

# Dropdown Menus Section
dropdown_frame = tk.Frame(root)
dropdown_frame.place(x=600, y=50)

fields = [
    "First Name", "Last Name", "Email", "Phone", "Street Address", "City", "State", "Zip Code", "County"
]

dropdown_options = []

# Create labels and dropdown menus
for idx, field in enumerate(fields):
    label = tk.Label(dropdown_frame, text=field, font=('Arial', 12))
    label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
    
    # in the loop

    dropdown = ttk.Combobox(dropdown_frame, width=20) 
    dropdown.grid(row=idx, column=1, padx=10, pady=5)
    dropdown_options.append(dropdown)

# Apply Theme
#sv_ttk.set_theme("dark")

root.mainloop()
