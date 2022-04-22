from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
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

password = Label(text="Password:")
password.grid(column=0, row=3, sticky="E")

web_entry = Entry()
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_entry.focus()

mail_entry = Entry()
mail_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
mail_entry.insert(0, "someone@example.com")

pas_entry = Entry()
pas_entry.grid(column=1, row=3, sticky="EW")

gen_pas = Button(text="Generate Password")
gen_pas.grid(column=2, row=3, sticky="EW")

add_pas = Button(text="Add", command=save)
add_pas.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()