#soma = 0
#for n in range(1,4):
#    nota = float(input(f'Digite a {n}° nota: '))
#    soma += nota
#print(f'A media das notas foi {soma/3}')

n = 1
soma = 0
while n<=3:
    nota = float(input(f'Digite a {n}° nota: '))
    soma += nota
    n += 1
print(f'A media das notas foi {soma/3}')