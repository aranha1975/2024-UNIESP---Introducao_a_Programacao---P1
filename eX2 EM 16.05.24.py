lista=[]
for c in range(5):
    lista.append(int(input('Digite um valor:')))
def valores(valor):
    return valor*valor

quadrado=list(map(valores, lista))
print(quadrado)