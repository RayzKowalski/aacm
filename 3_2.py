#НЕ ПОНИМАЮ

from math import sin, cos

def equations(x, y):
    func1 = sin(y + 1) - x - 1.2
    func2 = 2 * y + cos(x) - 2
    return func1, func2

def jacobian(x, y):
    df1_dx = -1
    df1_dy = cos(y + 1)
    df2_dx = -sin(x)
    df2_dy = 2
    return df1_dx, df1_dy, df2_dx, df2_dy

def newton_raphson(x, y, tolerance):
    while True:
        f1, f2 = equations(x, y)
        df1_dx, df1_dy, df2_dx, df2_dy = jacobian(x, y)
        determinant = df1_dx * df2_dy - df1_dy * df2_dx

        inv_df1_dx = df2_dy / determinant
        inv_df1_dy = -df1_dy / determinant
        inv_df2_dx = -df2_dx / determinant
        inv_df2_dy = df1_dx / determinant

        dx = inv_df1_dx * f1 + inv_df1_dy * f2
        dy = inv_df2_dx * f1 + inv_df2_dy * f2

        x -= dx
        y -= dy

        if abs(dx) < tolerance and abs(dy) < tolerance:
            break

    return x, y

def main():
    result = newton_raphson(-2, -2, 1e-4)
    print(f"x = {result[0]}\ty = {result[1]}")

if __name__ == "__main__":
    main()
