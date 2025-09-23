m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
m3 = float(input('Digite a terceira nota: '))

media = round((m1+m2+m3)/3, 2)

if (media >=0.0) and (media <= 4.0):
    print(f'A média do aluno é {media} e ele está REPROVADO')
else:
    if (media >= 4.1) and (media < 6.0):
        print(f'A média do aluno é {media} e ele está EM RECUPERAÇÃO')

        exame = float(input('Digite a nota do exame: '))

        if exame > 6.0:
            print(f'O aluno foi APROVADO')
        else:
            print(f'O aluno foi REPROVADO')
    else:
        if media >= 6:
            print(f'A média do aluno é {media} e ele está APROVADO')
        else:
            print('NOTAS INVÁLIDAS')