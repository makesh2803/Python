import tkinter as tk
from tkinter import messagebox
import os

# File to store contacts
CONTACTS_FILE = "contacts.txt"

def load_contacts():
    """Load contacts from the file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_contacts(contacts):
    """Save contacts to the file"""
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(contact + "\n")

def add_contact():
    """Add a new contact"""
    name = entry_name.get()
    phone = entry_phone.get()

    if name and phone:
        contact = f"{name} - {phone}"
        contacts.append(contact)
        save_contacts(contacts)
        listbox_contacts.insert(tk.END, contact)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please provide both name and phone.")

def delete_contact():
    """Delete the selected contact"""
    try:
        selected_index = listbox_contacts.curselection()[0]
        contact = listbox_contacts.get(selected_index)
        contacts.remove(contact)
        save_contacts(contacts)
        listbox_contacts.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

def search_contact():
    """Search for a contact"""
    search_term = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact.lower():
            listbox_contacts.insert(tk.END, contact)

# Initialize the window
window = tk.Tk()
window.title("Contact Book")

# Create widgets
frame = tk.Frame(window)
frame.pack(pady=10)

label_name = tk.Label(frame, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

label_phone = tk.Label(frame, text="Phone:")
label_phone.grid(row=1, column=0)
entry_phone = tk.Entry(frame)
entry_phone.grid(row=1, column=1)

button_add = tk.Button(frame, text="Add Contact", command=add_contact)
button_add.grid(row=2, column=0, columnspan=2, pady=5)

label_search = tk.Label(frame, text="Search:")
label_search.grid(row=3, column=0)
entry_search = tk.Entry(frame)
entry_search.grid(row=3, column=1)

button_search = tk.Button(frame, text="Search", command=search_contact)
button_search.grid(row=4, column=0, columnspan=2, pady=5)

button_delete = tk.Button(frame, text="Delete Contact", command=delete_contact)
button_delete.grid(row=5, column=0, columnspan=2, pady=5)

# Listbox to display contacts
listbox_contacts = tk.Listbox(window, width=40, height=10)
listbox_contacts.pack(pady=10)

# Load contacts from file
contacts = load_contacts()

# Display existing contacts
for contact in contacts:
    listbox_contacts.insert(tk.END, contact)

# Start the Tkinter event loop
window.mainloop()