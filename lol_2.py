#  square spiral 1.2 - цветная спираль из имени.
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["salmon", "sea green", "silver", "sienna", "blue", "green", "red", "brown"] # переменная со списком цветов
sides = int(turtle.numinput("How many sides", "How many sides do you need? Write number from 1 to 8: "))
# всплывающее окно запрашивающие имя пользователя
your_nane=turtle.textinput("Введите свое имя","Как вас зовут?")

# Отрисовка спирали из имени пользователя
for x in range(360):
    t.color(colors[x%sides])
    t.penup() # не рисовать "обычные" линии
    t.forward(x*3/sides+x)
    t.pendown()
    t.write(your_nane, font=("Arial", int((x+sides)/sides), "bold")) # написать имя пользователя, увеличивая шрифт
    t.left(360/sides+1)
    t.width(x*sides/200)

