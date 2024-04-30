'''masculino={}
feminino={}
masc=[]
fem=[]

while True:
    nome=str(input('Digite o nome: '))
    idade=str(input('Digite a idade: '))
    sexo=str(input('Digite o sexo [M/F]: '))
    if sexo in 'Mm':
        masculino[nome] = {'Idade': idade, 'Sexo': sexo}
    elif sexo in 'Ff':
        feminino[nome] = {'Idade': idade, 'Sexo': sexo}
    else:
        print('Opção de sexo inválida. Digite novamente.')
        sexo = str(input('Digite o sexo [M/F]: '))
    c = str(input('Deseja continuar inserindo dados? [S/N]: '))
    if c in 'Nn':
        break
#for c in masc:
#    masculino[c]=c+1

masculino

print(f'Dados masculinos: {masculino}')
print(f'Dados Femininos: {feminino}')'''

feminino = {}
masculino = {}

while len(feminino) + len(masculino) < 10:
    nome = input('Digite o nome do cliente: ')
    sexo = input('Digite o sexo do cliente [M/F]: ')
    idade = input('Digite a idade do cliente: ')

    if sexo.upper() == 'M':
        masculino[nome] = {'Sexo': sexo, 'Idade': idade}
    elif sexo.upper() == 'F':
        feminino[nome] = {'Sexo': sexo, 'Idade': idade}
    else:
        print('Sexo inválido. Digite novamente.')

    continuar = input('Deseja continuar cadastrando clientes? [S/N]: ')
    if continuar.upper() == 'N':
        break

print('\n--- Dados dos Clientes Femininos ---')
for nome, dados in feminino.items():
    print(f'Nome: {nome}, Sexo: {dados["Sexo"]}, Idade: {dados["Idade"]}')

print('\n--- Dados dos Clientes Masculinos ---')
for nome, dados in masculino.items():
    print(f'Nome: {nome}, Sexo: {dados["Sexo"]}, Idade: {dados["Idade"]}')
