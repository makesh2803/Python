import tkinter as tk
from tkinter import messagebox

# Function to save user details
def save_details():
    name = entry_name.get()
    surname = entry_surname.get()
    phone = entry_phone.get()
    instagram = entry_instagram.get()
    location = entry_location.get()
    product = entry_product.get()

    if name and surname and phone and instagram and location and product:
        user_info = f"Name: {name}\nSurname: {surname}\nPhone: {phone}\nInstagram: {instagram}\nLocation: {location}\nProduct: {product}\n\n"
       
        with open("user_data.txt", "a") as file:
            file.write(user_info)

        messagebox.showinfo("Success", "Details saved successfully!")

        # Clear input fields
        entry_name.delete(0, tk.END)
        entry_surname.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_instagram.delete(0, tk.END)
        entry_location.delete(0, tk.END)
        entry_product.delete(0, tk.END)

    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Create main window
window = tk.Tk()
window.title("User Information Form")
window.geometry("400x350")

# Labels and Entry fields
tk.Label(window, text="Name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Surname:").pack()
entry_surname = tk.Entry(window)
entry_surname.pack()

tk.Label(window, text="Phone Number:").pack()
entry_phone = tk.Entry(window)
entry_phone.pack()

tk.Label(window, text="Instagram:").pack()
entry_instagram = tk.Entry(window)
entry_instagram.pack()

tk.Label(window, text="Location:").pack()
entry_location = tk.Entry(window)
entry_location.pack()

tk.Label(window, text="Product:").pack()
entry_product = tk.Entry(window)
entry_product.pack()

# Submit Button
btn_submit = tk.Button(window, text="Submit", command=save_details)
btn_submit.pack(pady=10)

# Run the application
window.mainloop()