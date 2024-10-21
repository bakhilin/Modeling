import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import adfuller, acf

data = []
with open('data/data.txt', 'r') as f:
    data = [line.strip() for line in f]
data = [float(i) for i in data]

# Генерация случайного временного ряда (например, для ЧП)
np.random.seed(42)
data_length = 300
# data = np.random.poisson(lam=5, size=data_length)  # Генерация данных ЧП

# Создание DataFrame
df = pd.DataFrame(data, columns=['value'])

# Проверка на стационарность с помощью теста Дикки-Фуллера
result = adfuller(df['value'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

if result[1] <= 0.05:
    print("Ряд стационарен")
else:
    print("Ряд нестационарен")

# Вычисление коэффициентов автокорреляции для первых 10 лагов
k_ac = acf(df['value'], nlags=10)
print("nКоэффициенты автокорреляции (К-т АК) для первых 10 лагов:")
for lag, value in enumerate(k_ac):
    print(f"Лаг {lag}: {value:.4f}")

# Построение графика автокорреляции для 10 сдвигов
plt.figure(figsize=(12, 6))
plot_acf(df['value'], lags=10, ax=plt.gca())
plt.title('Автокорреляционная функция (ACF) для 10 сдвигов')
plt.xlabel('Лаг')
plt.ylabel('Автокорреляция')
plt.show()
