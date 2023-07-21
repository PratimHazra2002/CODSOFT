from tkinter import *


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


window = Tk()
window.geometry("350x350")
window.resizable(None, None)
window.title("Calculator")
expression = ""
input_text = StringVar()
input_frame = Frame(window, width=320, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
entry_field = Entry(input_frame, font=("arial 20 bold"), textvariable=input_text, width=50, fg="White", bg="black", bd=0, justify=RIGHT)
entry_field.grid(row=0, column=0)
entry_field.pack(ipady=10)
buttons_frame = Frame(window, width=320, height=280, bg="black")
buttons_frame.pack()


clear = Button(buttons_frame, text="C", fg="black", width=21, height=3, bd=0, bg="red", cursor="hand2", command=lambda: bt_clear()).grid(row=1, column=0, columnspan=2, padx=1, pady=1)

open_bracket = Button(buttons_frame, text="(", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", command=lambda: btn_click("(")).grid(row=1, column=2, padx=1, pady=1)

close_bracket = Button(buttons_frame, text=")", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", command=lambda: btn_click(")")).grid(row=1, column=3, padx=1, pady=1)


one = Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(1)).grid(row=2, column=0, padx=1, pady=1)

two = Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(2)).grid(row=2, column=1, padx=1, pady=1)

three = Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(3)).grid(row=2, column=2, padx=1, pady=1)

divide = Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", command=lambda: btn_click("/")).grid(row=2, column=3, padx=1, pady=1)


four = Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(4)).grid(row=3, column=0, padx=1, pady=1)

five = Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(5)).grid(row=3, column=1, padx=1, pady=1)

six = Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(6)).grid(row=3, column=2, padx=1, pady=1)

multiply = Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", command=lambda: btn_click("*")).grid(row=3, column=3, padx=1, pady=1)


seven = Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(7)).grid(row=4, column=0, padx=1, pady=1)

eight = Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(8)).grid(row=4, column=1, padx=1, pady=1)

nine = Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(9)).grid(row=4, column=2, padx=1, pady=1)

minus = Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", command=lambda: btn_click("-")).grid(row=4, column=3, padx=1, pady=1)


zero = Button(buttons_frame, text="0", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(0)).grid(row=5, column=0, columnspan=1, padx=1, pady=1)

point = Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", command=lambda: btn_click(".")).grid(row=5, column=1, padx=1, pady=1)

equals = Button(buttons_frame, text="=", fg="white", width=10, height=3, bd=0, bg="blue", cursor="hand2", command=lambda: bt_equal()).grid(row=5, column=2, padx=1, pady=1)

plus = Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", command=lambda: btn_click("+")).grid(row=5, column=3, padx=1, pady=1)

window.mainloop()
