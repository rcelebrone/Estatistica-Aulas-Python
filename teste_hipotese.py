# Testar se a média de uma população é igual a 50 com uma amostra de tamanho n = 30, 
# média amostral x̄ = 53, desvio padrão populacional conhecido σ = 10 e nível de 
# significância α = 0,05.

import numpy as np
from scipy import stats

# Parâmetros
mu_0 = 50
sigma = 10
n = 30
alpha = 0.05
x_bar = 53

# Estatística de teste z
z = (x_bar - mu_0) / (sigma / np.sqrt(n))
print(f'Estatística de teste z: {z:.3f}')

# Valor-p
p_value = 2 * (1 - stats.norm.cdf(abs(z)))
print(f'Valor-p: {p_value:.3f}')

# Decisão
if p_value < alpha:
    print('Rejeitamos H0.')
else:
    print('Não rejeitamos H0.')
