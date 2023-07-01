from turtle import *
speed('fastest')
colors = ['red','pink',]
bgcolor('black')
for i in range(6):
    pencolor('red')
    fd(150)
    for i in range(6):
        pencolor('blue')
        fd(100)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range (6):
           pencolor('green')
           fd(50)
           lt(360/6)
        end_fill()
    lt(360/6) 
    lt(360/6)

hideturtle()
mainloop()