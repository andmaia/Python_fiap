
import math


matriz=[[2,3,4],[5,6,7],[8,9,10]]

def getDimensao(mat):
    linhas=0
    colunas=0
    for c in range(len(mat)):
        linhas+=1
        for n in mat[c]:
            colunas+=1
            

    return f'{linhas} e {colunas/linhas}'
print(getDimensao(matriz))