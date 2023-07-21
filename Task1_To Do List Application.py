import tkinter as tk
from tkinter import messagebox
from tkinter import *

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        selected_index = listbox.curselection()
        listbox.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def update_task():
    try:
        selected_index = listbox.curselection()
        task = entry.get()
        if task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")


def clear_tasks():
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if confirmed:
        listbox.delete(0, tk.END)


def get_selected_task(event):
    try:
        selected_index = listbox.curselection()
        task = listbox.get(selected_index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, task)
    except:
        pass

window = tk.Tk()
window.title("To-Do List")

heading = Label(window, text="ALL TASKS", font="arial 20 bold", fg="white", bg="Green")
heading.pack(pady=0)


listbox = tk.Listbox(window, width=50, bg="black", fg="white")
listbox.pack(pady=50)
listbox.bind("<<ListboxSelect>>", get_selected_task)


scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


entry = tk.Entry(window, width=50)
entry.pack(pady=10)


add_button = tk.Button(window, text="Add Task", bg="#00ff00", fg="#000", bd=0, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", bg="#ff0000", fg="#fff", bd=0, command=delete_task)
delete_button.pack(pady=5)

update_button = tk.Button(window, text="Update Task", bg="#0000ff", fg="#fff", bd=0, command=update_task)
update_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear All", bg="yellow", fg="#000", bd=0, command=clear_tasks)
clear_button.pack(pady=5)


window.mainloop()
