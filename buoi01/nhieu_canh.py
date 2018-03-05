from turtle import *


n = int(input("so canh? "))

shape("turtle")
# color("blue")
# speed(-1)
fillcolor("grey")

begin_fill()
for i in range(n):
    forward(100)
    left(360 / n)
end_fill()


mainloop()
