lista = []
soma = 0

for n in range(6):
    lista.append(int(input('Digite um número inteiro: ')))
    soma += lista[n]

print(lista)
print(f'A soma dos elementos da lista é {soma}')