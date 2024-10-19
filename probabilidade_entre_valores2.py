# (Freund, 2006) A experiência mostra que 30% dos lançamentos de foguete de uma base da 
# NASA foram adiados em virtude do mau tempo. Determine a probabilidade de que, em dez 
# lançamentos de foguete daquela base, de 3 a 5 sejam adiados em virtude do mau tempo.
# 0,1029
# 0,5698
# 0,2668
# 0,2001

# usa binom pois só existem duas possibilidades, do lançamento acontecer e não acontecer
from scipy.stats import binom

# Parâmetros
n = 10  # número total de lançamentos
p = 0.30  # probabilidade de adiamento

# Calcula a probabilidade de 3 a 5 adiamentos
probabilidade = binom.pmf(3, n, p) + binom.pmf(4, n, p) + binom.pmf(5, n, p)

# Exibe o resultado
print(f'A probabilidade de que de três a cinco lançamentos sejam adiados é {probabilidade:.4f}')
