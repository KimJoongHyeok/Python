from tkinter import *

window =Tk()
window.title("My glossary")

def click():
    entered_text = entry.get()
    output.delete(0.0,END)
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word"
    output.insert(END,definition)


Label(window,text="Enter the word you want defining:").grid(row=0,column=0,sticky=W)

entry = Entry(window,width = 20,bg="Lightgreen")
entry.grid(row=1,column=0,sticky=W)

Button(window,text = "submit",width=5,command = click).grid(row=2,column=0,sticky=W)

Label(window,text="\nDefinition: ").grid(row=3,column=0,sticky=W)

output = Text(window,width=30,height=5,wrap=WORD,bg="light green")
output.grid(row=4,column=0,columnspan=2,sticky=W)

my_glossary = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five'
    }


window.mainloop()
