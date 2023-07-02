from turtle import *
speed('fastest')
bgcolor('black')
colors = ['red','green','yellow',
        'pink','sky blue','orange',
         'blue','purple','aqua']
i=0
while True:
    pencolor(colors[i%9])
    fd(10+i)
    lt(190)
    i+=1
hideturtle()
mainloop()