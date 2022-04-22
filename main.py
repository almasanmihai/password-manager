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
    if len(web_entry.get()) == 0 or len(pas_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{web_entry}",
                                       message=f"These are details entered:\nEmail: {mail_entry.get()}\n"
                                               f"Password: {pas_entry.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{web_entry.get()} | {mail_entry.get()} | {pas_entry.get()}\n")
            web_entry.delete(0, END)
            mail_entry.delete(0, END)
            pas_entry.delete(0, END)
            mail_entry.insert(0, "someone@example.com")

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
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_entry.focus()

mail_entry = Entry()
mail_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
mail_entry.insert(0, "someone@example.com")

pas_entry = Entry()
pas_entry.grid(column=1, row=3, sticky="EW")

gen_pas = Button(text="Generate Password", command=generate_password)
gen_pas.grid(column=2, row=3, sticky="EW")

add_pas = Button(text="Add", command=save)
add_pas.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
