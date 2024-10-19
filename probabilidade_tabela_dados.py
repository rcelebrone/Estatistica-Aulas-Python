# Determine a probabilidade de escolhermos, aleatoriamente, 
# uma pessoa do sexo masculino e sem opinião sobre a reforma agrária?
# 0,0811
# 0,1216
# 0,4865
# 0,1538

masc_diurno_sem_opiniao = 8
masc_noturno_sem_opiniao = 1

total = masc_diurno_sem_opiniao + masc_noturno_sem_opiniao

total_pessoas_diurno = 2+8+2+8+9+8
total_pessoas_noturno = 4+8+2+12+10+1

total_pessoas = total_pessoas_diurno + total_pessoas_noturno

p = total / total_pessoas

print(f'A probabilidade de escolhermos uma pessoa do sexo masculino e sem opinião sobre a reforma agrária é {p}')