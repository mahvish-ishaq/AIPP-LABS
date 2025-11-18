# TASK 4 - GRADIENT DESCENT OPTMIZATION
# Gradient Descent for minimizing the function f(x) = (x-3)^2 + 4

def f_derivative(x):
    return 2*x + 4   # derivative of x^2 + 4x + 5

def gradient_descent(lr=0.1, iterations=100):
    x = 0  # starting point
    for i in range(iterations):
        grad = f_derivative(x)
        x = x - lr * grad
    return x

x_min = gradient_descent()
print("Value of x where f(x) is minimum:", x_min)



