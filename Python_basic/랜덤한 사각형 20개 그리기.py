from tkinter import *
import random

window = Tk()
window.title("Random Rectangles")

canvas = Canvas(window,width=400,height=400)
canvas.pack()

def randomRects(num):
    for i in range(0,num):
        x1 = random.randrange(200)
        y1 = random.randrange(200)
        x2 = x1 + random.randrange(200)
        y2 = y1 + random.randrange(200)
        canvas.create_rectangle(x1,y1,x2,y2)
        #create_oval,polygon 가능
        
        
randomRects(20)
