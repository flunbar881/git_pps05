#charfun.py

#importación de librerias
import os #libreria de funciones de gestión de sistema operativo 
import re #libreria de funciones de gestión de expresiones regulares


#función principal del script
def init():
    # Para limpiar la consola
    os.system('cls')

    frase = input("Por favor introduzca la frase a analizar: ")
    #listado de signos de puntuación permitidos
    signos_puntuacion = ['.', ',', ';', ':', '!', '¡', '?', '¿', '\'', '"']
    #verifica que la frase contenga solo letras del alfabeto, espacios, alguno de los signos de puntuación admitidos y que no contenga sólo espacios en blanco
    while not (frase.strip() != '' and all(chr.isalpha() or chr.isspace() or chr in signos_puntuacion for chr in frase)):
        frase = input("No es una cadena con un formato válido. Introduzca una frase válida: ")

    #comprobamos si es palíndroma
    if esPalindromo(frase):
        print ("La frase SI es palíndroma")
    else:
        print ("La frase NO es palíndroma")


#función para comprobar si un texto es palíndromo
def esPalindromo(cadena):

    #limpiamos la cadena y dejamos solo los caracteres alfabéticos mediante una expresión regular
    cadena_limpia = re.sub("[^A-Za-z]", '', cadena) 
   
    #lInvertimos la cadena
    cadena_invertida = "".join(reversed(cadena_limpia))

    isPalindromo = False
    #comprobamos que la cadena limpia es igual a la invertida y que no son una cadena vacía
    if cadena_limpia.lower() == cadena_invertida.lower() and cadena_limpia.strip() != '':
        isPalindromo = True 

    return isPalindromo


#Lanza la funcion principal del script
if __name__ == '__main__':
    init()

 














