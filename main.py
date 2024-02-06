from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ------------- PASSWORD GENERATOR -------------#

# ---------------- SAVE PASSWORD ------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="fill the all blank space")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"these are the details"f" entred,\n Email:{email}\n"f"password  {password}. is it ok?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------- UI SETUP --------------#

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="lock_image.png")
canvas.create_image(100, 60, image=lock_image)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="website")
website_label.grid(row=1, column=0)
website_label.config(padx=10, pady=10)

email_label = Label(text="email")
email_label.grid(row=2, column=0)
email_label.config(padx=10, pady=10)

password_label = Label(text="password")
password_label.grid(row=3, column=0)
password_label.config(padx=10, pady=10)
# entry

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=29)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "dulalbijaya7@gmail.com")  # this helps to display the text on entry bar
# given as argumet( index , "text")


password_entry = Entry(width=36)
password_entry.grid(row=3, column=1, )

# Buttons
generate_pass = Button(text="Generate password")
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1)

window.mainloop()
