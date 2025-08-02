from tkinter import *

root = Tk()
root.title("Daddy's Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def myClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def calc_add():
    global glob_num
    global sign
    sign = "add"
    glob_num = e.get()
    e.delete(0, END)

def calc_sub():
    global glob_num
    global sign
    sign = "sub"
    glob_num = e.get()
    e.delete(0, END)

def calc_mult():
    global glob_num
    global sign
    sign = "mult"
    glob_num = e.get()
    e.delete(0, END)

def calc_div():
    global glob_num
    global sign
    sign = "div"
    glob_num = e.get()
    e.delete(0, END)



def equal_func():
    equal_num = e.get()
    e.delete(0, END)

    if sign == "add":
        answer = int(glob_num) + int(equal_num)

    elif sign == "sub":
        answer = int(glob_num) - int(equal_num)

    elif sign == "mult":
        answer = int(glob_num) * int(equal_num)

    elif sign == "div":
        answer = int(glob_num) / int(equal_num)

    e.insert(0, answer)


def clear_func():
    e.delete(0, END)


    return
button_1 = Button(root, text="1", padx=35, pady=20, command= lambda: myClick(1))
button_2 = Button(root, text="2", padx=35, pady=20, command= lambda: myClick(2))
button_3 = Button(root, text="3", padx=35, pady=20, command= lambda: myClick(3))

button_4 = Button(root, text="4", padx=35, pady=20, command= lambda: myClick(4))
button_5 = Button(root, text="5", padx=35, pady=20, command= lambda: myClick(5))
button_6 = Button(root, text="6", padx=35, pady=20, command= lambda: myClick(6))

button_7 = Button(root, text="7", padx=35, pady=20, command= lambda: myClick(7))
button_8 = Button(root, text="8", padx=35, pady=20, command= lambda: myClick(8))
button_9 = Button(root, text="9", padx=35, pady=20, command= lambda: myClick(9))
button_0 = Button(root, text="0", padx=35, pady=20, command= lambda: myClick(0))

button_div = Button(root, text="/", padx=35, pady=20, command= calc_div)
button_mult = Button(root, text="x", padx=35, pady=20, command= calc_mult)
button_sub = Button(root, text="-", padx=35, pady=20, command= calc_sub)

button_equal = Button(root, text="=", padx=120, pady=20, command= equal_func)
button_add = Button(root, text="+", padx=34, pady=20, command= calc_add)
button_clear = Button(root, text="Clear", padx=109, pady=20, command= clear_func)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_div.grid(row=1, column=4)
button_mult.grid(row=2, column=4)
button_sub.grid(row=3, column=4)


button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=4)
button_equal.grid(row=5, column=1, columnspan=4)


root.mainloop()