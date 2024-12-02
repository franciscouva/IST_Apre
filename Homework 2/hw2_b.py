import numpy as np

def multivariate_normal_pdf(x, mu, Sigma):
    D = len(mu)
    
    Sigma_det = np.linalg.det(Sigma)
    
    Sigma_inv = np.linalg.inv(Sigma)
    
    norm_factor = 1 / (np.power(2 * np.pi, D / 2) * np.sqrt(Sigma_det))
    
    diff = x - mu
    exponent = -0.5 * np.dot(np.dot(diff.T, Sigma_inv), diff)
    
    return norm_factor * np.exp(exponent)


muA = np.array([1.25, 1.2])

muB = np.array([2.75, 0.55])

SigmaA = np.array([[0.303333, 0.326667], 
                    [0.326667, 0.366667]])

SigmaB = np.array([[0.916667, 0.25], 
                    [0.25, 0.41]])

x = np.array([1, 2])

print(multivariate_normal_pdf(x, muA, SigmaA))
print(multivariate_normal_pdf(x, muB, SigmaB))
