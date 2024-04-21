from tkinter import *
 

myroot = Tk()
myroot.geometry('400x600') #width x height
myroot.title = "Calculator"
myroot.resizable(width=False, height=False)

#FRAMES
result_frame = Frame(myroot, height=100, width=390, highlightcolor="black", pady=20)
result_frame.pack()
button_frame = Frame(myroot)
button_frame.pack()

#RESULT
result_label = Label(result_frame,height=10, width=60, fg="black", bg="white")
result_label.pack()

#Numbers
btn1 = Button(button_frame,text= "1", height=2, width=12, command=lambda: buttonClick('1'))
btn2 = Button(button_frame,text=  "2", height=2, width=12, command=lambda: buttonClick('2'))
btn3 = Button(button_frame,text=  "3", height=2, width=12, command=lambda: buttonClick('3'))
btn4 = Button(button_frame,text=  "4", height=2, width=12, command=lambda: buttonClick('4'))
btn5 = Button(button_frame,text=  "5", height=2, width=12, command=lambda: buttonClick('5'))
btn6 = Button(button_frame,text=  "6", height=2, width=12, command=lambda: buttonClick('6'))
btn7 = Button(button_frame,text=  "7", height=2, width=12, command=lambda: buttonClick('7'))
btn8 = Button(button_frame,text=  "8", height=2, width=12, command=lambda: buttonClick('8'))
btn9 = Button(button_frame,text=  "9", height=2, width=12, command=lambda: buttonClick('9'))
btn0 = Button(button_frame,text=  "0", height=2, width=12, command=lambda: buttonClick('0'))

plus = Button(button_frame, text= '+', height=2, width=12, command=lambda: plusButtonClick())
minus = Button(button_frame, text= '-', height=2, width=12)
multiply = Button(button_frame, text= 'x', height=2, width=12)
divide = Button(button_frame, text= '/', height=2, width=12)
equal = Button(button_frame, text='=', height=2, width=12, command= lambda: equalButtonClick())

result_label.grid(row=0, column=0, sticky="nsew")

btn1.grid(row=1, column=1 , sticky="nsew")
btn2.grid(row=1, column=2 , sticky="nsew")
btn3.grid(row=1, column=3 , sticky="nsew")
btn4.grid(row=2, column=1 , sticky="nsew")
btn5.grid(row=2, column=2 , sticky="nsew")
btn6.grid(row=2, column=3 , sticky="nsew")
btn7.grid(row=3, column=1 , sticky="nsew")
btn8.grid(row=3, column=2 , sticky="nsew")
btn9.grid(row=3, column=3 , sticky="nsew")
btn0.grid(row=4, column=2 , sticky="nsew")

plus.grid(row=1, column=4 , sticky="nsew")
minus.grid(row=2, column=4 , sticky="nsew")
multiply.grid(row=3, column=4 , sticky="nsew")
divide.grid(row=4, column=3 , sticky="nsew")
equal.grid(row=4, column=4, sticky="nsew")

a = 0
b = 0
input_stream = ''
operator_pressed = False

def buttonClick(txt):
    global input_stream
    global a
    global b
    if(operator_pressed):
        input_stream += txt
        result_label.config(text=int(input_stream))
        
        b = int(input_stream)
    else:
        input_stream += txt
        result_label.config(text=int(input_stream))
        
        a = int(input_stream)

def plusButtonClick():
    global operator_pressed
    operator_pressed = True
    global input_stream
    input_stream = ''

def equalButtonClick():
    print(a)
    print(b)

myroot.mainloop()
 