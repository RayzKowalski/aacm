import math
import random

def func(x):
    return math.sin(x) ** 2 / (13 - 12 * math.cos(x))


def monte_carlo_integration(f, a, b, n):
    sum_hits = 0.0

    # Опционально установить начальное значение генератора случайных чисел для повторяемости
    random.seed()

    for _ in range(n):
        x = a + random.random() * (b - a)
        y = random.random()

        if y <= f(x):
            sum_hits += 1

    return sum_hits / n * (b - a)


def main():
    a = float(input("Введите нижний предел интегрирования: "))
    b = float(input("Введите верхний предел интегрирования: "))
    n = int(input("Введите количество случайных точек: "))

    integral = monte_carlo_integration(func, a, b, n)
    print(f"Приближенное значение интеграла: {integral}")


if __name__ == "__main__":
    main()
