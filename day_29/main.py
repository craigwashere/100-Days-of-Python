import tkinter
from tkinter import messagebox
import random
import pyperclip

ENTRY_WIDTH = 52
PASSWORD_ENTRY_WIDTH = 32
ADD_BUTTON_WIDTH = 44
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
                'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(0, random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(0, random.randint(2, 4))])

    random.shuffle(password_list)

    password = ''.join(password_list)
    
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_click():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please enter all fields.")
        return
        
    if not messagebox.askokcancel(title=f"{website}", 
        message=f"These are the details entered\nEmail: {email}\nPassword: {password}\nIs it OK to save?"):
        return
    
    with open("data.txt", "a") as f:
        f.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


lock_image = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(height=200, width=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0, sticky='e')
website_entry = tkinter.Entry(width=ENTRY_WIDTH)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky='e')
email_entry = tkinter.Entry(width=ENTRY_WIDTH)
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')
email_entry.insert(tkinter.END, "email@company.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0, sticky='e')
password_entry = tkinter.Entry(width=PASSWORD_ENTRY_WIDTH, justify="left")
password_entry.grid(row=3, column=1, sticky='w')
password_button = tkinter.Button(text="Generate Password", command=get_password)
password_button.grid(row=3, column=2, sticky='w')

add_button = tkinter.Button(text="Add", width=ADD_BUTTON_WIDTH, command=add_button_click)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()
