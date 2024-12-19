import tkinter as tk
from tkinter import messagebox


def handle_verify():
    # Simulate verification logic (replace this with your actual implementation)
    print("Verification functionality triggered!")


# constructor
root = tk.Tk()

class myGui:
    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your message", font=('Arial', 12))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 11))
        self.textbox.pack(padx=10, pady=10)

        #need to add a variable that has the content of the text button
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 12), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Show message", font=('Arial', 12), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()


    def show_message(self):
        if self.check_state.get() == 0:
            print(self.check_state.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    #use as a message for when the user is closing the application

myGui()