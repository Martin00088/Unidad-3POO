import unittest
from Palindromo import Palindromo


class TestPalindromo(unittest.TestCase):
    __palindromo: Palindromo

    def setUp(self):
        self.__palindromo = Palindromo(" ")

    def test_esPalind(self):
        self.__palindromo.setPalabra("ANA")
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_noesPalindromo(self):
        self.__palindromo.setPalabra("NO")
        self.assertFalse(self.__palindromo.esPalindromo())


if __name__ == '__main__':
    unittest.main()
