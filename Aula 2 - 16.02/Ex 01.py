import unittest
from escolar import avaliar_notas

class TestAvaliarNotas(unittest.TestCase):
    
    def test_valor_invalido_n1(self):
        with self.assertRaises(ValueError):
            avaliar_notas(-1, 0, 0, 0)

    
    def test_valor_invalido_n2(self):
        with self.assertRaises(ValueError):
            avaliar_notas(0, -1, 0, 0)

    
    def test_valor_invalido_n3(self):
        with self.assertRaises(ValueError):
            avaliar_notas(0, 0, -1, 0)


    def test_conceito_A(self):
        self.assertEqual(avaliar_notas(10, 10, 10, 10), 'A')

    
    def test_conceito_B(self):
        self.assertEqual(avaliar_notas(8.9, 8.9, 8.9, 8.9), 'B')

    
    def test_conceito_C(self):
        self.assertEqual(avaliar_notas(7.4, 7.4, 7.4, 7.4), 'C')

    
    def test_conceito_D(self):
        self.assertEqual(avaliar_notas(5.9, 5.9, 5.9, 5.9), 'D')
        
    

if __name__ == '__main__':
    unittest.main()
