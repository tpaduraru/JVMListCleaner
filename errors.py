import tkinter as tk
from tkinter import messagebox
from jvmlist import JVMList



class Error_Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Error Viewer")
        self.root.geometry("600x800")

        self.label = tk.Label(self.root, text="Errors", font=('Arial', 12))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 11))
        self.textbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        close_button = tk.Button(self.root, text="Close", command=self.root.destroy)
        close_button.pack(pady=10)

        if self.check_state.get() == 0:
            print(self.check_state.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
            self.textbox.config(state=tk.DISABLED)
            
        self.root.mainloop()
