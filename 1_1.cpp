#include <iostream>
#include <cmath>

using namespace std;

double func(double x) {
    return pow(sin(x), 2) / (13 - 12 * cos(x));
}

double simpsons_rule(double (*f)(double), double a, double b, int n) {
    double h = (b - a) / n;
    double x = a;
    double integral = f(a) + f(b);

    for (int i = 1; i < n; i++) {
        x += h;
        if (i % 2 == 0) {
            integral += 2 * f(x);
        }
        else {
            integral += 4 * f(x);
        }
    }

    integral *= h / 3;
    return integral;
}

double adaptive_simpsons_rule(double (*f)(double), double a, double b, int min_n, int max_n, double tol) {
    int n = min_n;
    double integral_old = simpsons_rule(f, a, b, n);
    n *= 2;
    double integral_new = simpsons_rule(f, a, b, n);

    while (abs(integral_new - integral_old) / 15 > tol && n <= max_n) {
        integral_old = integral_new;
        n *= 2;
        integral_new = simpsons_rule(f, a, b, n);
    }

    if (n > max_n) {
        throw "Максимальное количество разбиений достигнуто без достижения требуемой точности.";
    }

    return integral_new;
}

int main() {
    double a, b;
    int min_n = 10, max_n = 10000;
    double tol = 1e-4; // Указываем требуемую абсолютную погрешность

    cout << "Введите нижний предел интегрирования: ";
    cin >> a;
    cout << "Введите верхний предел интегрирования: ";
    cin >> b;

    try {
        double integral = adaptive_simpsons_rule(func, a, b, min_n, max_n, tol);
        cout << "Приближенное значение интеграла: " << integral << endl;
    }
    catch (const char* msg) {
        cerr << msg << endl;
    }

    return 0;
}
