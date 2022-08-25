

def retornaMedia(tuple):
    sumTuple=0
    for c in tuple:
        sumTuple+=c
    return sumTuple/len(tuple)
    
print(retornaMedia((2,2,2)))