


def desvioPadrao(valores):
    soma=0
    for c in range(len(valores)):
        soma+=valores[c]
    media=soma/len(valores)

    dp=((soma*(valores[0]-media)**2)/len(valores))*1/2
    
    return dp

print(desvioPadrao((1.55,1.170,1.8)))