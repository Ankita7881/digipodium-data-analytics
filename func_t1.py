from turtle import *

def square(size,color='red'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()
def hexagon(size,color='yellow'):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        fd(size)
        rt(60)
    end_fill()

square(100,'blue')  #calling
square(60,'green')
hexagon(100,'pink')
hexagon(60,'sky blue')
square(25,'yellow')

hideturtle()
mainloop()
    

