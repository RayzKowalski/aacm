import numpy as np

def gradient_descent(A, b, initial_guess, learning_rate=0.01, tol=1e-6, max_iter=1000):
    x = initial_guess
    for _ in range(max_iter):
        error = np.dot(A, x) - b
        gradient = 2 * np.dot(A.T, error)
        x_new = x - learning_rate * gradient
        
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    print("Метод не сошелся после", max_iter, "итераций.")
    return None

A = np.array([[2, -1, 0],
              [0, 5, 2],
              [1, -1, 3]])
b = np.array([3, 7, 4])
initial_guess = np.zeros_like(b)

solution = gradient_descent(A, b, initial_guess)
if solution is not None:
    print("Решение:", solution)
