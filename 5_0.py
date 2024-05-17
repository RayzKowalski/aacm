import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Пример функции для разложения
def f(x):
    return x

# Период функции
T = 2 * np.pi

# Численное интегрирование для коэффициентов
def compute_a0(f, T):
    result, _ = quad(f, 0, T)
    return result / T

def compute_an(f, T, n):
    result, _ = quad(lambda x: f(x) * np.cos(2 * np.pi * n * x / T), 0, T)
    return 2 * result / T

def compute_bn(f, T, n):
    result, _ = quad(lambda x: f(x) * np.sin(2 * np.pi * n * x / T), 0, T)
    return 2 * result / T

# Количество гармоник
N = 10

# Вычисляем коэффициенты
a0 = compute_a0(f, T)
an = [compute_an(f, T, n) for n in range(1, N+1)]
bn = [compute_bn(f, T, n) for n in range(1, N+1)]

# Печать коэффициентов
print(f'a0: {a0}')
for n in range(1, N+1):
    print(f'a{n}: {an[n-1]}, b{n}: {bn[n-1]}')

# Восстановление функции по ряду Фурье
def fourier_series(x, a0, an, bn, T):
    result = a0
    for n in range(1, len(an) + 1):
        result += an[n-1] * np.cos(2 * np.pi * n * x / T) + bn[n-1] * np.sin(2 * np.pi * n * x / T)
    return result

# Точки для графика
x_vals = np.linspace(0, T, 1000)
y_vals = f(x_vals)
y_fourier = [fourier_series(x, a0, an, bn, T) for x in x_vals]

# Вывод значений разложения для первых нескольких точек
print("\nПервые несколько значений разложения:")
for i in range(10):
    print(f"x = {x_vals[i]:.2f}, f(x) = {y_vals[i]:.2f}, Fourier(x) = {y_fourier[i]:.2f}")

# Построение графика
plt.plot(x_vals, y_vals, label='Original function')
plt.plot(x_vals, y_fourier, label='Fourier series')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Fourier Series Approximation')
plt.grid(True)
plt.show()
