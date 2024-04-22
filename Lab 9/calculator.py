from tkinter import *

# Crreating the window
window = Tk()
window.geometry("390x400")
window.title("Calcutor")

# Creating the frames
result_frame = Frame(master=window, height=200, width=390, bg="gray", pady=20)
result_frame.pack()
button_frame = Frame(master=window)
button_frame.pack()


# Result
result_label = Label(master=result_frame, height=10, width=60, fg="black", bg="lavender")
result_label.pack()

# Button clicking function
def button_click():
    pass

def add_click():
    pass

def sub_click():
    pass

def mul_click():
    pass

def div_click():
    pass

def eql_click():
    pass


# Button creation
btn1 = Button(master=button_frame, text="1", height=2, width=12, command= lambda: button_click("1"))
btn2 = Button(master=button_frame, text="2", height=2, width=12, command= lambda: button_click("2"))
btn3 = Button(master=button_frame, text="3", height=2, width=12, command= lambda: button_click("3"))
btn4 = Button(master=button_frame, text="4", height=2, width=12, command= lambda: button_click("4"))
btn5 = Button(master=button_frame, text="5", height=2, width=12, command= lambda: button_click("5"))
btn6 = Button(master=button_frame, text="6", height=2, width=12, command= lambda: button_click("6"))
btn7 = Button(master=button_frame, text="7", height=2, width=12, command= lambda: button_click("7"))
btn8 = Button(master=button_frame, text="8", height=2, width=12, command= lambda: button_click("8"))
btn9 = Button(master=button_frame, text="9", height=2, width=12, command= lambda: button_click("9"))
btn0 = Button(master=button_frame, text="0", height=2, width=12, command= lambda: button_click("0"))

btn_plus = Button(master=button_frame, text="+", height=2, width=12, command= lambda: add_click())
btn_minus = Button(master=button_frame, text="-", height=2, width=12, command= lambda: sub_click())
btn_multiply = Button(master=button_frame, text="x", height=2, width=12, command= lambda: mul_click())
btn_division = Button(master=button_frame, text="/", height=2, width=12, command= lambda: div_click())
btn_equal = Button(master=button_frame, text="=", height=2, width=12, command= lambda: eql_click())


# Griding
result_label.grid(row=0, column=0, sticky="nsew")

btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=3, column=1)
btn8.grid(row=3, column=2)
btn9.grid(row=3, column=3)
btn0.grid(row=4, column=3)

btn_equal.grid(row=4, column=2)
btn_plus.grid(row=1, column=4)
btn_minus.grid(row=2, column=4)
btn_multiply.grid(row=3, column=4)
btn_division.grid(row=4, column=4)


window.mainloop()