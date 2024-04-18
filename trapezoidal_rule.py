def f(x):
    # Define the function to integrate as f(x) = x^2
    return x**2

def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Width of each trapezoid
    integral = (f(a) + f(b)) / 2.0  # Area of the first and last trapezoids
    
    # Sum the areas of the rest of the trapezoids
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    return integral * h

if __name__ == "__main__":
     
	a = 0.0  # Lower limit of integration
	b = 1.0  # Upper limit of integration
	n = 1000  # Number of trapezoids
	
	print(f"The result of function f(x) = x^2 from {a} to {b} is {trapezoidal_rule(a, b, n)}")