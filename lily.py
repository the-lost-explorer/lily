from tkinter import *
from tkinter import ttk
canvas_width = 500
canvas_height = 500

def paint(event):
    python_green = "#476042"
    x, y = event.x,event.y
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y-1)
    w.create_line(0,0,x1,y1,fill="blue")
    #w.create_line(0,500,x1,y1,fill="red")
    #w.create_line(500,0,x1,y1,fill="yellow")
    #w.create_line(500,500,x1,y1,fill="green")
    slopePerpendicular1= -x/y
    slopePerpendicular2= (500-x)/y
    slopePerpendicular3=  x/500-y
    slopePerpendicular4=  -(500-x)/(500-y) 
    
    y3 = y/2 + slopePerpendicular1*(-x/2)
    x3 = ((-y/2)/slopePerpendicular1)+x/2
    w.create_line(x3,0,0,y3,fill="green")

master = Tk()
master.title("Points")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height,bg="black")
w.pack(expand=YES, fill=BOTH)
w.bind("<Button-1>", paint)
message = Label(master, text="Click and choose a point")
message.pack(side=BOTTOM)

mainloop()

