import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Чтение данных из CSV файлов
path = os.path.abspath("/home/skull32/Modeling/data/random.txt")
data_df = pd.read_csv(path)
sequence = data_df["values"]

path1 = os.path.abspath("/home/skull32/Modeling/data/data.csv")
data_df1 = pd.read_csv(path1)
sequence1 = data_df1["values"]

# Строит график значений последовательности
plt.figure(figsize=(10, 5))
plt.plot(sequence, marker='o', label='Сгенерированная последовательность')
plt.plot(sequence1, marker='o', label='Заданная последовательность')
plt.title('График значений последовательностей')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.legend()
plt.grid()
plt.show()

