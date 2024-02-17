# calcula o volume de uma caixa retangular
def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura 



try:
    resultado = calcula_volume(1, 1, 1)
    assert resultado == 1
    print('caso 1: ok')
except AssertionError:
    print('caso 1: erro')


try:
    resultado = calcula_volume(2, 4, 3)
    assert resultado == 24
    print('caso 2: ok')
except AssertionError:
    print('caso 2: erro')


try:
    resultado = calcula_volume(5, 5, 2)
    assert resultado == 50
    print('caso 3: ok')
except AssertionError:
    print('caso 3: erro')