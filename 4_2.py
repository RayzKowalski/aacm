import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Определение функции f(x)
def f(x):
    return np.sin(x)

# Определение отрезка и шага
a = 1.00
b = 1.20
h = 0.04

# Создание равномерной сетки значений x
x_values = np.arange(a, b + h, h)

# Вычисление значений функции на сетке
y_values = f(x_values)

# Построение кубического сплайна с использованием CubicSpline
cs = CubicSpline(x_values, y_values)

# Значения сплайна в заданных точках
points_to_interpolate = np.linspace(a, b, 100)  # Генерация точек для плавного графика
spline_values = cs(points_to_interpolate)

# Вывод результатов
for x, y_interp in zip(points_to_interpolate, spline_values):
    print(f"Значение сплайна в точке x = {x}: {y_interp}")

# Построение графика
plt.plot(x_values, y_values, 'o', label='Исходные данные')  # Точки данных
plt.plot(points_to_interpolate, spline_values, label='Кубический сплайн')  # Интерполированные значения
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция кубическим сплайном')
plt.legend()
plt.grid(True)
plt.show()
