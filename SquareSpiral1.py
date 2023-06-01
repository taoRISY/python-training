#  square spiral 1.1 - рисование 4цетной кадратной сприрали.
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["salmon","saddle brown","PaleVioletRed","plum1"] # переменная со списком цветов
for x in range(100):
    t.color(colors[x%4]) # 0<=x<=100(range), x%4 - результатом будет остаток от деления. За 100 итераций цикла мы "пройдем" каждый цвет 25 раз
    t.circle(x)
    t.left(91)
