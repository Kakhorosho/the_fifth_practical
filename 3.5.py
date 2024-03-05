import matplotlib.pyplot as plt

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

fig, ax = plt.subplots()

plt.xlim(xc - 80, xc + 80)
plt.ylim(yc - 80, yc + 80)
c = plt.Circle((xc, yc,), r, color='k', fill=False)
dot = plt.Circle((x, y), 2, color='red')
plt.grid(linestyle='dotted')

ax.set_aspect(1)

ax.add_artist(c)
ax.add_artist(dot)

if (x - xc)**2 + (y - yc)**2 < r**2:
    plt.title('Точка внутри окружности', fontsize=8, color='red')
elif (x - xc)**2 + (y - yc)**2 == r**2:
    plt.title('Точка лежит на окружности', fontsize=8, color='red')
else:
    plt.title('Точка вне окружности', fontsize=8, color='red')

plt.show()
