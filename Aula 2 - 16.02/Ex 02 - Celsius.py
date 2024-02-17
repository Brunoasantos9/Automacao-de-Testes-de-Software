import unittest

def converte_para_celsius(fahrenheit):

    celsius = (5.0/9.0) * (fahrenheit - 32)

    return celsius



class TesteConverteCelsius(unittest.TestCase):

    def test_celsius(self):

	    self.assertEqual(converte_para_celsius(41), 5)


if __name__ == '__main__':

	unittest.main()
     

