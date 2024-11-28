import numpy as np
import matplotlib.pyplot as plt

B = ('Ascariasis', 'Hepatitis', 'Stones')
text_file1 = open("Ascariasis_var4.csv", "r")
text_file2 = open("Hepatitis_var4.csv", "r")
text_file3 = open("Stones_var4.csv", "r")

lin1 = text_file1.readlines()
text_file1.close()
lin2 = text_file2.readlines()
text_file2.close()
lin3 = text_file3.readlines()
text_file3.close()

D1Size = len(lin1)
Diagnose1 = D1Size - 1
D2Size = len(lin2)
Diagnose2 = D2Size - 1
D3Size = len(lin3)
Diagnose3 = D3Size - 1

# Створення масивів для симптомів для кожного захворювання
Sympthoms_1 = np.zeros((6, 4))  # Масив для симптомів Ascariasis
Sympthoms_2 = np.zeros((6, 4))  # Масив для симптомів Hepatitis
Sympthoms_3 = np.zeros((6, 4))  # Масив для симптомів Stones

# Обробка даних для Ascariasis
for i in range(1, D1Size):
    data = lin1[i].split(';')
    Age = int(data[0])
    vomit = data[1]
    yellowness = data[2]
    pain = data[3]
    liver = data[4]
    appetite = data[5]

    # Обробка симптомів віку
    if Age < 20:
        Sympthoms_1[0, 0] += 1
    elif (Age >= 20) and (Age < 40):
        Sympthoms_1[0, 1] += 1
    elif (Age >= 40) and (Age < 60):
        Sympthoms_1[0, 2] += 1
    else:
        Sympthoms_1[0, 3] += 1

    # Обробка симптомів блювоти
    if vomit == 'yes':
        Sympthoms_1[1, 0] += 1
    else:
        Sympthoms_1[1, 1] += 1

    # Обробка симптомів жовтушності
    if yellowness == 'eye':
        Sympthoms_1[2, 0] += 1
    elif yellowness == 'skin':
        Sympthoms_1[2, 1] += 1
    else:
        Sympthoms_1[2, 2] += 1

    # Обробка симптомів болю в правому підребер'ї
    if pain == 'yes':
        Sympthoms_1[3, 0] += 1
    else:
        Sympthoms_1[3, 1] += 1

    # Обробка симптомів збільшення печінки
    if liver == 'yes':
        Sympthoms_1[4, 0] += 1
    else:
        Sympthoms_1[4, 1] += 1

    # Обробка симптомів апетиту
    if appetite == 'yes\n':
        Sympthoms_1[5, 0] += 1
    else:
        Sympthoms_1[5, 1] += 1

# Обробка даних для Hepatitis
for i in range(1, D2Size):
    data = lin2[i].split(';')
    Age = int(data[0])
    vomit = data[1]
    yellowness = data[2]
    pain = data[3]
    liver = data[4]
    appetite = data[5]

    if Age < 20:
        Sympthoms_2[0, 0] += 1
    elif (Age >= 20) and (Age < 40):
        Sympthoms_2[0, 1] += 1
    elif (Age >= 40) and (Age < 60):
        Sympthoms_2[0, 2] += 1
    else:
        Sympthoms_2[0, 3] += 1

    if vomit == 'yes':
        Sympthoms_2[1, 0] += 1
    else:
        Sympthoms_2[1, 1] += 1

    if yellowness == 'eye':
        Sympthoms_2[2, 0] += 1
    elif yellowness == 'skin':
        Sympthoms_2[2, 1] += 1
    else:
        Sympthoms_2[2, 2] += 1

    if pain == 'yes':
        Sympthoms_2[3, 0] += 1
    else:
        Sympthoms_2[3, 1] += 1

    if liver == 'yes':
        Sympthoms_2[4, 0] += 1
    else:
        Sympthoms_2[4, 1] += 1

    if appetite == 'yes\n':
        Sympthoms_2[5, 0] += 1
    else:
        Sympthoms_2[5, 1] += 1
# Обробка даних для Stones
for i in range(1, D3Size):
    data = lin3[i].split(';')
    Age = int(data[0])
    vomit = data[1]
    yellowness = data[2]
    pain = data[3]
    liver = data[4]
    appetite = data[5]

    if Age < 20:
        Sympthoms_3[0, 0] += 1
    elif (Age >= 20) and (Age < 40):
        Sympthoms_3[0, 1] += 1
    elif (Age >= 40) and (Age < 60):
        Sympthoms_3[0, 2] += 1
    else:
        Sympthoms_3[0, 3] += 1

    if vomit == 'yes':
        Sympthoms_3[1, 0] += 1
    else:
        Sympthoms_3[1, 1] += 1

    if yellowness == 'eye':
        Sympthoms_3[2, 0] += 1
    elif yellowness == 'skin':
        Sympthoms_3[2, 1] += 1
    else:
        Sympthoms_3[2, 2] += 1

    if pain == 'yes':
        Sympthoms_3[3, 0] += 1
    else:
        Sympthoms_3[3, 1] += 1

    if liver == 'yes':
        Sympthoms_3[4, 0] += 1
    else:
        Sympthoms_3[4, 1] += 1

    if appetite == 'yes\n':
        Sympthoms_3[5, 0] += 1
    else:
        Sympthoms_3[5, 1] += 1

# Розрахунок ймовірностей захворювань для кожного набору симптомів
PrKD1 = Sympthoms_1 / Diagnose1
PrKD2 = Sympthoms_2 / Diagnose2
PrKD3 = Sympthoms_3 / Diagnose3

