from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOK= Button(window,text="OK",fg="red",command=self.processOK)
        btCancel = Button(window,text="cancel",bg="yellow",command=self.processOK)
        btOK.pack()
        btCancel.pack()

        window.mainloop()

    def processOK(self):
        print("OK Button is clicked")

    def processCancel(self):
        print("Cancel button is clicked")

ProcessButtonEvent()
