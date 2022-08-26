lista=[1,2,3,4,6]

def adicionaNum(num,lista):
    if num <=lista[0]:
        lista.insert(0,num);
    elif num>=lista[len(lista)-1]:
        lista.append(num)
    else:
        for c in range(len(lista)):
            if num<lista[c]:
                lista.insert(lista.index(lista[c]),num)
                return lista
    return lista
print(adicionaNum(5,lista))