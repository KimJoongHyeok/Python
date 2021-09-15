from tkinter import *

window=Tk()
window.title("test")

label=Label(window,text = "aaaa")
label.grid(row=0,column=0,sticky=W)

button1 = Button(window,text="this text is very vety very long",width=30,bg = "Yellow",fg="Blue")
button1.grid(row=0,column=0,sticky=W)

button2 = Button(window,text="Click",width=30,bg = "White",fg="Green")
button2.grid(row=0,column=1,sticky=E)

button3 = Button(window,text="cLICK2",width=30,bg = "WHITE",fg="Blue")
button3.grid(row=1,column=0,sticky=E)

button4 = Button(window,text="this text is very vety very long",width=30,bg = "Yellow",fg="Blue")
button4.grid(row=1,column=1,sticky=W)

#columnspan = 숫자 몇칸 차지할건지
button5 = Button(window,width=30,text="reset",fg = "Red",bg="blue")
button5.grid(row=2,column=1,columnspan=2,sticky=S)

#ENTRY = INPUT을 받아들이는 칸
entry1 = Entry(window,width=20,bg="Yellow")
entry2 = Entry(window,width=20,bg="Green")

entry1.grid(row=3,column=1)
entry2.grid(row=3,column=1)

#wrap 이란 띄어쓰기 하거나 줄바꿈할때 단어사이에 못띄우고 자리가 남더라도 단어단위로

window.mainloop()


