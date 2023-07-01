from turtle import *

for i in range(6):
    pencolor('red')
    fd(100)
    lt(360/6)

    for i in range(6):
       pencolor('blue')
       fd(50)
       lt(360/6)
    


hideturtle()
mainloop()