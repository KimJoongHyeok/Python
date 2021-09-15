
#tkinter 필수 3줄

from tkinter import *

window = Tk()
window.title("my glossary")
#  윈도우 사이즈 window.geometry("500 * 500")

label = Label(window,text = "this is the first label")
#label.grid(row=0, column=0, sticky=w)
label.pack()

label2 = Label(window,text = "this is the seconde label")
label2.pack()

#버튼
button1 = Button(window,text = "This text is very very very long",fg="Blue",bg="Yellow")
button1.grid(row=0,column=0,sticky=W)

button2 = Button(window,text="Click2",bg="white",fg="Green")
button2.grid(row=0,column=0,sticky=W)


window.mainloop()
