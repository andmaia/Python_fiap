matriz=[]

for i in range(4):
    matriz.append([0]*5)
    
for i in range(4):
    for j in range(5):
        matriz[i][j] = j
for linha in matriz:
    print(linha)
