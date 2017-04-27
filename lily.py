from tkinter import *
from tkinter import ttk
canvas_width = 500
canvas_height = 500

def paint(event):
    python_green = "#476042"
    x, y = event.x,event.y
    x1, y1 = (event.x-3), (event.y-3)
    x2, y2 = (event.x+3), (event.y+3)
    w.create_rectangle(x1,y1,x2,y2,fill="red")
    
#define slopes    
    slopePerpendicular1 = -x/y
    slopePerpendicular2 = (500-x)/y
    slopePerpendicular3 = (x-500)/(500-y)
    slopePerpendicular4 = x/(500-y)

#define boundary points    
    y3 = y/2 + slopePerpendicular1*(-x/2)
    x3 = ((-y/2)/slopePerpendicular1)+x/2

    x4 = - y/(2*slopePerpendicular2) + (500+x)/2
    y4 = y/2 + slopePerpendicular2*(500 - (500+x)/2)

    x5 = (250+0.5*y)/slopePerpendicular3 + 250 + x
    y5 = (500+y)/2 + slopePerpendicular3*(250 - x/2)

    x6 = (250 - 0.5*y)/slopePerpendicular4 + x/2
    y6 = (500+y)/2 + slopePerpendicular4*(-x/2)

#find intersection
    
#create lines
    w.create_line(x3,0,0,y3,fill="white")
    w.create_line(x4,0,500,y4,fill="white")
    w.create_line(x5,500,500,y5,fill="white")
    w.create_line(x6,500,0,y6,fill = "white")

#define canvas   
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



