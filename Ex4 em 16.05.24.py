valores=[1000, 1500, 1250, 2500]
def imposto(valor):
    return valor * 1.1
valor_com_imposto=list(map(imposto, valores))
print(valor_com_imposto)

#LAMBDA
numero=1000
adicionar_imposto2=list(map(lambda valor: valor * 1.1, valores))
print(adicionar_imposto2)
