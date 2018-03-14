from turtle import *

mauu = ["red", "blue", "brown", "yellow", "grey"]
speed(-1)


for i in range(5):
    fillcolor(mauu[i])
    color(mauu[i])
    begin_fill()
    for j in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    forward(50)
    end_fill()

mainloop()
