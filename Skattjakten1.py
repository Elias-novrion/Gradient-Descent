import numpy as np

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

x1 = x - 0.0000001
y1 = y - 0.0000001
for p in range(0, 21):
    print("x =", x1)
    print("y =", y1)
    x1 = round(x1 + 0.00000001, 8)
    y1 = round(y1 + 0.00000001, 8)
    print(f(x1, y1))

x2 = x + 0.0000001
y2 = y - 0.0000001
for p in range(0, 21):
    print("x =", x2)
    print("y =", y2)
    x2 = round(x2 - 0.00000001, 8)
    y2 = round(y2 + 0.00000001, 8)
    print(f(x2, y2))

