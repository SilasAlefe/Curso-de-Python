import numpy as np

matriz = np.array([[3,4,1], [3,1,5]])
soma = 0

for a in range(matriz.shape[0]):
    for b in range(matriz.shape[1]):
        soma += matriz[a][b]
        print(matriz[a][b])
print(f'A soma de todos os elementos é {soma}')