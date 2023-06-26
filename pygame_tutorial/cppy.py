from os import listdir, system
import re




lista = listdir('.')


lista_fil = list()
for l in lista:
    if l[0] == 'g':
        lista_fil.append(l)



print(lista_fil)
print(len(lista_fil))
arq_anterior = len(lista_fil)
arq = arq_anterior + 1

system(f'cp g{arq_anterior}.py g{arq}.py')