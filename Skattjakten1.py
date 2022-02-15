import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**3+y**2-6*x*y
def dfdx(x, y):
    return 3*x**2-6*y
def dfdy(x, y):
    return 2*y-6*x
def grad(x, y):
    return np.array([dfdx(x, y), dfdy(x, y)])

n = int(input("Antal steg = "))
s = float(input("Steglängd = "))

counter = 0
min = [[0, 0]]

for i in range(-100, 100):
    for j in range(-100, 100):
        x = i
        y = j

        print(counter)
        counter += 1

        for k in range(0, n):
            x = x - s * dfdx(x, y)
            y = y - s * dfdy(x, y)

            if x < -10**50 or x > 10**50 or y < -10**50 or y > 10**50:
                break

            if dfdx(x, y) > -10**-50 and dfdx(x, y) < 10**-50 and dfdy(x, y) > -10**-50 and dfdy(x, y) < 10**-50:
                print("Möjlig lokal minimumpunkt =", round(x, 2), round(y, 2), "           gradient =", grad(x, y))

                if min.count([x, y]) < 1:
                    min.append([x, y])

counter = 0
max = [[0, 0]]

for i in range(-100, 100):
    for j in range(-100, 100):
        x = i
        y = j

        print(counter)
        counter += 1

        for k in range(0, n):
            x = x + s * dfdx(x, y)
            y = y + s * dfdy(x, y)

            if x < -10**50 or x > 10**50 or y < -10**50 or y > 10**50:
                break

            if dfdx(x, y) > -10**-50 and dfdx(x, y) < 10**-50 and dfdy(x, y) > -10**-50 and dfdy(x, y) < 10**-50:
                print("Möjlig lokal maximumpunkt =", round(x, 2), round(y, 2), "           grad =", grad(x, y))

                if max.count([x, y]) < 1:
                    max.append([x, y])

print("potentiella minimumpunkter:", min)
print("potentiella maximumpunkter:", max)
print("Testa eventuell sadelpunkt:")
x = float(input("punkt x = "))
y = float(input("punkt y = "))
punktvarde = f(x, y)
print("funktionsvärde då x =", x, " y =", y, " ->", punktvarde)

x1 = x - 10**-14
y1 = y - 10**-14
for p in range(0, 21):
    print("x =", x1)
    print("y =", y1)
    x1 = round(x1 + 10**-15, 15)
    y1 = round(y1 + 10**-15, 15)
    print(f(x1, y1))

x2 = x + 10**-14
y2 = y - 10**-14
for p in range(0, 21):
    print("x =", x2)
    print("y =", y2)
    x2 = round(x2 - 10**-15, 15)
    y2 = round(y2 + 10**-15, 15)
    print(f(x2, y2))

x_1 = np.linspace(-20, 20, 50)
y_1 = np.linspace(-20, 20, 50)
X, Y = np.meshgrid(x_1, y_1)

Z = f(X, Y)
dZdx = dfdx(X, Y)
dZdy = dfdy(X, Y)

o_point_x = [0]
o_point_y = [0]
o_point_z = [f(o_point_x[0], o_point_y[0])]
g_point_x = [6]
g_point_y = [18]
g_point_z = [f(g_point_x[0], g_point_y[0])]

plt.figure(1)
ax1 = plt.axes(projection='3d')
ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

ax1.scatter(g_point_x[0: -2], g_point_y[0: -2], g_point_z[0: -2], c=g_point_z[0: -2], marker='o', cmap="Greens")
ax1.scatter(g_point_x[-1], g_point_y[-1], g_point_z[-1], c=g_point_z[-1], marker='o', cmap='Greens')

ax1.scatter(o_point_x, o_point_y, o_point_z, c=o_point_z, marker='o', cmap='Oranges')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

plt.figure("Partiella derivata x")
ax2 = plt.axes(projection='3d')
ax2.contour3D(X, Y, dZdx, 1000, cmap='binary')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('partiella derivata: x')

plt.figure("Partiella derivata y")
ax2 = plt.axes(projection='3d')
ax2.contour3D(X, Y, dZdy, 1000, cmap='binary')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('partiella derivata: y')

plt.show()