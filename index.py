import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from clients import client

def save_registers():

    global nameInput, surnameInput, combo, ageInput, groupBox

    try:
        if nameInput is None or surnameInput is None or combo is None or ageInput is None or genreInput is None:
            print("Todos los campos deben estar completados")
            return
        
        name = nameInput.get()
        surname = surnameInput.get()
        age = ageInput.get()
        genre = combo.get()

        client.addClient(name, surname, age, genre)
        messagebox.showinfo("Información", "Datos cargados con exito!")

        nameInput.delete(0, tk.END)
        surnameInput.delete(0, tk.END)
        ageInput.delete(0, tk.END)
        combo.delete(0, tk.END)

        update_registers()

    except Exception as e: print(f"Error: {e}")

def update_register_data(event):
    try:
        selected_item = tree.focus()

        if selected_item:
            values = tree.item(selected_item)["values"]

            nameInput.delete(0, tk.END)
            nameInput.insert(0, values[0])
            surnameInput.delete(0, tk.END)
            surnameInput.insert(0, values[1])
            ageInput.delete(0, tk.END)
            ageInput.insert(0, values[2])
            combo.set(values[3])
    except Exception as e:
        print(f"Error al actualizar los datos: {e}")

def save_updated_register():

    global nameInput, surnameInput, combo, ageInput, groupBox

    try:
        if nameInput is None or surnameInput is None or combo is None or ageInput is None or genreInput is None:
            print("Todos los campos deben estar completados")
            return
        
        name = nameInput.get()
        surname = surnameInput.get()
        age = ageInput.get()
        genre = combo.get()

        client.updateClient(name, surname, age, genre)
        messagebox.showinfo("Información", "Datos actualizados con exito!")

        nameInput.delete(0, tk.END)
        surnameInput.delete(0, tk.END)
        ageInput.delete(0, tk.END)
        combo.delete(0, tk.END)

        update_registers()

    except Exception as e: print(f"Error: {e}")

def delete_register():

    global nameInput, surnameInput, combo, ageInput, groupBox

    try:
        if nameInput is None or surnameInput is None:
            print("Todos los campos deben estar completados")
            return
        
        name = nameInput.get()
        surname = surnameInput.get()
        age = ageInput.get()
        genre = combo.get()

        client.deleteClient(name, surname)
        messagebox.showinfo("Información", "Datos eliminados con exito!")

        nameInput.delete(0, tk.END)
        surnameInput.delete(0, tk.END)
        ageInput.delete(0, tk.END)
        combo.delete(0, tk.END)

        update_registers()

    except Exception as e: print(f"Error: {e}")

def update_registers():
    try:
        
        global tree

        tree.delete(*tree.get_children())

        data = client.showClients()

        for register in data:
            tree.insert('', tk.END, values=(register[1], register[2], register[3], register[4]))
        
        tree.bind("<<TreeviewSelect>>", update_register_data)

    except Exception as e:
        print(f"Error al actualizar la lista de usuarios: {e}")

class ClientForm:

    global root
    root = None

    global nameInput
    nameInput = None

    global surnameInput
    surnameInput = None

    global ageInput
    ageInput = None

    global genreInput
    genreInput = None

    global groupBox
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None
    def Form():
        
        global root
        global nameInput
        global surnameInput
        global ageInput
        global genreInput
        global groupBox
        global tree
        global combo

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

            tk.Button(groupBox, text='Submit', width=10, command=save_registers).grid(row=4, column=0)
            tk.Button(groupBox, text='Delete', width=10, command=delete_register).grid(row=4, column=1)
            tk.Button(groupBox, text='Update', width=10, command=save_updated_register).grid(row=4, column=2)

            groupBox = tk.LabelFrame(root, text="Client List", padx=10, pady=10)
            groupBox.grid(row=0, column=1, padx=10, pady=10)

            tree = ttk.Treeview(groupBox, columns=('Name', 'Surname', 'Age', 'Genre'), show='headings', height=10)
            tree.column('Name', anchor=tk.CENTER)
            tree.heading('Name', text="Name")
            tree.column('Surname', anchor=tk.CENTER)
            tree.heading('Surname', text="Surname")
            tree.column('Age', anchor=tk.CENTER)
            tree.heading('Age', text="Age")
            tree.column('Genre', anchor=tk.CENTER)
            tree.heading('Genre', text="Genre")

            update_registers()

            tree.pack()

            root.mainloop()
        except ValueError:
            messagebox.showerror("Error", "Please Enter Correct Details")

    Form()
