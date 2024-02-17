import unittest
from aposentadoria import verificar_qualificacao_empregado, REQUERER, NAO_REQUERER

class TestVerificarQualificacaoEmpregado(unittest.TestCase):
    
    def test_parametros_invalidos_idade_e_tempo_de_servico(self):
        with self.assertRaises(ValueError):
            verificar_qualificacao_empregado(0, 10)

    def test_parametros_invalidos_idade_e_tempo_de_servico(self):
        with self.assertRaises(ValueError):
            verificar_qualificacao_empregado(20, 0)


    def test_parametros_invalidos_idade(self):
        with self.assertRaises(TypeError):
            verificar_qualificacao_empregado('65', 30)

    
    def test_parametros_invalidos_tempo_de_servico(self):
        with self.assertRaises(TypeError):
            verificar_qualificacao_empregado(65, '30')





    def test_idade_minima(self):
        self.assertEqual(verificar_qualificacao_empregado(65, 20), REQUERER)
    
    def test_tempo_de_servico_minimo(self):
        self.assertEqual(verificar_qualificacao_empregado(59, 30), REQUERER)
    
    def test_idade_e_tempo_de_servico_minimos(self):
        self.assertEqual(verificar_qualificacao_empregado(60, 25), REQUERER)
    
    def test_nao_qualificado(self):
        self.assertEqual(verificar_qualificacao_empregado(59, 24), NAO_REQUERER)


if __name__ == '__main__':
    unittest.main()
