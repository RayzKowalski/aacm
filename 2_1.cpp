#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<double> gauss_jordan_with_pivot(vector<vector<double>>& A, vector<double>& b) {
    int n = A.size();

    // Прямой ход
    for (int i = 0; i < n; ++i) {
        // Выбор ведущего элемента
        int max_index = i;
        for (int j = i + 1; j < n; ++j) {
            if (abs(A[j][i]) > abs(A[max_index][i])) {
                max_index = j;
            }
        }
        swap(A[i], A[max_index]);
        swap(b[i], b[max_index]);

        // Приведение к единичной диагональной форме
        double pivot = A[i][i];
        for (int j = i; j < n; ++j) {
            A[i][j] /= pivot;
        }
        b[i] /= pivot;
        for (int k = 0; k < n; ++k) {
            if (k != i) {
                double factor = A[k][i];
                for (int j = i; j < n; ++j) {
                    A[k][j] -= factor * A[i][j];
                }
                b[k] -= factor * b[i];
            }
        }
    }

    return b;
}

int main() {
    vector<vector<double>> A = {{2, -1, 0},
                                 {0, 5, 2},
                                 {1, -1, 3}};
    vector<double> b = {3, 7, 4};

    vector<double> x = gauss_jordan_with_pivot(A, b);
    cout << "Решение:";
    for (double val : x) {
        cout << " " << val;
    }
    cout << endl;

    return 0;
}
