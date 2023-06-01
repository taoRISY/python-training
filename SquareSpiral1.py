#  square spiral 1.1 - рисование 4цетной кадратной сприрали.
import turtle
t = turtle.Pen()
colors = ["salmon","saddle brown","PaleVioletRed","plum1"] # переменная со списком цветов
for x in range(100):
    t.color(colors[x%4])
    t.forward(x)
    t.left(91)
