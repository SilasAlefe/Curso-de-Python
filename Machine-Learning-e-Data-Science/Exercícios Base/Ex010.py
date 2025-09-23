def leiadados():
    velocidade = float(input('Digite a velocidade média em km/h: '))
    tempo = float(input(f'Digite o tempo para percorrer os {velocidade} em horas: '))
    return velocidade, tempo
def calculedistancia(velocidade, tempo):
    return velocidade*tempo
def calculelitros(distancia):
    return distancia/12
def mostrarresultado():
    velocidade, tempo = leiadados()
    distancia = calculedistancia(velocidade, tempo)
    litros = calculelitros(distancia)
    print(f'A velocidade foi: {velocidade}')
    print(f'O tempo foi: {tempo}')
    print(f'A distância foi: {distancia}')
    print(f'A quantidade de litros de gasolina gasto foi: {round(litros, 2)}')

mostrarresultado()

