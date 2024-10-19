# P(0<X<x)
# Probabilidade entre 0 e x

from scipy.stats import expon

print('sabendo que as lampadas de um fabricante duram em média 1000 horas...')

alfa = 1000
media = 1/alfa
cdf_value = expon.cdf(alfa, scale=1/media) # distribuição exponencial inverte a media
print(f'probabilidade de durar 1000 horas: {cdf_value}')

alfa = 1000
media = 1/900
cdf_value1 = expon.cdf(alfa, scale=1/media) # distribuição exponencial inverte a media
alfa = 1000
media = 1/1200
cdf_value2 = expon.cdf(alfa, scale=1/media) # distribuição exponencial inverte a media
cdf_value3 = cdf_value1 - cdf_value2
print(f'probabilidade de durar entre 900 e 1200 horas:{cdf_value1} - {cdf_value2} = {cdf_value3}')


alfa = 850
media = 1/1000
cdf_value = expon.sf(alfa, scale=1/media) # distribuição exponencial inverte a media
print(f'probabilidade de durar mais de 850 horas: {cdf_value}')

