def dados (nome, idade, peso, altura, sexo):
    imc=peso/(altura**2)
    if idade >= 18:
        carcidade='maior'
    else:
        carcidade='menor'
    print(f'O nome de {nome} tem {len(nome)} letras.')
    print(f'{nome} é {carcidade} de idade. ')
    if imc < 18.5:
        print(f'O IMC de {nome} é {imc:.2f} e está ABAIXO DO PESO ideal.')
    elif imc >= 18.5 and imc <= 25 :
        print(f'O IMC de {nome} é {imc:.2f} e está no PESO IDEAL.')
    else:
        print(f'O IMC de {nome} é {imc:.2f} e está com SOBREPESO.')
dados (str(input('Digite o primeiro nome: ')), int(input('Digite a idade: ')),
      float(input('Digite o peso: ')), float(input('Digite a altura: ')),
      str(input('Digite o sexo [M/F]: ')))
