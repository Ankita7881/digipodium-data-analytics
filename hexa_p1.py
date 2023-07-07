from turtle import *

# function definition
def hexagon(size,color='red'):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        fd(size)
        rt(60)
    end_fill()

hexagon(100)  #calling
hexagon(60)
hideturtle()
mainloop()
