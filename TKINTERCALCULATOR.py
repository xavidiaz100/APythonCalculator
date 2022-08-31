# import tkinter
from tkinter import *
#Global variables

# creates window
window = Tk()
window.title("BRENDANATOR's AWESOME CALCULATOR")
e = Entry(window, width=100, borderwidth=5)
e.grid(row=0, columnspan=5, padx=20, pady=20)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear_button():
    e.delete(0, END)
def add_button():
    first_input = e.get()
    global f_num
    global operation
    operation = "ADD"
    f_num = int(first_input)
    e.delete(0, END)
def equal_button():
    second_input = e.get()
    e.delete(0, END)
    if (operation == "ADD"):
        e.insert(0, (f_num) + int(second_input))
    if (operation =="SUB"):
        e.insert(0, (f_num) - int(second_input))
    if (operation == "MULT"):
        e.insert(0, (f_num) * int(second_input))
    if (operation == "DIV"):
        e.insert(0, (f_num) / int(second_input))
def button_sub():
    first_input = e.get()
    global f_num
    global operation
    operation = "SUB"
    f_num = int(first_input)
    e.delete(0, END)
def button_mult():
    first_input = e.get()
    global f_num
    global operation
    operation = "MULT"
    f_num = int(first_input)
    e.delete(0, END)
def button_div():
    first_input = e.get()
    global f_num
    global operation
    operation = "DIV"
    f_num = int(first_input)
    e.delete(0, END)
def button_inst():
    e.insert(0,'USE "=" AFTER EACH EXPRESSION')


# define buttons
button_INST = Button(window, text ="INSTRUCTIONS",padx= 20, pady= 20, bg = "yellow", bd = 10, font = "Modern", command=button_inst)
button_1 = Button(window, text="1", padx=65, pady=20,bd = 5, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=65, pady=20, bd = 5,command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=65, pady=20,bd = 5, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=65, pady=20,bd = 5, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=65, pady=20, bd = 5,command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=65, pady=20,bd = 5, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=65, pady=20,bd = 5, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=65, pady=20,bd = 5, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=65, pady=20,bd = 5, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=65, pady=20,bd = 5, command=lambda: button_click(0))
button_add = Button(window, text="+", padx=65, pady=19, bd = 5,command=add_button)
button_equal = Button(window, text="=", padx=65, pady=19,bd = 5, command=equal_button)
button_clear = Button(window,text="CLEAR", padx=65, pady=19,bd = 5, command=clear_button)
button_sub = Button(window, text = "-", padx = 65, pady = 19,bd = 5,command=button_sub)
button_mult = Button(window, text = "X", padx = 65, pady = 19,bd = 5,command=button_mult)
button_div = Button(window, text = "%", padx = 65, pady = 19,bd = 5,command=button_div)

# display buttons
button_INST.grid(row = 6, column = 0,)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_clear.grid(row=6, column=2)
button_sub.grid(row=5, column=1)
button_mult.grid(row=5,column = 0)
button_div.grid(row=5, column = 2)

window.mainloop()