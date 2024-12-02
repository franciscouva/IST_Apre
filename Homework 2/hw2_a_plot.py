import numpy as np
import matplotlib.pyplot as plt

# Gaussian function
def gaussian_pdf(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-((x - mu)**2) / (2 * sigma**2))

# Data for Class A and B
mu_A1, sigma_A1 = 1.25, 0.550757
mu_A2, sigma_A2 = 1.2, 0.60553
mu_B1, sigma_B1 = 2.75, 0.957427
mu_B2, sigma_B2 = 0.55, 0.640312

# X-axis values (range of x)
x_values = np.linspace(-1, 5, 100)

# Gaussian PDFs for x1
pdf_A1 = gaussian_pdf(x_values, mu_A1, sigma_A1)
pdf_B1 = gaussian_pdf(x_values, mu_B1, sigma_B1)

# Gaussian PDFs for x2
pdf_A2 = gaussian_pdf(x_values, mu_A2, sigma_A2)
pdf_B2 = gaussian_pdf(x_values, mu_B2, sigma_B2)

# Plotting x1 for Class A and B
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_values, pdf_A1, label='Class A (x1)', color='blue')
plt.plot(x_values, pdf_B1, label='Class B (x1)', color='red')
plt.title('Gaussian Distribution for x1')
plt.xlabel('x1')
plt.ylabel('Probability Density')
plt.legend()

# Plotting x2 for Class A and B
plt.subplot(1, 2, 2)
plt.plot(x_values, pdf_A2, label='Class A (x2)', color='blue')
plt.plot(x_values, pdf_B2, label='Class B (x2)', color='red')
plt.title('Gaussian Distribution for x2')
plt.xlabel('x2')
plt.ylabel('Probability Density')
plt.legend()

plt.tight_layout()
plt.savefig('gaussian_plot.png')

