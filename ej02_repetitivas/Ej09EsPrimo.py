"""
Escribe un programa que diga si un número introducido por teclado es o no primo.
Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es
divisible por algún otro número.

Análisis
--------
Leemos un número y vamos comprobando si es divisible entre 2 hasta la raíz cuadrada del número.
Si es divisible por algún número no es primo.
Si no es divisible por ningún número es primo.
Para saber si es divisible usamos el operador módulo.

Datos de entrada: el número a comprobar si es primo o no.
Información de salida: Un mensaje diciendo si es primo o no.

Variables:
- num_a_comprobar (entero),
- num (entero) contador desde 2 hasta raíz cuadrada del num_es_primo
- creo_que_es_primo (lógico)

Diseño
------
1.- Supongo que el número es primo -> creo_que_es_primo<-Verdadero
2.- Leer num_es_primo
3.- Desde num = 2 hasta raíz(numero_es_primo)
4.- Si num_a_comprobar es divisible entre num -> creo_que_es_primo<-Falso
5.- Si creo_que_es_primo -> Mostrar "Es primo"
6.- Si no -> Mostrar "No es primo"
"""
import math

# Inicialización
creo_que_es_primo = True

# Pedimos datos
num_a_comprobar = int(input("Introduce un número para comprobar si es primo: "))

# Proceso
num = 2
while num <= math.sqrt(num_a_comprobar) and creo_que_es_primo:
    if num_a_comprobar % num == 0:
        creo_que_es_primo = False
    num += 1

# Mostramos resultado    
if creo_que_es_primo:
    print("Es Primo")
else:
    print("No es Primo")
