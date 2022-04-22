import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pas_char = [random.choice(letters) for _ in range(nr_letters)]
    pas_num = [random.choice(numbers) for _ in range(nr_numbers)]
    pas_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = pas_char + pas_symbol + pas_num
    random.shuffle(password_list)
    password = "".join(password_list)
    pas_entry.delete(0, END)
    pas_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get().title()
    new_data = {website: {"email": mail_entry.get(), "password": pas_entry.get()}}
    if len(website) == 0 or len(pas_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"These are details entered for {website}:\nEmail: {mail_entry.get()}\n"
                                               f"Password: {pas_entry.get()} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    if website in data:
                        overwrite = messagebox.askokcancel("Overwrite", f"Details for {website} exist.\n"
                                                                        f"Do you want to overwrite?")
                        if overwrite:
                            data.update(new_data)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            web_entry.delete(0, END)
            mail_entry.delete(0, END)
            pas_entry.delete(0, END)
            mail_entry.insert(0, "someone@example.com")


# ---------------------------- SEARCH ------------------------------- #


def search():
    website = web_entry.get().title()
    try:
        with open("data.json", "r") as file:
            read = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("File not found", "No data file found")
    else:
        if website in read:
            messagebox.showinfo(title=f"Your credentials for {website}",
                                message=f"Your user name is {read[website]['email']}\n"
                                        f"Your password is {read[website]['password']}")
        else:
            messagebox.showinfo(title=f"No details for {website}",
                                message=f"No details for {website} exist")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
img = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

web = Label(text="Website:")
web.grid(column=0, row=1, sticky="E")

user_name = Label(text="Email/User Name:")
user_name.grid(column=0, row=2, sticky="E")

pass_word = Label(text="Password:")
pass_word.grid(column=0, row=3, sticky="E")

web_entry = Entry()
web_entry.grid(column=1, row=1, sticky="EW")
web_entry.focus()

mail_entry = Entry()
mail_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
mail_entry.insert(0, "someone@example.com")

pas_entry = Entry()
pas_entry.grid(column=1, row=3, sticky="EW")

gen_pas = Button(text="Generate Password", command=generate_password, bg="#CD6155")
gen_pas.grid(column=2, row=3, sticky="EW")

add_pas = Button(text="Add", command=save, bg="#9CF806")
add_pas.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", width=15, bg="#D6EAF8", command=search)
search_button.grid(column=2, row=1, sticky="W")

window.mainloop()
