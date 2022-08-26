import random

def geraListas(num):
    lista=random.sample(range(1000),num)
    return lista

print(geraListas(2))

