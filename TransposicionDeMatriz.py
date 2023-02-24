def matrix_maker(rows,columns):
 matrix = []
 for x in range(rows):
    matrix.append([])
    for y in range(columns):
      value = int(input(f"introduzca los valoras de la fila {x+1}: \n"))
      matrix[x].append(value)
 return matrix

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

print (matrix)

for x in range(len(transposed_matrix)):
 print(transposed_matrix[x])

