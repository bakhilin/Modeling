import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# read csv
path = os.path.abspath("/home/skull32/Modeling/data/data.csv")
data_df = pd.read_csv(path)
sequence = data_df["values"]
data = data_df["values"].values

# 1. Рассчёт математического ожидания, дисперсии, стандартного отклонения, коэффициента вариации

# среднее арифметическое (arithmetic mean)
mean = np.mean(data)
# дисперсия (variance)
# ddof = delta degrees of freedom (скорректированная дисперсия)
# т.е. если степень свободы 1, то мы корректируем выборку как / (n - 1)
variance = np.var(data, ddof=1)
# std = standard deviation (стандартное отклонение)
std_dev = np.std(data, ddof=1)
# коэффициент вариации
# |- показывает относительное отклонение данных от ср. значения в процентах
coef_variation = (std_dev / mean) * 100

# Доверительные интервалы для математического ожидания
# |- (с доверительными вероятностями 0.9, 0.95, 0.99)
confidence_intervals = {}
for confidence in [0.9, 0.95, 0.99]:
    ci = stats.t.interval(
        confidence, len(data) - 1, loc=mean, scale=std_dev / np.sqrt(len(data))
    )
    confidence_intervals[confidence] = ci


# Автокорреляционный анализ
lag_values = range(1, 11)  # Сдвиги от 1 до 10
autocorrelation_coeffs = [sequence.autocorr(lag) for lag in lag_values]

# Вывод значений коэффициентов автокорреляции
print("Коэффициенты автокорреляции со сдвигом от 1 до 10:")
for lag, coeff in zip(lag_values, autocorrelation_coeffs):
    print(f"Сдвиг {lag}: {coeff:.4f}")


