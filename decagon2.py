from turtle import *
speed('fastest')
pencolor('red')
pensize(2)
for i in range(100):
    fd(100 - i)
    rt(36)
    circle(45,199)
    
hideturtle()
mainloop()