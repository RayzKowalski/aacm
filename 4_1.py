import numpy as np

class LagrangeInterpolation:
    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values

    def interpolate(self, x):
        n = len(self.x_values)
        result = 0.0
        for i in range(n):
            term = self.y_values[i]
            for j in range(n):
                if i != j:
                    term *= (x - self.x_values[j]) / (self.x_values[i] - self.x_values[j])
            result += term
        return result

def plot_interpolation(x_values, y_values):
    import matplotlib.pyplot as plt

    # Создание объекта для интерполяции
    lagrange_interpolator = LagrangeInterpolation(x_values, y_values)

    # Точки для интерполяции
    interpolation_points = np.linspace(min(x_values), max(x_values), 100)  # Генерация точек для более плавного графика

    # Интерполяция
    interpolated_values = [lagrange_interpolator.interpolate(point) for point in interpolation_points]

    # Построение графика
    plt.plot(x_values, y_values, 'o', label='Табличные значения')  # Точки данных
    plt.plot(interpolation_points, interpolated_values, label='Интерполяция Лагранжа')  # Интерполированные значения
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Интерполяция Лагранжа')
    plt.legend()
    plt.grid(True)
    plt.show()

# Пример использования
if __name__ == "__main__":
    # Табличные значения
    x_values = np.array([1, 2, 3, 4, 5])
    y_values = np.array([5.1, 4.4, 3.2, 2.7, 2.55])

    # Вывод таблицы значений
    print("Табличные значения:")
    for x, y in zip(x_values, y_values):
        print(f"x={x}, y={y}")

    # Проверка, нужно ли построить график
    plot_choice = input("Построить график интерполяции? ( + / - ): ").strip().lower()
    if plot_choice == "+":
        plot_interpolation(x_values, y_values)
    elif plot_choice != "-":
        print("Error.")
