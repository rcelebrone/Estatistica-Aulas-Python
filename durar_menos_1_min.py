# O tempo de utilização de um caixa eletrônico por clientes de um certo banco, em minutos,  
# foi modelado por uma variável T com distribuição exponencial com parâmetro igual a 3. 
# Determine a probabilidade de que um cliente demore menos de um minuto utilizando o caixa eletrônico.

from scipy.stats import expon

alfa = 1
media = 1/3
cdf_value = expon.cdf(alfa, scale=media)
print(f'a probabilidade de que um cliente demore menos de um minuto utilizando o caixa eletrônico é {cdf_value}')