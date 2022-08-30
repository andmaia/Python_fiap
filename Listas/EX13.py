from tkinter import N


pessoas=list(range(1,1001))

def portas(pessoas):
    portas=[]
    for c in range(1,len(pessoas)):
        if c==1:
            while len(portas)<1001:
                portas.append(False)
        else:
            for n in range(1,len(portas)):
                
                v=n
                while v<len(portas):
                    if portas[v]==False:
                        portas[v]=True
                    if portas[v]==True:
                        portas[v]=False
                    v+=v    
    return portas                
                
                

print(portas(pessoas))


