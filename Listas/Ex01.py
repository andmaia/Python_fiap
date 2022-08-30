


matriz=list(range(6))


def cria_funcao(linhas,colunas,lista):
    matriz=[]
    if (linhas*colunas)!=len(lista):
        return f'Impossível fazer uma matriz'
    else:
        for c in range(colunas):
          matriz.append([])
        c=n=0
        while n!=len(lista):
            matriz[c].append(lista[n])
            n=n+1
            if len(matriz[c])==linhas:
                c=+1
        return matriz

print(cria_funcao(3,2,matriz))