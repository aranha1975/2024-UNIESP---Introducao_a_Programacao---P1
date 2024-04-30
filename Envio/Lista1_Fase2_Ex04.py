def alfabeto(letra):
    alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(alfabeto.index(letra.lower())+1)
    global posicao
    posicao=alfabeto.index(letra.lower())+1
def parimpar(posicao):
    if posicao % 2 ==0:
        pares=list(range(0,posicao,2))
        print(f'Valores PARES de 0 a {posicao} são: {pares}')
    else:
        impares = list(range(1, posicao, 2))
        print(f'Valores IMPARES de 0 a {posicao} são: {impares}')
alfabeto(str(input('Digite uma letra: ')))
parimpar(posicao)