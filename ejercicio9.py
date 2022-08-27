Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

-------------------------------------------------------------

fecha = input("Introduce tu fecha de nacimiento en forma dd/mm/aaaa: ")
print('El Día es ', fecha[:2])
print('Del Mes', fecha[3:5])
print('Del Año', fecha[6:])
