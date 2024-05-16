valores=[1000, 1500, 1250, 2500]
valor_com_imposto=[]
def imposto(valor):
    return valor * 1.1
for c in valores:
    valor_com_imposto.append(c*1.1)

print(valor_com_imposto)
