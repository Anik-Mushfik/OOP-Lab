from tkinter import *

window = Tk()
window.geometry("400x600")
window.title("LOGIN")


lable_1 = Label(master=window, text="Login", font="Calibri 50 bold" )
lable_1.pack()

un_entry = Entry(master=window)
un_entry.pack()



window.mainloop()