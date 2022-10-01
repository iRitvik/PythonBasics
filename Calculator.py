#Calculator

from tkinter import *

master = Tk()
master.title("My Calculator")
master.geometry("300x490")
master.iconbitmap(r"C:\Users\ranar\Downloads\page_paper_file_document_text_note_icon_228151.ico")


e1 = Entry(master, width = 35, borderwidth= 5)
e1.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_clicked(number):
    a = e1.get()
    b = a + str(number)
    e1.delete(0, END)
    e1.insert(0, b)

def pressed_clear():
    e1.delete(0,END)

def pressed_operator(b):
    global num1
    global a
    a = b
    num1 = e1.get()
    e1.delete(0,END)




def pressed_equal():
    a = "mult"
    num1 = e1.get()
    num2 = e1.get()
    if (a == "add"):
        answer = int(num1) + int(num2)
    elif (a == "sub"):
        answer = int(num1) - int(num2)
    elif (a == "mult"):
        answer = int(num1) * int(num2)
    elif (a == "div"):
        answer = int(num1) / int(num2)

    e1.delete(0,END)
    e1.insert(0, answer)


b0 = Button(master, text = "0", padx = 40, pady = 20,command = lambda : button_clicked(0))
b1 = Button(master, text = "1", padx = 40, pady = 20,command = lambda : button_clicked(1))
b2 = Button(master, text = "2", padx = 40, pady = 20,command = lambda : button_clicked(2))
b3 = Button(master, text = "3", padx = 40, pady = 20,command = lambda : button_clicked(3))
b4 = Button(master, text = "4", padx = 40, pady = 20,command = lambda : button_clicked(4))
b5 = Button(master, text = "5", padx = 40, pady = 20,command = lambda : button_clicked(5))
b6 = Button(master, text = "6", padx = 40, pady = 20,command = lambda : button_clicked(6))
b7 = Button(master, text = "7", padx = 40, pady = 20,command = lambda : button_clicked(7))
b8 = Button(master, text = "8", padx = 40, pady = 20,command = lambda : button_clicked(8))
b9 = Button(master, text = "9", padx = 40, pady = 20,command = lambda : button_clicked(9))

b_equal = Button(master, text = '=', padx =91, pady = 20, command = pressed_equal)
b_add = Button(master, text = '+', padx =39, pady = 20, command = lambda : pressed_operator("add"))
b_clear = Button(master, text = 'Clear', padx =79, pady = 20, command = pressed_clear)
b_sub = Button(master, text = "-", padx = 40, pady = 20,command = lambda : pressed_operator("sub"))
b_mult = Button(master, text = "*", padx = 40, pady = 20,command = lambda : pressed_operator("mult"))
b_div = Button(master, text = "/", padx = 40, pady = 20,command = lambda : pressed_operator("div"))


#Geometry
b0.grid(row= 4)

b1.grid(row = 3, column = 0)
b3.grid(row = 3, column = 2)
b2.grid(row = 3, column = 1)

b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 2)
b6.grid(row = 2, column = 1)

b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)

b_equal.grid(row = 4, column=1, columnspan= 2)
b_clear.grid(row = 5,column=1, columnspan=2)
b_add.grid(row = 5,column=0)

b_sub.grid(row = 6, column = 0)
b_mult.grid(row = 6, column = 1)
b_div.grid(row = 6, column = 2)
master.mainloop()



#ico