def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius

def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit

try:
    resultado = converte_para_fahrenheit(0)
    assert resultado == 32
    print('caso 1: ok')
except AssertionError:
    print('caso 1: erro')


try:
    resultado = converte_para_fahrenheit(27)
    assert resultado == 80.6
    print('caso 2: ok')
except AssertionError:
    print('caso 2: erro')


try:
    resultado = converte_para_celsius(32)
    assert resultado == 0
    print('caso 3: ok')
except AssertionError:
    print('caso 3: erro')


try:
    resultado = converte_para_celsius(41)
    assert resultado == 5
    print('caso 4: ok')
except AssertionError:
    print('caso 4: erro')