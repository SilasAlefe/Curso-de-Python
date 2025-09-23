dados = {}
media = {}
soma = 0

for n in range(3):
    nome = str(input(f'Digite o nome do {n+1}° aluno: '))
    nota = float(input(f'Digite a nota do {n+1}° aluno: '))

    dados.update({nome: nota}) #ou dados[nome] = nota
    soma += nota

print(dados)
print(f'A média de pontos é: {soma/3}')