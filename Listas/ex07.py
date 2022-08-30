def verifica(lista):
    maior=0
    for c in range(len(lista)):
        if c==0:
            maior=lista[c]
        else:
            if maior<=lista[c]:
                maior=lista[c]
            else:
                return False
    return True 

print(verifica([1,2,3]))