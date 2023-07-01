from turtle import *
speed('fastest')
for i in range(10):

    pencolor('red')
    fd(100)
    lt(360/10)

    for i in range(10):
       pencolor('blue')
       fd(50)
       lt(360/10)
    

hideturtle()
mainloop()