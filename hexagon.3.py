from turtle import *
speed('fastest')
pencolor('red')
pensize(2)
for i in range(200):
    fd(200 - i)
    rt(60)
    circle(20,40)
    dot(30,'blue')
    
hideturtle()
mainloop()