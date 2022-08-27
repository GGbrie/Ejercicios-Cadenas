Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

-------------------------------------------------------------------------

frase = input("Introduzca una frase en minúsculas: ")
vocal = input("Introduce la vocal minúscula que quiera convertir en Mayúscula:  ")
print(frase.replace(vocal, vocal.upper()))
