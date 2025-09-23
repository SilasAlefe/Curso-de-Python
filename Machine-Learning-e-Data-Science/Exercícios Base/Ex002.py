idade = int(input('Digite a sua idade: '))

if (idade >= 0) and (idade <= 12):
    print(f'A pessoa tem {idade} anos e é uma CRIANÇA')
else:
    if (idade >= 13) and (idade <= 17):
        print(f'A pessoa tem {idade} anos e é um ADOLESCENTE')
    else:
        if (idade >= 18):
            print(f'A pessoa tem {idade} anos e é um ADULTO')
        else:
            print('IDADE INVÁLIDA')