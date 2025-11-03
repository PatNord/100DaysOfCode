from tkinter import *
from tkinter import messagebox
import random
import json

def save():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":username,
            "password":password
    }}  

    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="alert", message="website or password field is empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail: {username} \nPassword: {password}")
        if is_ok:
            #jos tiedostoa ei ole, luodaan tyhjä dict "data". Sen jälkeen se päivitetään sisältämään website username password ja kirjoitetaan lopuksi
            #json tiedostoon.
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def load_data():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="alert", message="Type name of the website in search box.")
        return

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="alert", message="information not found.")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Data file is corrupted or empty.")
    else:
        if website in data:
             messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \n Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Not found", message=f"No details for '{website}' found.")
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email or username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Patrik.Nordlund@yahoo.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#buttons
search_button = Button(text="Search", command=load_data)
search_button.grid(row=1, column=2)
gen_passwrd_button = Button(text="Generate password", command=generate_password)
gen_passwrd_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()