import numpy as np

def f(x):
    return (np.sin(x))**2 / (13 - 12*np.cos(x))

def simpsons_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = func(x)
    integral = h / 3 * np.sum(fx[0:-1:2] + 4 * fx[1::2] + fx[2::2])
    return integral

def runge_rule(func, a, b, n, tol):
    S1 = simpsons_rule(func, a, b, n)
    S2 = simpsons_rule(func, a, b, 2 * n)
    error = np.abs(S2 - S1) / 15
    if error < tol:
        return S2
    else:
        return runge_rule(func, a, b, 2 * n, tol)

a = 0  # Начальный предел интегрирования
b = np.pi / 2  # Конечный предел интегрирования
tolerance = 1e-6  # Заданная точность
result = runge_rule(f, a, b, 2, tolerance)
print("Результат:", result)
