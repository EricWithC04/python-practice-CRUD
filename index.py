import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

class ClientForm:
    def Form():
        try:
            root = tk.Tk()
            root.title("Client Form")
            root.geometry("1280x720")
            groupBox = tk.LabelFrame(root, text="Client Details", padx=10, pady=10)
            groupBox.grid(row=0, column=0, padx=10, pady=10)

            nameLabel = tk.Label(groupBox, text="Name:", width=15, font=("Oswald", 10)).grid(row=0, column=0)
            nameInput = tk.Entry(groupBox)
            nameInput.grid(row=0, column=1)

            surnameLabel = tk.Label(groupBox, text="Surname:", width=15, font=("Oswald", 10)).grid(row=1, column=0)
            surnameInput = tk.Entry(groupBox)
            surnameInput.grid(row=1, column=1)

            ageLabel = tk.Label(groupBox, text="Age:", width=15, font=("Oswald", 10)).grid(row=2, column=0)
            ageInput = tk.Entry(groupBox)
            ageInput.grid(row=2, column=1)

            genreLabel = tk.Label(groupBox, text="Genre:", width=15, font=("Oswald", 10)).grid(row=3, column=0)
            genreInput = tk.StringVar()
            combo = ttk.Combobox(groupBox, textvariable = genreInput, values=["Male", "Female"])
            combo.grid(row=3, column=1)

            tk.Button(groupBox, text='Submit', width=10).grid(row=4, column=0)
            tk.Button(groupBox, text='Delete', width=10).grid(row=4, column=1)
            tk.Button(groupBox, text='Update', width=10).grid(row=4, column=2)

            root.mainloop()
        except ValueError:
            messagebox.showerror("Error", "Please Enter Correct Details")
    
    Form()