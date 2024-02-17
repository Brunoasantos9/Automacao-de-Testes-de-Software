def converte_para_celsius(fahrenheit):

    celsius = (5.0/9.0) * (fahrenheit - 32)

    return celsius

 

def converte_para_fahrenheit(celsius):

    fahrenheit = 1.8 * celsius + 32

    return fahrenheit 


try:
    resultado = converte_para_fahrenheit(0)
    assert resultado == 32
    print('caso 1: OK')
except AssertionError:
    print('caso 1: Erro')