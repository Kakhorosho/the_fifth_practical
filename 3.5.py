import turtle as t

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

t.penup()
t.goto(xc, yc - r)
t.pendown()
t.circle(r)

t.penup()
t.goto(x, y)
t.pendown()
t.pencolor('red')
t.begin_fill()
t.fillcolor('red')
t.circle(2)
t.end_fill()

if (x - xc)**2 + (y - yc)**2 < r**2:
    print('Точка внутри окружности')
elif (x - xc)**2 + (y - yc)**2 == r**2:
    print('Точка лежит на окружности')
else:
    print('Точка вне окружности')
