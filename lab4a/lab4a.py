from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
from scipy.integrate import trapezoid

# Читання даних з файлів
text_file_flu = open("Hospital_14_FluTemp.csv", "r")
text_file_normal = open("Hospital_14_visitorsTemp.csv", "r")
flu = text_file_flu.readlines()
normal = text_file_normal.readlines()
text_file_flu.close()
text_file_normal.close()

DSize = [len(flu)-1, len(normal)-1]

# Ініціалізація масивів для даних про температуру та вік пацієнтів
FluDataTemp = np.zeros((DSize[0], 2))
NormalDataTemp = np.zeros((DSize[1], 2))
AgeFlu = np.zeros((DSize[0], 1))
AgeNormal = np.zeros((DSize[1], 1))

# Обробка даних про хворих
for i in range(1, DSize[0]):
    data_flu = flu[i].split(';')
    AgeFlu[i] = int(data_flu[1])
    FluDataTemp[i, 1] = float(data_flu[2])

# Обробка даних про здорових
for i in range(1, DSize[1]):
    data_normal = normal[i].split(';')
    AgeNormal[i] = int(data_normal[1])
    NormalDataTemp[i, 1] = float(data_normal[2])

# Сортуємо дані для подальшого аналізу
DataTempF = sorted(FluDataTemp[:, 1])
DataTempF[0] = DataTempF[1]
FluMeanTempN = np.mean(DataTempF)
FluStdTempN = np.std(DataTempF)
TF_min = min(DataTempF)
TF_max = max(DataTempF)

DataTempN = sorted(NormalDataTemp[:, 1])
DataTempN[0] = DataTempN[1]
NormalMeanTempN = np.mean(DataTempN)
NormalStdTempN = np.std(DataTempN)
TN_min = min(DataTempN)
TN_max = max(DataTempN)

print()
print('Average temperature of sick person h is ' + str(FluMeanTempN))
print('With standard deviation ' + str(FluStdTempN))
print('All the data on flu temperature is between ' + str(TF_min) + ' and ' + str(TF_max))

print("------------------------------------------------------------------------------------------")

print('Average temperature of healthy person h is ' + str(NormalMeanTempN))
print('With standard deviation ' + str(NormalStdTempN))
print('All the data on normal temperature is between ' + str(TN_min) + ' and ' + str(TN_max))

print("------------------------------------------------------------------------------------------")

# Побудова гістограми для порівняння температури у хворих та здорових
flu_histT, flu_bT = np.histogram(DataTempF, 8, density=True)
plt.hist(DataTempF, bins=flu_bT, alpha=0.5, density=True, color='red', label='Sick')

normal_histT, normal_bT = np.histogram(DataTempN, 8, density=True)
plt.hist(DataTempN, bins=normal_bT, alpha=0.5, density=True, color='blue', label='Healthy')

# Побудова функцій густини розподілу для нормального розподілу
mTN, sTN = stat.norm.fit(DataTempN)
mTF, sTF = stat.norm.fit(DataTempF)
xx = np.linspace(0.99 * TN_min, 1.1 * TF_max, 100)
yTN = stat.norm.pdf(xx, loc=mTN, scale=sTN)
yTF = stat.norm.pdf(xx, loc=mTF, scale=sTF)
plt.plot(xx, yTN, '-b', label='Healthy Distribution')
plt.plot(xx, yTF, '-r', label='Sick Distribution')

# Позначення величини температури, за якою вважається хворий або здоровий
TN_Edge = 37.0
xxEdge = [TN_Edge, TN_Edge]
yyEdge = [0, 0.8]
plt.plot(xxEdge, yyEdge, '-k', label='Temperature Threshold')

# Визначення областей під кривими густини розподілу
tN = np.linspace(0.99 * TN_min, TN_Edge, 100)
yTN = stat.norm.pdf(tN, loc=mTN, scale=sTN)
Pr11 = trapezoid(yTN, tN)

tF = np.linspace(TN_Edge, 1.1 * TF_max, 100)
yTF = stat.norm.pdf(tF, loc=mTF, scale=sTF)
Pr12 = trapezoid(yTF, tF)

tN = np.linspace(0.99 * TN_min, TN_Edge, 100)
yTN = stat.norm.pdf(tN, loc=mTN, scale=sTN)
tF = np.linspace(TN_Edge, 1.1 * TF_max, 100)
yTF = stat.norm.pdf(tF, loc=mTF, scale=sTF)

Pr21 = trapezoid(yTN, tN)
Pr22 = trapezoid(yTF, tF)

# Виведення ймовірностей правильного та помилкового прийняття рішення
print('Probability of correct decision for healthy person is ' + str(Pr11))
print('Probability of the mistake of 1st type "the healthy person with high temperature" is ' + str(Pr12))
print('Probability of correct decision for ill person is ' + str(Pr22))
print('Probability of the mistake of 2nd type "the ill person with low temperature" is ' + str(Pr21))

print("------------------------------------------------------------------------------------------")

# Розрахунок ризику та апріорного ризику
P1 = 0.15
C12 = 10
P2 = 0.15
C21 = 10
R = C12 * P1 * Pr12 + C21 * P2 * Pr21
print('The risk is ' + str(R))
print('The apriory risk for 1st mistake is ' + str(C12 * P1))
print('The apriory risk for 2nd mistake is ' + str(C21 * P2))
plt.legend()
plt.show()
