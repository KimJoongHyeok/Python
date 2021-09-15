from tkinter import *

window = Tk()
window.title("my glossary")

def click():
    entered_text = entry1.get()
    print(entered_text)



label1=Label(window,text="Student ID")
label2=Label(window,text="Name")
label3=Label(window,text="Phone Number")

entry1 = Entry(window,width=20,bg="White")
entry2 = Entry(window,width=20,bg="White")
entry3 = Entry(window,width=20,bg="White")

label1.grid(row=0,column=0,sticky=E)
label2.grid(row=1,column=0,sticky=E)
label3.grid(row=2,column=0,sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)

Button(window,text="Submit",width=10,command=click).grid(row=3,column=1,sticky=S)


#입력받은값 eval로 계산하고 str로 바꾸고 계산하기 
def click2():
    entered_text2 = entry2.get()
    print(str(eval(entered_text2)))

Button(window,text="Submit2",width=10,command=click2).grid(row=4,column=1,sticky=S)

window.mainloop()
