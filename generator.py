import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Параметры распределения
a1 = 406515.850962572
a2 =  0.76072506
q1 = 0.00017
q2 = 1-q1

# Генерация случайных чисел из экспоненциального распределения
generator1 = expon.rvs(scale=a1, loc=0, size=300)
generator2 = expon.rvs(scale=a2, loc=0, size=300)

# Генерация результата
result = [
    random.choice(generator1) if random.random() <= q1 else random.choice(generator2)
    for _ in range(300)
]

# Вывод результата
for value in result:
    print(value)

# Запись результата в файл
with open('random.txt', 'w') as file:
    for value in result:
        file.write(f"{value}\n")

# Построение графика
plt.figure(figsize=(10, 6))
plt.hist(result, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма значений')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()