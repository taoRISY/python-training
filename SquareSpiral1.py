#  square spiral 1.2 - цветная спираль из имени.
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["salmon", "sea green", "silver", "sienna"] # переменная со списком цветов

# всплывающее окно запрашивающие имя пользователя
your_nane=turtle.textinput("Введите свое имя","Как вас зовут?")

# Отрисовка спирали из имени пользователя
for x in range(100):
    t.color(colors[x%4])
    t.penup() # не рисовать "обычные" линии
    t.forward(x*4)
    t.pendown()
    t.write(your_nane, font=("Arial", int((x+4)/4), "bold")) # написать имя пользователя, увеличивая шрифт
    t.left(92)

