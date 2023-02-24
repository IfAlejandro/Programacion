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