# Визначення симптомів для нового пацієнта та їх ймовірностей
Age_1 = 56
vomit_1 = 'no'
yellowness_1 = 'no'
pain_1 = 'yes'
liver_1 = 'yes'
appetite_1 = 'no'

# Визначення початкової ймовірності для кожного захворювання
PrD1 = 1 / 3

# Створення масивів для кожного симптому для нового пацієнта
ArAge_1 = np.zeros(3)
ArVomit_1 = np.zeros(3)
ArYellowness_1 = np.zeros(3)
ArPain_1 = np.zeros(3)
ArLiver_1 = np.zeros(3)
ArAppetite_1 = np.zeros(3)

# Обробка симптомів для нового пацієнта
if Age_1 < 20:
    ArAge_1[0] = PrKD1[0, 0]
    ArAge_1[1] = PrKD2[0, 0]
    ArAge_1[2] = PrKD3[0, 0]
elif (Age_1 >= 20) and (Age_1 < 40):
    ArAge_1[0] = PrKD1[0, 1]
    ArAge_1[1] = PrKD2[0, 1]
    ArAge_1[2] = PrKD3[0, 1]
elif (Age_1 >= 40) and (Age_1 < 60):
    ArAge_1[0] = PrKD1[0, 2]
    ArAge_1[1] = PrKD2[0, 2]
    ArAge_1[2] = PrKD3[0, 2]
else:
    ArAge_1[0] = PrKD1[0, 3]
    ArAge_1[1] = PrKD2[0, 3]
    ArAge_1[2] = PrKD3[0, 3]
print()

if vomit_1 == 'yes':
    ArVomit_1[0] = PrKD1[1, 0]
    ArVomit_1[1] = PrKD2[1, 0]
    ArVomit_1[2] = PrKD3[1, 0]
else:
    ArVomit_1[0] = PrKD1[1, 1]
    ArVomit_1[1] = PrKD2[1, 1]
    ArVomit_1[2] = PrKD3[1, 1]

if yellowness_1 == 'eye':
    ArYellowness_1[0] = PrKD1[2, 0]
    ArYellowness_1[1] = PrKD2[2, 0]
    ArYellowness_1[2] = PrKD3[2, 0]
elif yellowness_1 == 'skin':
    ArYellowness_1[0] = PrKD1[2, 1]
    ArYellowness_1[1] = PrKD2[2, 1]
    ArYellowness_1[2] = PrKD3[2, 1]
else:
    ArYellowness_1[0] = PrKD1[2, 2]
    ArYellowness_1[1] = PrKD2[2, 2]
    ArYellowness_1[2] = PrKD3[2, 2]

if pain_1 == 'yes':
    ArPain_1[0] = PrKD1[3, 0]
    ArPain_1[1] = PrKD2[3, 0]
    ArPain_1[2] = PrKD3[3, 0]
else:
    ArPain_1[0] = PrKD1[3, 1]
    ArPain_1[1] = PrKD2[3, 1]
    ArPain_1[2] = PrKD3[3, 1]

if liver_1 == 'yes':
    ArLiver_1[0] = PrKD1[4, 0]
    ArLiver_1[1] = PrKD2[4, 0]
    ArLiver_1[2] = PrKD3[4, 0]
else:
    ArLiver_1[0] = PrKD1[4, 1]
    ArLiver_1[1] = PrKD2[4, 1]
    ArLiver_1[2] = PrKD3[4, 1]

if appetite_1 == 'yes':
    ArAppetite_1[0] = PrKD1[5, 0]
    ArAppetite_1[1] = PrKD2[5, 0]
    ArAppetite_1[2] = PrKD3[5, 0]
else:
    ArAppetite_1[0] = PrKD1[5, 1]
    ArAppetite_1[1] = PrKD2[5, 1]
    ArAppetite_1[2] = PrKD3[5, 1]

# Розрахунок ймовірності кожного захворювання для нового пацієнта
PrKxD = np.zeros(3)
PrKx = 0
for i in range(0, 3):
    PrKxD[i] = ArAge_1[i] * ArVomit_1[i] * ArYellowness_1[i] * ArPain_1[i] * ArLiver_1[i] * ArAppetite_1[i]
    PrKx += PrKxD[i] * PrD1

# Розрахунок ймовірностей кожного захворювання для нового пацієнта
PrDKx = np.zeros(3)
for i in range(0, 3):
    PrDKx[i] = PrD1 * PrKxD[i] / PrKx

# Виведення ймовірностей кожного захворювання для нового пацієнта та найімовірнішого діагнозу
for i in range(0, 3):
    print(f'Ймовірність {B[i]}: {PrDKx[i]*100:.2f}%')

print('Найімовірніше те, що у хворого ', B[PrDKx.argmax()])

# Створення графіку
X = [1, 2, 3]
Y = [round(PrDKx[0] * 100, 2), round(PrDKx[1] * 100, 2), round(PrDKx[2] * 100, 2)]

colors = ['blue', 'green', 'red']

bars = plt.bar(X, Y, color=colors)

for bar, y, color in zip(bars, Y, colors):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{y}%', ha='center', color='black')
    plt.text(bar.get_x() + bar.get_width() / 2, -10, f'{y}', ha='center', color=color)

plt.xlabel('Діагнози')
plt.ylabel('Ймовірність певного діагнозу')

legend_labels = ['Ascariasis', 'Hepatitis', 'Stones']
plt.legend(bars, legend_labels, loc='upper left', bbox_to_anchor=(0, 1))

plt.show()