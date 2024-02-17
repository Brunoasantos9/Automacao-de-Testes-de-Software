import unittest


def avaliar_notas(n1, n2, n3, media_exercicios):



    if n1 < 0 or n1 > 10:

        raise ValueError('Valor inválido para n1')



    if n2 < 0 or n2 > 10:

        raise ValueError('Valor inválido para n2')



    if n3 < 0 or n3 > 10:

        raise ValueError('Valor inválido para n3')



    if media_exercicios < 0 or media_exercicios > 10:

        raise ValueError('Valor inválido para media_exercicios')





    media_aproveitamento = (n1 + 2*n2 + 3*n3 + media_exercicios)/7



    if media_aproveitamento >= 9.0:

        return 'A'

    elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:

        return 'B'

    elif media_aproveitamento >= 6.0 and media_aproveitamento < 7.5:

        return 'C'

    elif media_aproveitamento < 6.0:

        return 'D' 
    

class TesteAvaliarNotas(unittest.TestCase):

    def avaliar_notas(self):

	    self.assertEqual(avaliar_notas(10, 10, 10, 10)'A')


if __name__ == '__main__':

	unittest.main()