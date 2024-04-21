from tkinter import *

window = Tk()
window.geometry("300x300")



lab_1 = Label(window, text="ajgdk")
lab_2 = Label(window, text="fsig")
lab_1.pack(side="left", padx=20)
lab_2.pack(side="right", padx=20)
lab_3 = Label(window, text="ugafi")
lab_3.pack(side="bottom", pady=20)



window.mainloop()