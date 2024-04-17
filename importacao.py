def importacao(produto,peso,valor):
    valorreal = valor * 5.09
    frete = peso * 0.0199 * 5.09
    total=valorreal+frete
    print(f'O valor do produto em reais é: R${valorreal:.2f}.')
    print(f'O valor do frete é R$ {frete:.2f}.')
    print(f'O valor total pago foi de R$ {total:.2f}')
