from turtle import *
speed('fastest')
pencolor('red')
pensize(2)
for i in range(200):
    fd(100 - i)
    rt(100)
    circle(46,180)
    dot(20,'blue')
    
hideturtle()
mainloop()