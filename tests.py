# tests.py

#importamos la libreria unitest para los tests unitarios
import unittest
#importamos la función a la que le vamos a realizar el test
from charfun import esPalindromo

#clase para los test unitarios
class Test(unittest.TestCase):

    #comprobamos que la funcion devuelve true si una frase es palindroma
    def test_cadena_es_palindroma(self):
        cadena='Anita lava la tina'
        resultado = esPalindromo(cadena)
        #al corresponder la cadena con un palíndromo la función devuelve True
        self.assertTrue(resultado)

    #comprobamos que la funcion devuelve True si una frase que contiene signos de puntuacion es palindroma
    def test_cadena_con_signos_puntuacion_es_palindroma(self):
        cadena='Anita. lava-- la t;ina'
        resultado = esPalindromo(cadena)
        #la función limpia todos los caracteres de puntuación de la cadena y al ser palíndroma devuelve true
        self.assertTrue(resultado)

    #comprobamos que la funcion devuelve false si una frase no es palindroma
    def test_cadena_no_es_palindroma(self):
        cadena='En un lugar de la mancha'
        resultado = esPalindromo(cadena)
        #al no ser palíndromo se espera que la función devuelva False
        self.assertFalse(resultado)

     #comprobamos que la funcion devuelve false si no introducimos ningún valor
    def test_cadena_vacia_no_es_palindroma(self):
        cadena=''
        resultado = esPalindromo(cadena)
        #al no ser palíndromo se espera que la función devuelva False
        self.assertFalse(resultado)
    
    
if __name__ == '__main__':
    unittest.main()