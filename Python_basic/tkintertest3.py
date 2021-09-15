from tkinter import *

window=Tk()
window.title("test")

"""
label1 = Label(window,text="Name : ").grid(row=0,column=0,sticky=E)
label2 = Label(window,text="Password : ").grid(row=1,column=0,sticky=E)

entry1 = Entry(window,bg = "Yellow").grid(row=0,column=1)
entry2 = Entry(window,bg = "Green").grid(row=1,column=1)

#checkbox버튼
cbutton = Checkbutton(window,text="Remember name").grid(row=2,column=0,columnspan=2)
"""
"""
#slider -> Scale 이라는 함수 사용
slide1 = Scale(window,from_=0,to=100).pack()
"""

def newFile():
    print("this is new file")
def openFile():
    print("this is open")

#메뉴바 만들고 그 밑에 서브메뉴만들기
mainMenu = Menu(window)
window.configure(menu = mainMenu)

subMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=subMenu)

subMenu.add_command(label="New File",command=newFile)
#서브메뉴 사이에 줄긋기
subMenu.add_separator()
subMenu.add_command(label="Open",command=openFile)





window.mainloop()
