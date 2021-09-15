from tkinter import *
import time

window = Tk()
window.title("Animation")

canvas = Canvas(window,width=400,height=400)
canvas.pack()

canvas.create_polygon(50,100,50,150,100,125)
canvas.create_polygon(50,200,50,250,100,225)
canvas.create_oval(350,200,400,250)
message = Label(window,text = "message")

for i in range(0,50):
    canvas.move(1,5,0)
    canvas.move(2,10,0) # canvas.move(몇번째, x축으로 몇만큼 , y축으로 몇만큼)
    canvas.move(3,-5,0)
    message.move(1,5,0)
    window.update()
    time.sleep(0.1)




window.mainloop()
