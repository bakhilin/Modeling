import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def confidence_interval(data, confidence=0.95):
    # Проверяем, что уровень доверия корректный
    if confidence not in [0.9, 0.95, 0.99]:
        raise ValueError("Уровень доверия должен быть 0.9, 0.95 или 0.99")

    # Вычисляем среднее и стандартную ошибку
    sem = stats.sem(data)
    # Находим критическое значение для заданного уровня доверия
    h = sem * stats.t.ppf((1 + confidence) / 2, len(data) - 1)

    # Возвращаем одно значение, например, среднее между нижней и верхней границей
    return h


def calculate_mean(data):
    """Вычисляет математическое ожидание (среднее значение)"""
    return np.mean(data)


def calculate_variance(data):
    """Вычисляет дисперсию"""
    mean = calculate_mean(data)
    deviations = [(x - mean) ** 2 for x in data]
    variance = np.sum(deviations) / (len(data) - 1)
    return variance


def calculate_standard_deviation(data):
    """Вычисляет среднее квадратическое отклонение (СКО)"""
    variance = calculate_variance(data)
    return np.sqrt(variance)


def coefficient_of_variation(data):
    """Вычисляет коэффициент вариации (%)"""
    mean = calculate_mean(data)
    std_dev = calculate_standard_deviation(data)  # Выборочное СКО
    if mean == 0:
        raise ValueError("Среднее значение не должно быть равно нулю для вычисления коэффициента вариации.")
    cv = (std_dev / mean) * 100  # В процентах
    return cv


def relative_deviation(calculated, reference):
    """
    Вычисляет относительное отклонение (%) между рассчитанным и эталонным значениями.
    Формула:
    (|calculated - reference| / |reference|) * 100%
    """
    if reference == 0:
        raise ValueError("Эталонное значение не должно быть равно нулю для вычисления относительного отклонения.")
    return (abs(calculated - reference) / abs(reference)) * 100


def plot_data(data):
    """Строит график значений последовательности."""
    plt.figure(figsize=(10, 5))
    plt.plot(data, marker='o')
    plt.title('График значений последовательности')
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.grid()
    plt.show()


def analyze_sequence(data):
    """Определяет характер последовательности."""
    increasing = all(data[i] < data[i + 1] for i in range(len(data) - 1))
    decreasing = all(data[i] > data[i + 1] for i in range(len(data) - 1))

    if increasing:
        return "возрастающая"
    elif decreasing:
        return "убывающая"

    # Проверка на периодичность
    period = None
    for p in range(2, len(data) // 2 + 1):
        if all(data[i] == data[i + p] for i in range(len(data) - p)):
            period = p
            break

    if period:
        return f"периодичная (период = {period})"

    return "случайная последовательность"
def start():
    # Чтение данных из файла
    data_str = []
    try:
        with open('data/random.txt', 'r') as f:
            data_str = [line.strip() for line in f]
    except FileNotFoundError:
        print("Файл 'random.txt' не найден.")
        return

    try:
        data = [float(i) for i in data_str]
    except ValueError:
        print("Файл 'data.txt' содержит нечисловые значения.")
        return

    count_data = [10, 20, 50, 100, 200, 300]

    # Проверяем, что в данных достаточно элементов
    if len(data) < 300:
        print("В файле 'data.txt' должно быть не менее 300 числовых значений.")
        return

    # Эталонные статистики на полной выборке из 300 элементов
    reference_data = data[:300]
    ref_mean = calculate_mean(reference_data)
    ref_variance = calculate_variance(reference_data)
    ref_std_dev = calculate_standard_deviation(reference_data)
    ref_conf_intervals = {
        0.9: confidence_interval(reference_data, confidence=0.9),
        0.95: confidence_interval(reference_data, confidence=0.95),
        0.99: confidence_interval(reference_data, confidence=0.99)
    }
    ref_cv = coefficient_of_variation(reference_data)

    print("Эталонные статистики (n=300):")
    print(f"  Математическое ожидание: {ref_mean}")
    print(f"  Дисперсия: {ref_variance}")
    print(f"  СКО: {ref_std_dev}")
    for conf, interval in ref_conf_intervals.items():
        print(f"  Доверительный интервал ({conf * 100}%) : ({interval})")
    print(f"  Коэффициент вариации: {ref_cv}%")
    print("\nОтносительные отклонения (%) для других выборок:")

    # Обработка каждой подвыборки и вычисление относительных отклонений
    for n in count_data:
        current_data = data[:n]
        current_mean = calculate_mean(current_data)
        current_variance = calculate_variance(current_data)
        current_std_dev = calculate_standard_deviation(current_data)
        current_conf_intervals = {
            0.9: confidence_interval(current_data, confidence=0.9),
            0.95: confidence_interval(current_data, confidence=0.95),
            0.99: confidence_interval(current_data, confidence=0.99)
        }
        current_cv = coefficient_of_variation(current_data)

        # Вычисление относительных отклонений
        mean_dev = relative_deviation(current_mean, ref_mean)
        variance_dev = relative_deviation(current_variance, ref_variance)
        std_dev_dev = relative_deviation(current_std_dev, ref_std_dev)
        # Для доверительных интервалов можно считать отклонение средней границы (что эквивалентно среднему)
        conf_dev_90 = relative_deviation(current_conf_intervals[0.9], ref_conf_intervals[0.9])
        conf_dev_95 = relative_deviation(current_conf_intervals[0.95], ref_conf_intervals[0.95])
        conf_dev_99 = relative_deviation(current_conf_intervals[0.99], ref_conf_intervals[0.99])
        cv_dev = relative_deviation(current_cv, ref_cv)

        # Вывод статистик и их относительных отклонений
        print(f"\nВыборка n={n}:")
        print(f"  Математическое ожидание: {current_mean} ({mean_dev:.2f}%)")
        print(f"  Дисперсия: {current_variance} ({variance_dev:.2f}%)")
        print(f"  СКО: {current_std_dev} ({std_dev_dev:.2f}%)")
        print(
            f"  Доверительный интервал (0.9): ({current_conf_intervals[0.9]}) (Среднее отклонение: {conf_dev_90:.2f}%)")
        print(
f"  Доверительный интервал (0.95): ({current_conf_intervals[0.95]}) (Среднее отклонение: {conf_dev_95:.2f}%)")
        print(
            f"  Доверительный интервал (0.99): ({current_conf_intervals[0.99]}) (Среднее отклонение: {conf_dev_99:.2f}%)")
        print(f"  Коэффициент вариации: {current_cv}% ({cv_dev:.2f}%)")

    plot_data(data)
    sequence_type = analyze_sequence(data)
    print(f"\nХарактер последовательности: {sequence_type}")


if __name__ == '__main__':
    start()
