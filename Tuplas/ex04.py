


def maiorString(tuple):
    maior=' '
    for c in range(len(tuple)):
        if c==0:
            maior:tuple[c]
        else:
            if len(maior)<len(tuple[c]):
                maior=tuple[c]
    return maior
print(maiorString(('aaa','bbbb','ddd')))