from tkinter import *

window = Tk()
window.title("Canvas")

canvas = Canvas(window,width=400,height=400)
canvas.pack()

canvas.create_rectangle(50,50,150,150,fill="Blue")

canvas.create_line(0,0,400,400)

#원그리기
canvas.create_oval(100,100,250,250)

#polygon = 다각형
canvas.create_polygon(200,250,250,350,350,350,300,100,fill="Red")
