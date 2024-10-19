# Uma companhia fabrica motores. As especificações requerem que o comprimento de uma certa haste deste 
# motor esteja entre 7,48 cm e 7,52 cm. Os comprimentos destas hastes, fabricadas por um fornecedor, 
# têm uma distribuição normal com média 7,505 cm e desvio padrão 0,01 cm. 
# Qual a probabilidade de uma haste escolhida ao acaso estar dentro das especificações?
# 0,0606
# 0,9270
# 0,5668
# 0,0062

from scipy.stats import norm

# Parâmetros da distribuição normal
media = 7.505
desvio = 0.01
alvo = 7.48
p = norm.cdf(alvo, media, desvio)
print(f'A probabilidade de uma haste escolhida é {p} com base em {alvo}')

# Parâmetros da distribuição normal
alvo = 7.52
p2 = norm.cdf(alvo, media, desvio)
print(f'A probabilidade de uma haste escolhida é {p2} com base em {alvo}')

print(f'probabilidade entre valores {p2-p}')
