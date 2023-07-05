# # Ejercicio 1
# # 1. Elimina todos los VW de la siguiente lista. Crea una lista nueva para ello.
# # 2. Hazlo de otra manera. Crea una lista nueva, y ve añadiendo todos los que no sean VW
# # 3. En vez de `for`, usa un bucle `while`
# # > ejer_1 = ["VW", "Audi", "Renault", "VW", "BMW"]


# ejer_1 = ["VW", "Audi", "Renault", "VW", "BMW"]
# ejer_1_2 = ejer_1.copy()

# for i in ejer_1:
#     if i == "VW":
#         ejer_1_2.remove("VW")
        
# print(ejer_1_2)

# # ['Audi', 'Renault', 'BMW']

# ejer_1 = ["VW", "Audi", "Renault", "VW", "BMW"]

# result = []

# for i in ejer_1:
#     if i != "VW":
#         result.append(i)
        
# print(result)

# # ['Audi', 'Renault', 'BMW']

# ejer_1 = ["VW", "Audi", "Renault", "VW", "BMW"]

# result = []
# i = 0

# while i < len(ejer_1):
#     print(i)
        
#     if ejer_1[i] != "VW":
#         result.append(ejer_1[i])
        
#     i = i + 1

#     print(result)

# print("\nFin del bucle:", result)

# # 0
# # []
# # 1
# # ['Audi']
# # 2
# # ['Audi', 'Renault']
# # 3
# # ['Audi', 'Renault']
# # 4
# # ['Audi', 'Renault', 'BMW']

# # Fin del bucle: ['Audi', 'Renault', 'BMW']


# # Ejercicio 2
# # Imprime por pantalla la siguiente secuencia: 10, 9, 8.... -8, -9, -10

# for i in range(10, -11, -1):
#     print(i)
    
# # Ejercicio 3
# # 1. Escribe un programa que vaya pidiendo numeros al usuario. Cuando el usuario introduzca el 0, el programa tiene que imprimir por pantalla el sumatorio de todos los numeros positivos introducidos
# # 2. Además de la suma, queremos que imprima también una lista con todos los números.

# suma = 0
# num = None

# while num != 0:
#     num = int(input("Introduzca un numero del teclado"))
    
#     if num > 0:
#         suma += num
        
# print("El sumatorio de todos los enteros positivos fue de", suma)


# # Ejercicio 4
# # Escribir un programa que vaya pidiendo la cantidad de compras de un cliente. El programa tiene que pedir cantidades hasta que se ingresa un 0. Igualmente cuando una de las cantiaddes introducida es negativa, hay que mandar un mensaje de que "la cantidad es negativa, por favor introducir numeros positivos"

# ingreso = None
# suma = 0
# while ingreso != 0:
#     ingreso = int(input("Introduzca la cantidad de compra"))
    
#     if ingreso > 0:
#         suma += ingreso
#     else:
#         print("Numero negativo, por favor, introduzca un numero positivo")
# print("Total de compras", suma)

# Ejercicio 5
# Imprime por pantalla la palabra "Python", pero empezando con la última letra.

palabra = "Python"
for i in range(len(palabra) -1, -1, -1):
    print(palabra[i])
    

# Ejercicio 6
# Escribe un programa que calcule la cantidad de veces que está la letra "m" o "M" en la frase:
# > "En un lugar de La Mancha, de cuyo nombre no quiero acordarme"


frase = "En un lugar de La Mancha, de cuyo nombre no quiero acordarme"
count_m = 0
for i in frase.lower():
    if i == "m":
        count_m = count_m +1
print("Numero de veces que aparece m:", count_m)



# Ejercicio 7
# Crea un programa que simule la siguiente pirámide. Para ello, el programa tiene que pedirle al usuario un caracter cualquiera. El número de filas es fijo, 5. Vas a necesitar usar dos bucles anidados.

# W W W W W 

# W W W W 

# W W W 

# W W 

# W 


caracter = input("Introduzca un caracter")
num_filas = 5

for i in range(num_filas):
    
    for j in range(num_filas - i):
        print(caracter, end = " ")
    
    print("")
    


 # Ejercicio 8
#  Crea un programa que en función de un input numérico que inserte el usuario, imprima por pantalla la pirámide de ejemplo. Si el input es 6, tendrá 6 pisos, pero si introduce 10, la pirámide tendrá 10 pisos.
 
#  1 2 3 4 5 6
 
#  1 2 3 4 5
 
#  1 2 3 4
 
#  1 2 3
 
#  1 2
 
#  1

filas = int(input("Introduzca un numero"))

for i in range(filas):  
    
    out = ""
    for j in range(filas-i):
        out = out + " " + str(j + 1)
    print(out)
    
# Ejercicio 9
# Replica el siguiente patrón
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

n=5;
for i in range(n):
    for j in range(i):
        print ('*', end=" ")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*', end=" ")
    print('')
    
# Ejercicio 10
# Imprime toda la secuencia de numeros del 1 al 10, excepto el 3, 4 y 9. Impleméntalo de dos maneras diferentes

# una
for i in range(1,11):
    if i not in [3,4,9]:
        print(i)
        
# Dos
for i in range(1,11):
    if i != 3 and i != 4 and i != 9:
        print(i)
        
# Tres
for i in range(1, 11):
    if i in [3,4,9]:
        continue
        
    print(i)
    
    
    
# Ejercicio 11
# Suponiendo que siempre se cumple que las dos listas del ejercicio son iguales de tamaño, implementa un programa que calcule el ratio ingreso/gasto de cada elemento, y lo guarde en una nueva lista. Si hubiese algún problema con los datos, hay que almacenar un mensaje de error en la lista del resultado. Usa `try/except`
# > ingresos = [100, 200, 500, 100, 600]
# >
# > gastos = [50, 20, 70, 0, 25]

ingresos = [100, 200, 500, 100, 600]
gastos = [50, 20, 70, 0, 25]

ing_gasto = []

for i in range(len(ingresos)):
    try:
        ing_gasto.append(ingresos[i]/gastos[i])
        
    except ZeroDivisionError:
        print(ZeroDivisionError)
        ing_gasto.append(9999)
    
print(ing_gasto)


# Ejercicio 12
# Muy parecido al anterior, aunque ahora tendremos que excepcionar más tipos de errores con estos nuevos datos. En este caso, almacena un mensaje diferente en la lista resultado, para cada error.

# > ingresos = [100, "HHH", 500, 100, 600, 900, 150]
# >
# > gastos = [50, 20, 70, 0, 25]

ingresos = [100, "HHH", 500, 100, 600, 900, 150]
gastos = [50, 20, 70, 0, 25]

ing_gasto = []

for i in range(len(ingresos)):
    try:
        ing_gasto.append(ingresos[i]/gastos[i])
        
    except ZeroDivisionError:
        print(ZeroDivisionError)
        ing_gasto.append("Zero division error")
        
    except IndexError:
        print(IndexError)
        ing_gasto.append("Index Error")
        
    except TypeError:
        print(TypeError)
        ing_gasto.append("TypeError")
    
print(ing_gasto)