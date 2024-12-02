import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the polynomial
coefficients = [2.59232475, -7.49664634, -1.93661531, 10.03942366]

# Create a function to evaluate the polynomial
def polynomial(x):
    return coefficients[0]*x**3 + coefficients[1]*x**2 + coefficients[2]*x + coefficients[3]

# Generate x values
x = np.linspace(-1.5, 3, 400)

# Calculate y values
y = polynomial(x)

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2.59*x^3 - 7.50*x^2 - 1.94*x + 10.04', color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig('polynomial_plot.png')
