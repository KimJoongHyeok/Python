from tkinter import *

window = Tk()
window.title("Loan Calculator")

label1 = Label(window,text = "Annual Interest Rate")
label2 = Label(window,text = "Number of Years")
label3 = Label(window,text = "Loan Amount")
label4 = Label(window,text = "Monthly Payment")
label5 = Label(window,text = "Total Payment")

label1.grid(row=1,column=1,sticky = W)
label2.grid(row=2,column=1,sticky = W)
label3.grid(row=3,column=1,sticky = W)
label4.grid(row=4,column=1,sticky = W)
label5.grid(row=5,column=1,sticky = W)

entry1 = Entry(window,bg = "white")
entry2 = Entry(window,bg = "white")
entry3 = Entry(window,bg = "white")

entry1.grid(row=1,column = 2)
entry2.grid(row=2,column = 2)
entry3.grid(row=3,column = 2)

label6 = Label(window,text="")
label7 = Label(window,text="")

label6.grid(row=4,column=2)
label7.grid(row=5,column=2)

button = Button(window,text="Compute Payment")
button.grid(row=6,column=2,sticky=E)


window.mainloop()
