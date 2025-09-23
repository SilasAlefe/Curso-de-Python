def f1():
    print(f'{(9*c+160)/5}°F')

def f2(b):
    return (9*b+160)/5


c = float(input('Digite a temperatura em Celsius: '))
print(f'{c}°C em fahrenheit é')
f1()
print(f'{c}°C em fahrenheit é {f2(c)}°F')

