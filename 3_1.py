import numpy as np

def f(x):
    return x - 1 / np.tan(x)

def df(x):
    return 1 + 1 / np.sin(x)**2

def combined_method(func, df, a, b, tol=1e-4, max_iter=100):
    for _ in range(max_iter):
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tol:
            return c
        if np.sign(func(c)) == np.sign(func(a)):
            a = c
        else:
            b = c
        if abs(func(c)) < tol:
            return c
        c = c - func(c) / df(c)
        if abs(func(c)) < tol:
            return c
    raise ValueError("Метод не сошелся.")

# Находим корни уравнения
roots = []
ranges = [(0.1, np.pi/2), (np.pi/2, np.pi), (np.pi, 3*np.pi/2), (3*np.pi/2, 2*np.pi)]
for interval in ranges:
    root = combined_method(f, df, interval[0], interval[1])
    roots.append(root)

# Выводим корни
print("Корни уравнения:")
for i, root in enumerate(roots):
    print(f"Корень {i + 1}: {root:.6f}")
