import numpy as np

def gaussian_prob(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-((x - mu)**2) / (2 * sigma**2))

mu_A1, sigma_A1 = 1.25, 0.550757
mu_A2, sigma_A2 = 1.2, 0.60553
mu_B1, sigma_B1 = 2.75, 0.957427
mu_B2, sigma_B2 = 0.55, 0.640312

x1_query, x2_query = 1, 2
p_A = 0.5
p_B = 0.5

p_x1_A = gaussian_prob(x1_query, mu_A1, sigma_A1)
p_x2_A = gaussian_prob(x2_query, mu_A2, sigma_A2)
p_A_xquery = p_x1_A * p_x2_A * p_A
print(p_A_xquery)

p_x1_B = gaussian_prob(x1_query, mu_B1, sigma_B1)
p_x2_B = gaussian_prob(x2_query, mu_B2, sigma_B2)
p_B_xquery = p_x1_B * p_x2_B * p_B
print(p_B_xquery)

p_A_given_xquery = p_A_xquery / (p_A_xquery + p_B_xquery)
p_B_given_xquery = p_B_xquery / (p_A_xquery + p_B_xquery)

print(p_A_given_xquery, p_B_given_xquery)
