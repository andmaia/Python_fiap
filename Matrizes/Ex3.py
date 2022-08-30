from random import randint

colunas=5
linhas=7
matriz=[]

for l in range(linhas):
    matriz.append([]*colunas)


for c in range(len(matriz)):

    for v in range(colunas):

      matriz[c].append(randint(0,1))
print(matriz)


