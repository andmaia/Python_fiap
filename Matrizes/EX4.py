i=0

matriz=[]
while i <3:
    matriz.append([])
    i+=1
n=0
while n<3:
    for c in range(len(matriz)):
        matriz[c].append(n)
    n+=1


def somaPos(matriz):
    soma=0
    for c in range(len(matriz)):
        for v in range(len(matriz[c])):
           soma+= matriz[c][v]


    return soma
print(somaPos(matriz))

