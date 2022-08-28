def organizaLista(listaA,listaB):
    
    menor=min(listaB)  
    maior=max(listaB)
    for c in listaA:
        if c <=menor:
            listaB.insert(listaB.index(menor),c)
            menor=c
        elif c>=maior:
            listaB.append(c)
            maior=c
        else:
            for v in range(len(listaB)):
                if c<listaB[v]:
                    listaB.insert(listaB.index(listaB[v]),c)
            
                    
    return listaB
print(organizaLista([1,3,42,50,80,81],[2,4,60]))