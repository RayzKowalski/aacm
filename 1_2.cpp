#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

double func(double x) {
    return pow(sin(x), 2) / (13 - 12 * cos(x));
}

double monte_carlo_integration(double (*f)(double), double a, double b, int n) {
    double sum = 0.0;
    double x, y;

    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        x = a + (double)rand() / RAND_MAX * (b - a);
        y = (double)rand() / RAND_MAX;

        if (y <= f(x)) {
            sum += 1;
        }
    }

    return sum / n * (b - a);
}

int main() {
    double a, b;
    int n;

    cout << "Введите нижний предел интегрирования: ";
    cin >> a;
    cout << "Введите верхний предел интегрирования: ";
    cin >> b;
    cout << "Введите количество случайных точек: ";
    cin >> n;

    double integral = monte_carlo_integration(func, a, b, n);
    cout << "Приближенное значение интеграла: " << integral << endl;

    return 0;
}
