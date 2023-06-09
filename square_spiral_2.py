#  square spiral 2.0 - цветная спираль - numinput funktion
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors=["salmon","saddle brown","PaleVioletRed","plum1", "sea green", "silver", "sienna", "peru", "orange"] # переменная со списком цветов
# задаем количество сторон
sides=int(turtle.numinput("Сколько сторон", "Задайте количество сторон (1-8)", 4, 1, 8))
for x in range(360):
    t.color(colors[x%sides])
    t.forward(x*3/sides+x) # изменить размер в соотвецтвии с к-вом сторон
    t.left(360/sides+1) 
    t.width(x*sides/200) # увеличить толщину линии по мере движения во внешнюю сторону

