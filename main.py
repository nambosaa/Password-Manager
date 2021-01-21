from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH BUTTON ------------------------------- #


def search():
    website = web_field.get()
    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)
            site_data = data[website]
            email = site_data['email']
            password = site_data['password']
    except FileNotFoundError:
        messagebox.showerror(title="No Data", message="Please add data first")
    except KeyError:
        messagebox.showerror(title="Website Not Available", message="Website information not available")
    else:
        messagebox.showinfo(title="Your Login Details", message=f"Email: {email} \nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_field.get()
    email = email_field.get()
    password = pass_field.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty")
    else:
        try:
            with open("password.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_field.delete(0, END)
            pass_field.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

FONTNAME = ("Courier")


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)

# Logo
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Website

web_label = Label(text="Website", font=FONTNAME)
web_label.grid(column=0, row=1)

# Email/Username
email_label = Label(text="Email/Username", font=FONTNAME)
email_label.grid(column=0, row=2)

# Password
password_label = Label(text="Password", font=FONTNAME)
password_label.grid(column=0, row=3)

# Website Field
web_field = Entry(width = 50)
web_field.grid(column=1, row=1, columnspan=2)
web_field.focus()

# Email Field
email_field = Entry(width=50)
email_field.grid(column=1, row=2, columnspan=2)
email_field.insert(0, "sahil@email.com")

# Password Field
pass_field = Entry(width=50)
pass_field.grid(column=1, row=3, columnspan=2)

# Generate Password Button
generate_btn = Button(text="Generate Password", width=15, command=generate)
generate_btn.grid(column=2, row=3)

# Add Button
add_btn = Button(text="Add", width=43, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

# Search Button
search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(column=2, row=1)

window.mainloop()
