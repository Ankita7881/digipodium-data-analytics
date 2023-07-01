from turtle import *
speed('fastest')
color = ['red','purple',]
for i in range(6):
    pencolor('red')
    fd(100)
    for i in range(6):
        pencolor('blue')
        fd(50)
        for i in range (6):
           pencolor('green')
           fillcolor('yellow')
           begin_fill()
           fd(25)
           lt(360/6)
           end_fill()
        lt(360/6) 
    lt(360/6)

hideturtle()
mainloop()