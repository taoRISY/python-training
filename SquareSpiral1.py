#  square spiral 1.1 - рисование 4цетной кадратной сприрали.
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
sides=eval(input("Введите число от 1 до 8: "))
colors = ["salmon","saddle brown","PaleVioletRed","plum1", "sea green", "silver", "sienna", "peru"] # переменная со списком цветов
for x in range(360):
    t.color(colors[x%sides]) # 0<=x<=100(range), x%sides(6) - результатом будет остаток от деления
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200) # толщина линии

