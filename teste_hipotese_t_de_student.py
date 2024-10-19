# Testar se a média de uma população é igual a 50 com uma amostra de tamanho n = 30, 
# média amostral x̄ = 53, desvio padrão populacional conhecido σ = 10 e nível de 
# significância α = 0,05.

import numpy as np
from scipy import stats

# Dados amostrais
dados = [55, 52, 49, 51, 54, 50, 53, 48, 56, 47,
         52, 50, 49, 51, 54, 50, 53, 48, 56, 47,
         55, 52, 49, 51, 54, 50, 53, 48, 56, 47]

# Parâmetros
mu_0 = 50
alpha = 0.05
n = len(dados)
x_bar = np.mean(dados)
s = np.std(dados, ddof=1)  # Desvio padrão amostral

# Estatística de teste t
t = (x_bar - mu_0) / (s / np.sqrt(n))
print(f'Estatística de teste t: {t:.3f}')

# Valor-p
p_value = 2 * (1 - stats.t.cdf(abs(t), df=n-1))
print(f'Valor-p: {p_value:.3f}')

# Decisão
if p_value < alpha:
    print('Rejeitamos H0.')
else:
    print('Não rejeitamos H0.')
