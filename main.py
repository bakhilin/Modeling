import numpy as np
import scipy.stats as stats

def confidence_interval(data, confidence=0.95):
    # Проверяем, что уровень доверия корректный
    if confidence not in [0.9, 0.95, 0.99]:
        raise ValueError("Уровень доверия должен быть 0.9, 0.95 или 0.99")
    
    # Вычисляем среднее и стандартную ошибку
    mean = np.mean(data)
    sem = stats.sem(data)
    
    # Находим критическое значение для заданного уровня доверия
    h = sem * stats.t.ppf((1 + confidence) / 2., len(data) - 1)
    
    # Вычисляем доверительный интервал
    lower_bound = mean - h
    upper_bound = mean + h
    
    # Возвращаем одно значение, например, среднее между нижней и верхней границей
    return (lower_bound + upper_bound) / 2

def calculate_mean(data):
    """Вычисляет математическое ожидание (среднее значение)"""
    return np.mean(data)

def calculate_variance(data):
    """Вычисляет дисперсию"""
    mean = calculate_mean(data)
    deviations = [(x - mean) ** 2 for x in data]
    variance = np.mean(deviations)
    return variance

def calculate_standard_deviation(data):
    # Вычисляем среднее значение
    mean = np.mean(data)
    # Вычисляем отклонения от среднего
    deviations = [(x - mean) ** 2 for x in data]
    # Вычисляем дисперсию
    variance = np.mean(deviations)
    # Возвращаем среднеквадратическое отклонение
    return variance ** 0.5

def coefficient_of_variation(data):
    # Вычисляем среднее и стандартное отклонение
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # Используем ddof=1 для выборочного стандартного отклонения
    
    # Проверяем, что среднее значение не равно нулю
    if mean == 0:
        raise ValueError("Среднее значение не должно быть равно нулю для вычисления коэффициента вариации.")
    
    # Вычисляем коэффициент вариации
    cv = (std_dev / mean) * 100  # Умножаем на 100 для получения процента
    return cv



def start():
    data_str = []
    with open('data.txt', 'r') as f:
        data_str = [line.strip() for line in f]
    data = [float(i) for i in data_str]
    count_data = [10, 20, 50, 100, 200, 300]
    
    for i in range(len(count_data)):
        print(f"мат ожидание {count_data[i]}:", calculate_mean(data[:count_data[i]]))
        print(f"дисперсия {count_data[i]}", calculate_variance(data[:count_data[i]]))
        print(f"С.К.О. {count_data[i]} %", calculate_standard_deviation(data[:count_data[i]]))
    
    # Доверительные интервалы
    for i in range(len(count_data)):
        print(f"Дов. интервал (0,9) {count_data[i]}", confidence_interval(data[:count_data[i]], confidence=0.9))
        print(f"Дов. интервал (0,95){count_data[i]}", confidence_interval(data[:count_data[i]], confidence=0.95))
        print(f"Дов. интервал (0,99){count_data[i]}", confidence_interval(data[:count_data[i]], confidence=0.99))

    for i in range(len(count_data)):
        print(f"Кэф вариации {count_data[i]}:", coefficient_of_variation(data[:count_data[i]]))

if __name__ == '__main__':
    start() 