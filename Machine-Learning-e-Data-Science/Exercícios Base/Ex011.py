lista = []

try:
    for a in range(1,3):
        lista.append(float(input('Digite um número: ')))
    divisao = lista[0] / lista[1]
except ValueError:
    print('Valor digitado não é um número!')
except ZeroDivisionError:
    print('Segundo valor digitado é igual a zero!')
except IndexError:
    print('Índice inválido!')
except KeyboardInterrupt:
    print('Usuário interrompeu a execução!')