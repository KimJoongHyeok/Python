from tkinter import *

class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("pack manager")

        Label(window,text = "blue",bg = "blue").pack()
        Label(window,text="red",bg="red").pack(fill = BOTH,expand = 1)
        Label(window,text="green",bg="green").pack(fill=BOTH)

        window.mainloop()
        
PackManagerDemo()
