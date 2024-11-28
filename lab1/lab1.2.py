from math import *
import numpy as np
import matplotlib.pyplot as plt

# Визначення кількості точок (вузлів) на вісі x
N = 100

x0 = -4 * pi
xn = 4 * pi

# Обчислюємо крок між точками
dx = (xn - x0) / N

x = np.zeros(N, float)
y = np.zeros(N, float)
z = np.zeros(N, float)

x[0] = x0

n = 1
while n < N:
    x[n] = x[n-1] + dx

    temp = x[n]
    while True:
        if temp > pi:
            temp -= 2 * pi
        elif temp < -pi:
            temp += 2 * pi
        else:
            break

    if (temp > -pi) and (temp < 0):
        y[n] = -1/2
    elif (temp > 0) and (temp < pi):
        y[n] = 1/2
    n += 1

# Визначення кількості членів ряду Фур'є
Nf = 100

# Створюємо масиви для зберігання даних про функцію z(x)
b = np.zeros(Nf, float)
Fb = np.zeros(Nf, float)

# Обчислення коефіцієнтів b для ряду Фур'є
k = 1
while k < Nf:
    if k % 2 == 0:
        b[k] = 0
    else:
        b[k] = 2 / pi / k
    k += 1

# Заповнюємо z(x) відповідно до ряду Фур'є
n = 1
while n < N:
    x[n] = x[n-1] + dx
    z[n] = b[1] * sin(x[n])
    k = 2
    while k < Nf:
        z[n] = z[n] + b[k] * sin(k * x[n])
        k += 1

    n += 1

plt.plot(x, y, '--r') # Червона лінія - оригінальна функція (прямокутний імпульс)
plt.plot(x, z, '-b')  # Синя лінія - апроксимована функція

plt.title("Завдання 2")
plt.grid()

plt.show()