from tkinter import *
from random import randint


def generate():
	passwords.delete(0, END)
	password_length = int(length_get.get())
	the_password = ""
	for x in range(password_length):
		the_password += chr(randint(33, 126))
	passwords.insert(0, the_password)


def copy():
	window.clipboard_clear()
	window.clipboard_append(passwords.get())


def clear():
	for widget in window.winfo_children():
		if isinstance(widget, Entry):
			widget.delete(0, END)


window = Tk()
window.title('Password Generator app')
window.geometry("500x300")


User = Label(window, text="User name: ", font="arial 10", fg="white", bg="brown")
User.pack(pady=10)
user_name = Entry(window)
user_name.pack(pady=10)

length = Label(window, text="Enter the length: ", font="arial 10", fg="white", bg="brown")
length.pack(pady=10)
length_get = Entry(window)
length_get.pack(pady=10)

generated_password = Label(window, text="Generated Password ", font="arial 10", fg="white", bg="blue")
generated_password.pack(pady=10)
passwords = Entry(window)
passwords.pack(pady=10)

frame = Frame(window)
frame.pack(pady=10)

generate_button = Button(frame, text="Generate Password", fg="black", bg="cyan", command=generate)
generate_button.grid(row=0, column=0, padx=10)

copy_button = Button(frame, text="Save", fg="yellow", bg="green", command=copy)
copy_button.grid(row=0, column=1, padx=10)

clear_button = Button(frame, text="Reset", fg="yellow", bg="red", command=clear)
clear_button.grid(row=0, column=2, padx=10)

window.mainloop()
