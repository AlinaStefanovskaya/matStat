from math import *
import numpy as np
import matplotlib.pyplot as plt

# Визначення кількості точок (вузлів) на вісі x
N = 100

x0 = -2 * pi
xn = 2 * pi

# Обчислюємо крок між точками
dx = (xn - x0) / N

x = np.zeros(N, float)
y = np.zeros(N, float)
z = np.zeros(N, float)

x[0] = x0

# Визначення кількості членів ряду Фур'є
Nf = 100

# Створюємо масиви для зберігання даних про функцію z(x)
b = np.zeros(Nf, float)
Fb = np.zeros(Nf, float)

# Обчислення коефіцієнтів b для ряду Фур'є
k = 1
while k < Nf:
    b[k] = -2 * (pow(-1, k) / k)
    k += 1

# Задання функції y(x) - сигнал у вигляді піли
n = 1
while n < N:
    x[n] = x[n-1] + dx
    y[n] = (x[n] - pi) % (2 * pi) - pi
    n += 1

# Обчислення значень апроксимованої функції z(x) за допомогою ряду Фур'є
n = 1
while n < N:
    z[n] = b[1] * sin(x[n])  # Перший член ряду Фур'є
    k = 2
    while k < Nf:
        z[n] = z[n] + b[k] * sin(k * x[n])
        k += 1
    n += 1

plt.plot(x, y, '--r')  # Червона лінія - оригінальна функція y(x) = x
plt.plot(x, z, '-b')   # Синя лінія - апроксимована функція з ряду Фур'є

plt.grid()
plt.title("Завдання 3")

plt.show()