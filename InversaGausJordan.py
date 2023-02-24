print("Problema 2. Inversion de matrices (gauss-jordan)")

# Importando la libreria de NumPy 
import numpy as np
import sys

# Se utiliza un bucle for para que los valores de la matriz sean observados de forma mas amena en el terminal.
def show_matrix(matrix):

  for x in range(len(matrix)):
    print(matrix[x])
  
  return

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

# Se imprime la Matriz Inversa
print("La matriz inversa sera: \n")
for x in range(order_matrix):
    for y in range(order_matrix, 2*order_matrix):
        print(matrix[x][y], end="\t")
    print()

print((matrix))


