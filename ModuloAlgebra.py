print ("Problema 1. Multiplicacion de matrices.")

# Esta funcion genera una matriz al ser introducido la cantidad de filas y columnas deseada. Emplea bucles for para la generacion de la matriz.
def matrix_maker(rows,columns):
 matrix = []
 for x in range(rows):
    matrix.append([])
    for y in range(columns):
      value = int(input(f"introduzca los valoras de la fila {x+1}: \n"))
      matrix[x].append(value)

 return matrix

# Se define una funcion que realiza el procedimento de multiplicar respectivamente dos matrices. Para esto utiliza condiciones y ciclos for 
# para generar e introducir los resultados a una nueva matrix multiplicacion.
def multiplication_matrix(matrix_1 , matrix_2):
  if len(matrix_1[0]) == len(matrix_2):
     matrix_multiplication = []

     for x in range(len(matrix_1)):
       matrix_multiplication.append([])
       for y in range(len(matrix_2[0])):
         matrix_multiplication[x].append(0) 

     for x in range(len(matrix_1)):
       for y in range(len(matrix_2[0])):
         for z in range(len(matrix_1[0])):
           matrix_multiplication[x][y] += matrix_1[x][z] * matrix_2 [z][y]
     
     return matrix_multiplication

  else:
     return None

# Se utiliza un bucle for para que los valores de la matriz sean observados de forma mas amena en el terminal.
def show_matrix(matrix):

  for x in range(len(matrix)):
    print(matrix[x])
  
  return print("")

# Se solicitan el numero de filas y columnas respectivamente.
number_of_rows = int(input("Introduzca el numero de filas para la matriz 1:\n"))
number_of_columns = int(input("Introduzca el numero de columnas para la matriz 1:\n"))

# Se genera una matriz con la funcion matrix_maker.
matrix_1 = matrix_maker(number_of_rows,number_of_columns)

# Se solicitan el numero de filas y columnas respectivamente.
number_of_rows = int(input("Introduzca el numero de filas para la matriz 2:\n"))
number_of_columns = int(input("Introduzca el numero de columnas para la matriz 2:\n"))

# Se genera una matriz con la funcion matrix_maker.
matrix_2 = matrix_maker(number_of_rows,number_of_columns)

# Se utiliza la funcion multiplication_matrix para generar una matriz matrix_multiplication siendo la resultante de matrix_1 y matrix_2.
matrix_multiplication = multiplication_matrix(matrix_1 , matrix_2)

# Se utiliza una condicionante if y un ciclo while para garantizar que las matrices generadas se pueden multiplicar. Dentro del ciclo while se
# colocan los procedimentos anteriores para asi generar otras matrices y poder multiplicarlas
if matrix_multiplication == None:
    while matrix_multiplication == None:
      print ("Las matrices no pueden ser multiplicadas.\n")
      number_of_rows = int(input("Introduzca el numero de filas para la matriz 1:\n"))
      number_of_columns = int(input("Introduzca el numero de columnas para la matriz 1:\n"))

      matrix_1 = matrix_maker(number_of_rows,number_of_columns)

      number_of_rows = int(input("Introduzca el numero de filas para la matriz 2:\n"))
      number_of_columns = int(input("Introduzca el numero de columnas para la matriz 2:\n"))

      matrix_2 = matrix_maker(number_of_rows,number_of_columns) 

      matrix_multiplication = multiplication_matrix(matrix_1 , matrix_2)
    
else:
  print("La matriz resultante sera: \n")
  # Se utiliza la funcion show_matrix para imprimir la matriz resultante.
  print(show_matrix(matrix_multiplication))

print("\n")
print("Problema 2. Inversion de matrices (gauss-jordan)")
print("\n")

# Importando la libreria de NumPy 
import numpy as np
import sys

# Solicitando el orden de la matriz
order_matrix = int(input("Enter order of matrix: \n"))

# Realizando un arreglo en numpy con el orden ingresado de forma n x 2n.Generando una matriz de ceros
matrix = np.zeros((order_matrix,2*order_matrix))


# Introduciendo los elementos de la matriz
print("Introduzca los valores de la matriz:\n")
for x in range(order_matrix):
    for y in range(order_matrix):
        matrix[x][y] = float(input( "matrix["+str(x)+"]["+ str(y)+"]=" ))

# Generando una matriz identidad del mismo orden que el de la matriz generada anteriormente.
for x in range(order_matrix):        
    for y in range(order_matrix):
        if x == y:
            matrix[x][y+order_matrix] = 1

