from random import randint
matriz=[]
linhas=0
while linhas<4:
        matriz.append([0])
        linhas+=1
        
for linhas in range(len(matriz)):
        l=0
        while l<4:
            matriz[linhas].append(randint(-5,10))
            l+=1   



def valor(matriz):
    positivos=0
    negativos=0

    for linhas in range(len(matriz)):
        for colunas in range(len(matriz[linhas])):
            if matriz[linhas][colunas]<0:
                negativos+=matriz[linhas][colunas]
            else:
                positivos+=matriz[linhas][colunas]
    return [positivos,negativos]
            



print(valor(matriz))


