import numpy as np
import matplotlib.pyplot as plt

N = 1000  # Загальна кількість спостережень

# Змінні визначають імовірності вибрації (K1), температури (K2) та загрязнення смазки (K3)
# поділені на підкатегорії (K11, K12, K13, K21, K22, K23, K31, K32)

PrK11_D1 = 0.7   # Імовірність вибрації в діапазоні 0.25-0.5 для ісправного подшипника
PrK12_D1 = 0.2   # Імовірність вибрації в діапазоні 0.5-0.75 для ісправного подшипника
PrK13_D1 = 0.1   # Імовірність вибрації в діапазоні >0.75 для ісправного подшипника
PrK11_D2 = 0.05  # Імовірність вибрації в діапазоні 0.25-0.5 для неісправного подшипника
PrK12_D2 = 0.15  # Імовірність вибрації в діапазоні 0.5-0.75 для неісправного подшипника
PrK13_D2 = 0.8   # Імовірність вибрації в діапазоні >0.75 для неісправного подшипника

PrK21_D1 = 0.8   # Імовірність температури в діапазоні 50-70°C для ісправного подшипника
PrK22_D1 = 0.1   # Імовірність температури в діапазоні 70-90°C для ісправного подшипника
PrK23_D1 = 0.1   # Імовірність температури в діапазоні >90°C для ісправного подшипника
PrK21_D2 = 0.07  # Імовірність температури в діапазоні 50-70°C для неісправного подшипника
PrK22_D2 = 0.08  # Імовірність температури в діапазоні 70-90°C для неісправного подшипника
PrK23_D2 = 0.85  # Імовірність температури в діапазоні >90°C для неісправного подшипника

PrK31_D1 = 0.9   # Імовірність загрязнення смазки в межах норми для ісправного подшипника
PrK32_D1 = 0.1   # Імовірність повишеного загрязнення смазки для ісправного подшипника
PrK31_D2 = 0.3   # Імовірність загрязнення смазки в межах норми для неісправного подшипника
PrK32_D2 = 0.7   # Імовірність повишеного загрязнення смазки для неісправного подшипника

# Створення масивів для зберігання ймовірностей.
PrKD = np.zeros((4, 4, 3))  # Тривимірний масив для зберігання ймовірностей для різних комбінацій.
PrD = np.zeros(4)  # Масив для зберігання ймовірностей станів об'єкта.
PrK_D = np.zeros(4)  # Масив для зберігання ймовірностей факторів K для кожного стану об'єкту.
PrD_K = np.zeros(4)  # Масив для зберігання ймовірностей стану об'єкта при наявності дефекту.

# Тривимірний масив ймовірностей для різних комбінацій
PrKD[1, 1, 1] = PrK11_D1
PrKD[1, 2, 1] = PrK12_D1
PrKD[1, 3, 1] = PrK13_D1
PrKD[1, 1, 2] = PrK11_D2
PrKD[1, 2, 2] = PrK12_D2
PrKD[1, 3, 2] = PrK13_D2

PrKD[2, 1, 1] = PrK21_D1
PrKD[2, 2, 1] = PrK22_D1
PrKD[2, 3, 1] = PrK23_D1
PrKD[2, 1, 2] = PrK21_D2
PrKD[2, 2, 2] = PrK22_D2
PrKD[2, 3, 2] = PrK23_D2

PrKD[3, 1, 1] = PrK31_D1
PrKD[3, 2, 1] = PrK32_D1
PrKD[3, 1, 2] = PrK31_D2
PrKD[3, 2, 2] = PrK32_D2

D = [0, 900, 100]  # Масив для зберігання кількості спостережень для кожного стану
K = [0, 2, 2, 2]  # Масив для зберігання номерів підкатегорій

# Обчислення ймовірностей станів об'єкта та ймовірностей факторів K для кожного стану об'єкту
for i in range(1, np.size(D)):
    PrD[i] = D[i] / N
    PrK_D[i] = PrKD[1, K[1], i]
    for j in range(2, np.size(K)):
        PrK_D[i] = PrK_D[i] * PrKD[j, K[j], i]

PrK = PrD[1] * PrK_D[1]

# Обчислення загальної ймовірності виходу за дефектом для подальших спостережень та додавання до загальної ймовірності (PrK)
for i in range(2, np.size(D)):
    PrK = PrK + PrD[i] * PrK_D[i]

# Обчислення ймовірностей стану об'єкта при наявності дефекту
for i in range(1, np.size(D)):
    PrD_K[i] = PrD[i] * PrK_D[i] / PrK

# Виведення інформації про признаки, за якими проводиться спостереження
print('При спостереженні:')
print(' вібрації у діапазоні 0,5-0,75g (ознака k12);')
print(' температурі у діапазоні 70-90°C (ознака k22);')
print(' забрудненні змащення вище норми (ознака k32).')

print('Ймовірність належного стану (діагноз D1) становить:')
print(f"{PrD_K[1]*100:.4f}%")
print('Ймовірність неналежного стану (діагноз D2) становить:')
print(f"{PrD_K[2]*100:.4f}%")

X = ['Належний стан', 'Неналежний стан']
Y = [round(PrD_K[1]*100, 4), round(PrD_K[2]*100, 4)]

plt.bar(X, Y, color=['green', 'red'])
plt.text(X[0], Y[0]/2, f'{Y[0]:.4f}%', ha='center', color='black', fontsize=10, fontweight='bold')
plt.text(X[1], Y[1]/2, f'{Y[1]:.4f}%', ha='center', color='black', fontsize=10, fontweight='bold')

plt.xlabel('Діагноз')
plt.ylabel('Ймовірність, %')
plt.title('Ймовірність діагнозу в залежності від стану')
plt.show()