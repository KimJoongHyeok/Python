from tkinter import *
def click1():
    print("This is New File")

def click2():
    print("This is Open File")

def click3():
    print("This is Save File")

def click4():
    print("This is Save As File")

def click5():
    print("This is Undo File")

def click6():
    print("This is Redo... File")

def click7():
    print("This is Cut File")

def click8():
    print("This is Copy File")





window =  Tk()
window.title("Drop Down")

mainMenu1 = Menu(window)

window.configure(menu = mainMenu1)

subMenu = Menu(mainMenu1)
ssubMenu1 = Menu(subMenu)
ssubMenu2 = Menu(subMenu)
ssubMenu3 = Menu(subMenu)
ssubMenu4 = Menu(subMenu)
ssubMenu5 = Menu(subMenu)
ssubMenu6 = Menu(subMenu)
ssubMenu7 = Menu(subMenu)
ssubMenu8 = Menu(subMenu)

mainMenu1.add_cascade(label = "File", menu = subMenu)
subMenu.add_cascade(label = "New File", menu = ssubMenu1)
subMenu.add_cascade(label = "Open...", menu = ssubMenu2)
subMenu.add_separator()
subMenu.add_cascade(label = "Save", menu = ssubMenu3)
subMenu.add_cascade(label = "Save As ...", menu = ssubMenu4)



subMenu = Menu(mainMenu1)
mainMenu1.add_cascade(label = "Edit", menu = subMenu)
subMenu.add_cascade(label = "Undo", menu = ssubMenu5)
subMenu.add_cascade(label = "Redo...", menu = ssubMenu6)
subMenu.add_separator()
subMenu.add_cascade(label = "Cut", menu = ssubMenu7)
subMenu.add_cascade(label = "Copy", menu = ssubMenu8)

ssubMenu1.add_command(label = "Test", command = click1)
ssubMenu2.add_command(label = "Test", command = click2)
ssubMenu3.add_command(label = "Test", command = click3)
ssubMenu4.add_command(label = "Test", command = click4)
ssubMenu5.add_command(label = "Test", command = click5)
ssubMenu6.add_command(label = "Test", command = click6)
ssubMenu7.add_command(label = "Test", command = click7)
ssubMenu8.add_command(label = "Test", command = click8)

window.mainloop()
