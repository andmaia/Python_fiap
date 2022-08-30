#Capturando valores inteiros para lista 
n=int(input('Digite um número:'))
op=''
valores=[]
while True:
    valores.append(int(input('Digite um valor inteiro:')))
    op=input('Quer continuar ?')
    if op[0] in 'nN':
        break

#Declaração de variáveis
c=0
x=c+1

while c<len(valores):
    soma=valores[c]+valores[n-x]
    print(soma)
    c+=1