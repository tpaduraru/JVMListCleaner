import tkinter as tk
from tkinter import filedialog
import os
#import sv_ttk

from errors import Error_Window
from map import handle_map
from verify import handle_verify


def select_files():
    filenames = filedialog.askopenfilenames(filetypes=[("CSV Files", "*.csv")]) 
    if filenames:
        file_names = ", ".join([os.path.basename(file) for file in filenames])
        file_label_var.set(file_names)
    else:
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
Select_Title.pack(anchor="w", padx=20, pady=2)

select_button = tk.Button(root, text="Select File", command=select_files)
Select_Title.place(x=150, y=110, height=50, width=100)

file_label_var = tk.StringVar()
file_label_var.set("No files selected")
file_label = tk.Label(root, textvariable=file_label_var, font=('Arial', 10), anchor="w", wraplength=1000)
file_label.pack(anchor="w", padx=40, pady=2)

# Overwrite Section
Overwrite_Box = tk.Label(root, text="Overwrite an Existing File?", font=('Arial', 12))
Overwrite_Box.pack(anchor="w", padx=20, pady=5)

check_var = tk.IntVar()
checkbox = tk.Checkbutton(root, variable=check_var, relief="ridge", bd=2)
checkbox.pack(anchor="w", padx=40, pady=2)

overwrite_button = tk.Button(root, text="Overwrite File", command=select_files)
overwrite_button.pack(anchor="w", padx=40, pady=5)

# Map Button
MapBtn = tk.Button(root, text='Map', command=handle_map)
MapBtn.pack(anchor="w", padx=20, pady=20)

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

# Apply theme
#sv_ttk.set_theme("dark")
root.mainloop()
