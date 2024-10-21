import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import os

path = os.path.abspath("/home/skull32/Modeling/data/random.txt")
data_df = pd.read_csv(path)
sequence = data_df["values"]

path1 = os.path.abspath("/home/skull32/Modeling/data/data.csv")
data_df1 = pd.read_csv(path1)
sequence1 = data_df1["values"]

# Расчет коэффициента корреляции
correlation_coefficient, _ = pearsonr(sequence, sequence1)

# Вывод результатов
print(f"Коэффициент корреляции между сгенерированной последовательностью и заданной: {correlation_coefficient:.4f}")

# Визуализация
plt.scatter(sequence, sequence1, alpha=0.5)
plt.xlabel('Сгенерированная последовательность')
plt.ylabel('Заданная последовательность')
plt.title('Корреляционный анализ')
plt.grid()
plt.show()
