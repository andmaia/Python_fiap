
def interseccao(listaA,listaB):
    listaC=[]
    for c in listaA:
        if c in listaB:
            listaC.append(c)
    if len(listaC)==0:
        return f'Não elementos que fazem pate da interssecção.'
    else:
        return listaC
print(interseccao([1,2,3],[2,3]))