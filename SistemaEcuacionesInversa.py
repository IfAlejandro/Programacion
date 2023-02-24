# Se importa el modulo numpy para trabajar durante el desarrollo del ejercicio.
import numpy as np

# Esta funcion genera matrices al ser introducido la cantidad de filas y columnas deseada. Emplea bucles for para la generacion de la matriz.
def matrix_maker(rows,columns):

 matrix = []
 for x in range(rows):
    matrix.append([])
    for y in range(columns):
      value = int(input(f"introduzca los valoras de la fila {x+1}: \n"))
      matrix[x].append(value)

 return matrix

# Se utiliza un bucle for para que los valores de la matriz sean observados de forma mas amena en el terminal.
def show_matrix(matrix):

  for x in range(len(matrix)):
    print(result_matrix[x])

  return print("")

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
print(show_matrix(result_matrix))


