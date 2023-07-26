import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors=["salmon","saddle brown","PaleVioletRed","plum1", "sea green", "silver", "sienna", "peru", "orange"]
sides = int(turtle.numinput("How many sides", "How many sides do you need? Write number from 1 to 8: "))
for x in range(100):
    t.color(colors[x%sides])
    t.circle(x)
    t.left(880)