# Se emplearon cilos for para simular el metodo matematico de eliminacion gauss-jordan. Los ciclos cambian los valores especificos de cada fila
# y columna respectivamente. Tambien utiliza condicionales para garantizar que no se divide entre cero durante la aplicacion del metodo.
for x in range(order_matrix):
    if matrix[x][x] == 0.0:
        sys.exit("Al realizar el metodo de eliminacion no se puede dividir entre 0")
        
    for y in range(order_matrix):
        if x != y:
            value = matrix[y][x]/matrix[x][x]

            for z in range(2*order_matrix):
                matrix[y][z] = matrix[y][z] - value * matrix[x][z]

# Operacion de filas para obtener una diagonas principal igual a 1. 
for x in range(order_matrix):
    divisor = matrix[x][x]
    for y in range(2*order_matrix):
        matrix[x][y] = matrix[x][y]/divisor

# Se imprime la Matriz Inversa solamente. 
print("La matriz inversa sera: \n")
for x in range(order_matrix):
    for y in range(order_matrix, 2*order_matrix):
        print(matrix[x][y], end="\t")
    print()

print("\n")
print("Problema 3. Producto Vectorial")
print("\n")

# Se define una funcion con el procedimiento matematico del producto vectorial. Esta toma en consideracion las tres cordenadas de dos vectores.
def cross_product(u,v):
    i_axis = u[1] * v[2] - u[2] * v[1]
    j_axis = u[2] * v[0] - u[0] * v[2]
    z_axis = u[0] * v[1] - u[1] * v[0]
    vector = [i_axis,j_axis,z_axis]

    return vector

vector_1 = []

# Se emplea un bucle for para introducir los valores del vector deseado.
for y in range(3):
  value = int(input("introduzca los valoras del primer vector: \n"))
  vector_1.append(value)

print(vector_1)

vector_2 = []

# Se emplea un bucle for para introducir los valores del vector deseado.
for y in range(3):
  value = int(input("introduzca los valoras del segundo vector: \n"))
  vector_2.append(value)

print(vector_2)

print("El producto vectorial sera igual a: \n")

# Se emplea la funcion creada con dos vectores deseados para optener su producto vectorial.
print(cross_product(vector_1,vector_2))

print("\n")
print("Problema 4. Transposicion de Matrices")
print("\n")

# Esta deficion emplea dos ciclos for para integrar los valores de una matriz ya existente a una nueva matriz transponiendo su orden a medida
# que ocurre cada bucle.
def transposed(matrix):
    transposed_matrix = []
    for x in range(len(matrix[0])):
        transposed_matrix.append([])
        for y in range(len(matrix)):
          transposed_matrix[x].append(matrix[y][x])
    
    return transposed_matrix

# Se utiliza la funcion matrix_maker para generar una matriz de un numero de filas y columnas especifico.
number_of_rows = int(input("Introduzca el numero de filas para la matriz 1:\n"))
number_of_columns = int(input("Introduzca el numero de columnas para la matriz 1:\n"))

# Se utiliza la deficion matrix_maker para generar una matriz.
matrix = matrix_maker(number_of_rows,number_of_columns)

print("La matriz transpuesta sera: \n")

# Se utiliza la deficion transposed_matrix para generar la matriz transpuesta.
transposed_matrix = transposed(matrix)

# Se utiliza la funcion show_matrix para imprimir la matriz transpuesta.
print(show_matrix(transposed_matrix))

print("\n")
print("Problema 5/ Resolucion de sistema de ecuaciones lineales (utilizando la funcion inversa)")
print("\n")

# Se introducen la cantidad de filas y columnas deseada.
number_of_rows = int(input("Introduzca el numero de filas para la matriz 1:\n"))
number_of_columns = int(input("Introduzca el numero de columnas para la matriz 1:\n"))

# Se utiliza la funcion matrix_maker para generar una matriz de un numero de filas y columnas especifico.
matrix_1 = matrix_maker(number_of_rows,number_of_columns)

number_of_rows = int(input("Introduzca el numero de filas para la matriz 2:\n"))
number_of_columns = 1

# La matrix_2 representa los valores del otro lado del igual de la ecuacion.
matrix_2 = matrix_maker(number_of_rows,number_of_columns)

# Se utilizara la extension numpy para obtener el valor de la inversa de la matrix_1. Este valor puede ser calculado con el mismo codigo
# Aplicado en el ejercicio 2 pero se busco optimizar este codigo.
inverse_matrix = np.linalg.inv(matrix_1)

# Se utiliza la extension numpy para multiplicar la matriz inverse_matrix con la matrix_2. Siguiendo la formulas establecidas para el metodo.
# Nuevamente se podria aplicar el codigo utilizado en el ejercicio 1 de multiplicacion de matrices pero se busco optimizar este codigo.

result_matrix = np.dot(inverse_matrix,matrix_2)

print("La resolucion de la ecuacion vendra dada por la matriz: /n")

# Se utiliza la funcion show_matrix para imprimir la matriz.
print(show_matrix(result_matrix))








