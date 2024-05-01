# Кубический сплайн. НУЖНО РЕДАКТИРОВАТЬ ПОД СЕБЯ!!!


import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Определяем функции и их названия
functions = [
    (np.exp, "e^x"),
    (np.sinh, "sh(x)"),
    (np.cosh, "ch(x)"),
    (np.sin, "sin(x)"),
    (np.cos, "cos(x)"),
    (np.log, "ln(x)"),
    (lambda x: np.exp(-x), "e^-x")
]

# Создаем равномерную сетку на отрезке [1.00; 1.20] с шагом h = 0.04
x = np.arange(1.00, 1.21, 0.04)  # Включаем конечную точку

# Точки для вычисления значений сплайнов
points = [1.115, 1.09, 1.13, 1.15, 1.19]

# Интерполируем каждую функцию и вычисляем значения в заданных точках
for func, name in functions:
    # Вычисляем значения функции на сетке
    y = func(x)

    # Строим кубический сплайн
    spline = CubicSpline(x, y)

    # Вычисляем значения сплайна в заданных точках
    spline_values = spline(points)

    # Выводим результаты
    print(f"Функция {name}:")
    for point, value in zip(points, spline_values):
        print(f"В точке {point:.3f}, значение сплайна = {value:.4f}")
    print("-" * 40)

# Готовимся к построению графиков
fig, axs = plt.subplots(7, 1, figsize=(10, 35))

for ax, (func, name) in zip(axs, functions):
    # Вычисляем значения функции на сетке
    y = func(x)

    # Строим кубический сплайн
    spline = CubicSpline(x, y)

    # Подготавливаем детальную сетку для графика
    x_detail = np.linspace(1.00, 1.20, 400)

    # Вычисляем значения сплайна на детальной сетке
    spline_values_detail = spline(x_detail)

    # Вычисляем значения сплайна в заданных точках
    spline_values_points = spline(points)

    # Рисуем сплайн
    ax.plot(x_detail, spline_values_detail, label=f"Сплайн {name}")

    # Рисуем исходные точки
    ax.scatter(x, y, color='red', label='Исходные точки')

    # Рисуем точки, в которых вычисляли значения сплайна
    ax.scatter(points, spline_values_points, color='green', label='Значения в точках', zorder=5)

    ax.legend()
    ax.set_title(f"Сплайн интерполяция для {name}")
    ax.grid(True)

plt.tight_layout()
plt.show()
