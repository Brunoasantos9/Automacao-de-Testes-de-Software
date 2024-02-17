def calcula_volume(comprimento, largura, altura):

    return comprimento * largura * altura 


try:
    resultado = calcula_volume(1, 1, 1)
    assert resultado == 1
    print('caso 1: OK')
except AssertionError:
	print('caso 1: Erro')