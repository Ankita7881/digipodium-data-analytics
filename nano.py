from turtle import *

for i in range(9):
    speed('fastest')
    pencolor('red')
    fd(100)
    lt(360/9)

    for i in range(9):
      pencolor('blue')
      fd(50)
      lt(360/9)

      for i in range(9):
       pencolor('red')
      fd(20)
      lt(360/9)





hideturtle()
mainloop()