Ejercicio 1
Escribir un programa que pregunte el nombre del usuario 
en la consola y un número entero e imprima por pantalla 
en líneas distintas el nombre del usuario tantas veces 
como el número introducido.

--------------------------------------------------------------------------

nombre = input("¿Cuál es tu nombre? ")
n = input("Introduce el número de veces que quieras que aparezca: ")
print((nombre + "\n") * int(n))

