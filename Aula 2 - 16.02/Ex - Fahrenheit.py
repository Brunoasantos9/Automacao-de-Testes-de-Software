import unittest

def converte_para_fahrenheit(celsius):

    fahrenheit = 1.8 * celsius + 32

    return fahrenheit 


class TesteConverteFahrenheit(unittest.TestCase):

    def test_fahrenheit(self):

	    self.assertEqual(converte_para_fahrenheit(27), 80.6)


if __name__ == '__main__':

	unittest.main()