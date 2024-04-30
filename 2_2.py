import numpy as np


def gauss_seidel(A, B, initial_guess, tol=1e-6, max_iter=1000):
    """
    Реализация метода Зейделя для решения системы линейных уравнений Ax=B.

    Параметры:
        A: numpy.array, квадратная матрица коэффициентов системы уравнений
        B: numpy.array, вектор правой части системы уравнений
        initial_guess: numpy.array, начальное приближение решения
        tol: float, допустимая погрешность
        max_iter: int, максимальное количество итераций

    Возвращает:
        x: numpy.array, приближенное решение системы уравнений
        num_iter: int, количество выполненных итераций
    """
    n = len(B)
    x = initial_guess
    num_iter = 0
    while num_iter < max_iter:
        x_prev = np.copy(x)
        for i in range(n):
            x[i] = (B[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        if np.linalg.norm(x - x_prev) < tol:
            break
        num_iter += 1
    return x, num_iter


# Заданные матрицы A и B
A = np.array([[2.0, -1.0, 0.0], [0.0, 5.0, 2.0], [1.0, -1.0, 3.0]])
B = np.array([3.0, 7.0, 4.0])

# Начальное приближение решения
initial_guess = np.zeros_like(B)

# Вызов функции метода Зейделя
solution, num_iterations = gauss_seidel(A, B, initial_guess)

print("Приближенное решение:", solution)
print("Количество итераций:", num_iterations)
