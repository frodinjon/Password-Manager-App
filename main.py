import random
from tkinter import *
from tkinter import messagebox
import pyperclip

FONT = ("Arial", 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
					"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", 
					"e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
					"u", "v", "w", "x", "y", "z"]
SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", ",", "<", 							">", "?", ".", ":", ";"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password_list = []
def generate_password():
	global password_list
	letter_list = [random.choice(LETTERS) for _ in range(random.randint(8,10))]

	number_list = [random.choice(NUMBERS) for _ in range(random.randint(2,4))]

	symbol_list = [random.choice(SYMBOLS) for _ in range(random.randint(2,4))]

	password_list = letter_list + number_list + symbol_list

	#shuffle password list
	random.shuffle(password_list)

	#conver to string and place in box
	password_string = "".join(password_list)
	#clear existing text
	password_entry.delete(0, END)
	password_entry.insert(0, password_string)
	#reset the array	
	password_list = []
	pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
	if len(email_entry.get()) > 0 and len(password_entry.get()) > 0 and len(website_entry.get()) > 0:
		is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \n Email: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it okay to save?")
		if is_ok:
			with open("password_vault.txt", mode='a') as file:
				file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
			website_prompt.delete(0, END)
			password_prompt.delete(0, END)
	else:
		messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0,column=1)

# Labels
website_prompt = Label(text="Website:", font = FONT)
website_prompt.grid(row=1, column=0)
email_prompt = Label(text="Email/Username:", font = FONT)
email_prompt.grid(row=2, column=0)
password_prompt = Label(text="Password:", font = FONT)
password_prompt.grid(row=3, column=0)

#Entries
website_entry = Entry(width=40)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0, "myemail@sharklasers.com")
password_entry = Entry(width=22)
password_entry.grid(row=3,column=1, columnspan=1)

#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()