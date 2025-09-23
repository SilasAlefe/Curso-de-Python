tempo = int(input('Quantas horas durou a viagem? '))
mediav = int(input('Qual a media de velocidade? '))

distancia = tempo * mediav

litros = distancia / 12

print('')
print(f'Você rodou {distancia} kilometros')
print(f'O gasto de combustível foi de {round(litros, 1)} litros')