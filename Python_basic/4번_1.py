#1행2행 열개수 다른경우
#import Tkinter toolkit
from tkinter import*

#main
window = Tk()
window.title("test")

def c():
    entered_text = entry.get()  
    output.delete(0.0, END)

def click():
    entered_text = entry.get()  
    output.delete(0.0, END)

def result():
    button+button


#Button widget
entry1 = Entry(window, width=20, bg="Yellow")
entry1.grid(row=0, column=1,columnspan=2)


button = Button(window, text="1",width=10,fg="black",bg="light gray").grid(row=1,column=0,sticky=W)             
button2 = Button(window, text="2",width=10,fg="black",bg="light gray").grid(row=1,column=1,sticky=W)
button3 = Button(window, text="3",width=10,fg="black",bg="light gray").grid(row=1,column=2,sticky=W)
button4 = Button(window, text="+",width=10,fg="black",bg="light gray").grid(row=1,column=3,sticky=W)

button5= Button(window, text="4",width=10,fg="black",bg="light gray").grid(row=2,column=0,sticky=W)             
button6 = Button(window, text="5",width=10,fg="black",bg="light gray").grid(row=2,column=1,sticky=W)
button7 = Button(window, text="6",width=10,fg="black",bg="light gray").grid(row=2,column=2,sticky=W)
button8 = Button(window, text="-",width=10,fg="black",bg="light gray").grid(row=2,column=3,sticky=W)

button9= Button(window, text="7",width=10,fg="black",bg="light gray").grid(row=3,column=0,sticky=W)             
button10 = Button(window, text="8",width=10,fg="black",bg="light gray").grid(row=3,column=1,sticky=W)
button11 = Button(window, text="9",width=10,fg="black",bg="light gray").grid(row=3,column=2,sticky=W)
button12 = Button(window, text="*",width=10,fg="black",bg="light gray").grid(row=3,column=3,sticky=W)

button13 = Button(window, text="C",width=10,fg="black",bg="light gray",command=c).grid(row=4,column=0,sticky=W)             
button14 = Button(window, text="0",width=10,fg="black",bg="light gray",command=result).grid(row=4,column=1,sticky=W)
button15 = Button(window, text="=",width=10,fg="black",bg="light gray").grid(row=4,column=2,sticky=W)
button16 = Button(window, text="/",width=10,fg="black",bg="light gray").grid(row=4,column=3,sticky=W)


window.mainloop() 
