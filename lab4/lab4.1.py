from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *
import scipy.stats as stat
import scipy.special as spec

text_file = open("ZNO_var14.csv", "r")
lin = text_file.readlines()
text_file.close()

N = len(lin) - 1
Age = np.zeros(N)
Mark = np.zeros(N)

# Цикл для обробки даних з файлу
for num_repeats in range(2, 6):
    # Лічильник для кількості випадків, коли бал дорівнює 200
    k = 0

    # Цикл для обробки даних в кожному рядку
    for i in range(1, N):
        data = lin[i].split(";")
        Age[i] = int(data[1])
        Mark[i] = int(data[num_repeats])

        if Mark[i] == 200:
            k += 1

    # Обробка випадку, коли бал дорівнює 200
    Age[0] = Age[1]
    Mark[0] = Mark[1]

    Age = sorted(Age)
    Age_max = Age[N - 1]
    Age_min = Age[1]

    min = str(Age_min)
    max = str(Age_max)

    # Виведення інформації про предмет залежно від значення num_repeats
    if num_repeats == 2:
        subject_name = "Math"
    elif num_repeats == 3:
        subject_name = "UA_lang"
    elif num_repeats == 4:
        subject_name = "English"
    else:
        subject_name = "Physics"

    print(f"{subject_name}:")
    print("The age of students is between (", min, ", ", max, ")")

    # Обчислення статистичних параметрів
    MeanGrade = np.mean(Mark)
    stdGrade = np.std(Mark)
    MedianGrade = np.median(Mark)
    LPercentileGrade = np.percentile(Mark, 5)
    RPercentileGrade = np.percentile(Mark, 95)

    # Виведення інформації про бали студентів
    print("Average students grade on math is " + str(MeanGrade))
    print("with standard deviation " + str(stdGrade))
    print("the median of distribution is " + str(MedianGrade))
    print("the 5% persentile of distribution is " + str(LPercentileGrade))
    print("the 95% persentile of distribution is " + str(RPercentileGrade))

    l = plt.plot(Age, Mark, 'ro')
    plt.setp(l, markersize=10)

    MeanArr = np.zeros(N) + MeanGrade
    MedArr = np.zeros(N) + MedianGrade
    stdArr = np.zeros(N) + stdGrade
    LPArr = np.zeros(N) + LPercentileGrade
    RPArr = np.zeros(N) + RPercentileGrade

    plt.plot(Age, MeanArr, 'r-', lw=3)
    plt.plot(Age, MedArr, 'b-', lw=1)

    plt.plot(Age, LPArr, 'g:', lw=1)
    plt.plot(Age, RPArr, 'g:', lw=1)

    plt.plot(Age, MeanArr + stdArr, 'b:', lw=1)
    plt.plot(Age, MeanArr - stdArr, 'b:', lw=1)

    plt.title(f'{subject_name} Distribution')
    plt.show()

    Mark = sorted(Mark)
    Math_max = Mark[N - 1]
    Math_min = Mark[1]

    # Визначення кількості інтервалів гістограми
    k = round(N ** 0.5)

    d = (Math_max - Math_min) / k
    dell = (Math_max - Math_min) / 20
    xl = Age_min - dell
    xr = Math_max + dell

    # Розрахунок гістограми та її побудова
    histogr, b = np.histogram(Mark, k, density=True)
    plt.hist(Mark, bins=b, density=True)

    # Побудова графіку нормального розподілу за середнім та стандартним відхиленням
    xx = np.linspace(Math_min, Math_max, 100)
    Mx = MeanGrade
    Sx = stdGrade

    y = ((1 / (np.sqrt(2 * np.pi) * Sx)) * np.exp(-0.5 * (1 / Sx * (xx - Mx)) ** 2))
    plt.plot(xx, y, "-r")

    # Побудова графіку гамма-розподілу за параметрами, які визначаються fit
    a, dd, p = stat.gamma.fit(Mark)
    yy = 1 / spec.gamma(a) / p ** a * (xx - dd) ** (a - 1) * np.exp(-(xx - dd) / p)
    plt.plot(xx, yy, "-g")

    # Побудова графіку гамма-розподілу за явно визначеними параметрами
    yyy = gamma.pdf(xx, a=a, loc=dd, scale=p)
    plt.plot(xx, yyy, '--c')

    # Ініціалізація масивів для очікуваних частот
    exp_freqG = np.zeros(k)
    exp_freqN = np.zeros(k)

    # Розрахунок очікуваних частот для гамма- та нормального розподілів
    for i in range(0, k):
        exp_freqG[i] = gamma.cdf(Math_min + (i + 1) * d, a=a, loc=dd, scale=p) - gamma.cdf(Math_min + i * d, a=a, loc=dd, scale=p)
        exp_freqN[i] = norm.cdf(Math_min + (i + 1) * d, Mx, Sx) - norm.cdf(Math_min + i * d, Mx, Sx)

    # Розрахунок спостережуваних частот
    obs_freq = (histogr * d)

    # Розрахунок хі-квадрат для гамма-розподілу та нормального розподілу
    xPirsonG = 0
    xPirsonN = 0

    for i in range(0, k):
        xPirsonG += (obs_freq[i] - obs_freq[i] * exp_freqG[i]) ** 2 / (obs_freq[i] * exp_freqG[i])
        xPirsonN += (obs_freq[i] - obs_freq[i] * exp_freqN[i]) ** 2 / (obs_freq[i] * exp_freqN[i])

    # Виведення результатів тесту хі-квадрат для гамма-розподілу
    print()
    print("X^2 for Gamma = " + str(xPirsonG))
    if xPirsonG > 0.1:
        print("Відмінності між досліджуваними рядами потрібно вважати істотними, тобто гіпотеза не приймається")
    else:
        print("Розбіжності вважаються випадковими і гіпотеза приймається")

    # Виведення результатів тесту хі-квадрат для нормального розподілу
    print()
    print("X^2 for Norm = " + str(xPirsonN))
    if xPirsonN > 0.1:
        print("Відмінності між досліджуваними рядами потрібно вважати істотними, тобто гіпотеза не приймається")
    else:
        print("Розбіжності вважаються випадковими і гіпотеза приймається")

    plt.title(f'{subject_name} Histogram and Distribution')
    plt.show()
