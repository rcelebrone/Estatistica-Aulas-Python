# Testar se a média de uma população é igual a 50 com uma amostra de tamanho n = 30, 
# média amostral x̄ = 53, desvio padrão populacional conhecido σ = 10 e nível de 
# significância α = 0,05.

import numpy as np
from scipy import stats

# Dados amostrais
dados = [12, 8, 15, 13, 10, 12, 14, 11, 12, 13, 15,19,15,12,13,16,15]

# Parâmetros do teste
mu = 12  # Média sob H0
alpha = 0.05  # Nível de significância
conf_level = 0.95  # Nível de confiança

# Estatística de teste t e valor-p bilateral
t_statistic, p_value_bilateral = stats.ttest_1samp(dados, popmean=mu)

print(f'Estatística t: {t_statistic:.4f}')
print(f'Valor-p bilateral: {p_value_bilateral:.4f}')

# Ajuste do valor-p para teste unilateral (alternative='greater')
if t_statistic > 0:
    p_value = p_value_bilateral / 2
else:
    p_value = 1 - (p_value_bilateral / 2)

print(f'Valor-p unilateral: {p_value:.4f}')

# Estatísticas da amostra
n = len(dados)
df = n - 1  # Graus de liberdade
sample_mean = np.mean(dados)
sample_std = np.std(dados, ddof=1)  # Desvio padrão amostral

# Quantil t crítico para o nível de confiança unilateral
t_crit = stats.t.ppf(conf_level, df)

# Limite superior do intervalo de confiança unilateral
upper_limit = sample_mean + t_crit * (sample_std / np.sqrt(n))

print(f'Intervalo de confiança unilateral superior: ({sample_mean:.4f}, {upper_limit:.4f})')

# Decisão
if p_value < alpha:
    print('Rejeitamos H0: a média é significativamente maior que 12.')
else:
    print('Não rejeitamos H0: não há evidência suficiente para afirmar que a média é maior que 12.')
