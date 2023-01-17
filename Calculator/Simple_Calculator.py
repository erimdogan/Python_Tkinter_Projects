from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=50)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_clicked(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    global number
    global math
    math = "add"
    first_number = entry.get()
    number = int(first_number)
    entry.delete(0, END)

def button_subtract():
    global number
    global math
    math = "subtract"
    first_number = entry.get()
    number = int(first_number)
    entry.delete(0, END)

def button_multiply():
    global number
    global math
    math = "multiply"
    first_number = entry.get()
    number = int(first_number)
    entry.delete(0, END)

def button_divide():
    global number
    global math
    math = "divide"
    first_number = entry.get()
    number = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "add":
        entry.insert(0, number + int(second_number))
    elif math == "subtract":
        entry.insert(0, number - int(second_number))
    elif math == "multiply":
        entry.insert(0, number * int(second_number))
    elif math == "divide":
        entry.insert(0, number / int(second_number))

# Define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command = lambda: button_clicked(1))
button_2 = Button(root, text="2", padx=40, pady=20, command = lambda: button_clicked(2))
button_3 = Button(root, text="3", padx=40, pady=20, command = lambda: button_clicked(3))
button_4 = Button(root, text="4", padx=40, pady=20, command = lambda : button_clicked(4))
button_5 = Button(root, text="5", padx=40, pady=20, command = lambda : button_clicked(5))
button_6 = Button(root, text="6", padx=40, pady=20, command = lambda : button_clicked(6))
button_7 = Button(root, text="7", padx=40, pady=20, command = lambda : button_clicked(7))
button_8 = Button(root, text="8", padx=40, pady=20, command = lambda : button_clicked(8))
button_9 = Button(root, text="9", padx=40, pady=20, command = lambda : button_clicked(9))
button_0 = Button(root, text="0", padx=40, pady=20, command = lambda : button_clicked(0))
button_addition = Button(root, text="+", padx=39, pady=20, command = lambda : button_add())
button_subtraction = Button(root, text="-", padx=39, pady=20, command = lambda : button_subtract())
button_multiplication = Button(root, text="*", padx=39, pady=20, command= lambda : button_multiply())
button_division = Button(root, text="/", padx=39, pady=20, command = lambda : button_divide())
button_equal = Button(root, text="=", padx=91, pady=20, command = button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command = button_clear)

# Put the buttons on the screen

button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_addition.grid(row=6, column=0)
button_subtraction.grid(row=6, column=1)
button_multiplication.grid(row=7, column=0)
button_division.grid(row=7, column=1)

button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)



root.mainloop()