notas = {'Silas':8.0, 'Rafael':7.5, 'Ellen':8.0}
n = 1

for a, b in notas.items():
    print(a, b)
    with open(f'aluno{n}.txt', 'w') as texto:
        texto.write(f'{a},{b}')
    n += 1