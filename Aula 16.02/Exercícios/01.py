import unittest

def calcula_volume(comprimento, largura, altura):

    return comprimento * largura * altura 



class TesteCalculaVolume(unittest.TestCase):

    def test_volume(self):

	    self.assertEqual(calcula_volume(2, 4, 3), 24)


if __name__ == '__main__':

	unittest.main()