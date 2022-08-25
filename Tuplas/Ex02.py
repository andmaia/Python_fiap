def maiorTuple(tuple):
    max=0
    for c in range(len(tuple)):
        if c==0:
           max= tuple[c]
        else:
            if tuple[c]>max:
                max=tuple[c]
    return max

print(maiorTuple((2,32432,45,5432,3)))
    