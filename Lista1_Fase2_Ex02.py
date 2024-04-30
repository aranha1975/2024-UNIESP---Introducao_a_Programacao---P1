valores=[]
soma=0
while True:
    numero=int(input('Digite um número: '))
    valores.append(numero)
    soma+=numero
    parar=str(input('Quer continuar? [S/N]: '))
    if parar in 'Nn':
        break
print(f'Você digitou os seguintes números: {valores}.')
print(f'A soma entre os valores digitados foi {soma}.')

