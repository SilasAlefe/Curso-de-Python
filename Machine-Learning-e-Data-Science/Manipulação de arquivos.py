with open('frase1.txt') as tex:
    for linha in tex:
        print(linha)

print('-----------------------------')

with open('frase1.txt') as tex:
    r = tex.readline()
    print(r)

print('-----------------------------')

with open('frase2.txt', 'w') as texto:
    texto.write('Olá a todos')
    print(texto)
