

def funcao(n,lista):
    maiores=0
    if n in lista:
        for c in lista:
            if n<c:
                maiores+=1
        return maiores
    else :
        return f'Parãmetro não contido em lista'
print(funcao(5,[1,2,3,4]))

