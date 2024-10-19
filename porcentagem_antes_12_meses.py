# (Stevenson, 2001) A vida  útil de lavadoras de pratos automáticas pode ser modelada pela distribuição 
# normal com uma média de 1,5 ano e com desvio padrão de 0,3 ano. Que percentagem das 
# lavadoras vendidas necessitará de conserto antes de expirar o tempo de garantia de 12 meses?

from scipy.stats import norm

# Parâmetros da distribuição normal
media = 1.5  # média de 1,5 anos
desvio = 0.3  # desvio padrão de 0,3 ano

# Garantia de 12 meses = 1 ano
tempo_garantia = 1  # 1 ano

# Calcula a percentagem de lavadoras que falham antes de 1 ano (CDF até 1)
percentagem = norm.cdf(tempo_garantia, media, desvio) # é CDF pq é menor (antes dos 12 meses de garantia)

# Exibe o resultado
print(f'A percentagem de lavadoras que necessitarão de conserto antes de expirar a garantia é {percentagem:.4f}')
