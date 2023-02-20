with open("TextMatrix.txt","r") as archive:
 archive_lines = archive.readlines()
 number_of_rows = int(archive_lines[1])

archive.close()

number_of_columns = 2
matrix = []
last_value = 0

for rows in range(1,number_of_rows + 1):
  list = []
  if rows % 2 != 0:
    for columns in range(1,number_of_columns + 1):
      list.append(last_value + columns)
      
    list.append(list[0]+list[1])
    matrix.append(list)
    last_value = list[1]
  
  if rows % 2 == 0:
    for columns in range(1,number_of_columns + 1):
      list.append(last_value + columns)

    list.append(list[0]*list[1]) 
    matrix.append(list)
    last_value = list[1]

matrix_str = ""

for rows in range (number_of_rows):
    string = str(matrix[rows])
    matrix_str += string
    matrix_str += "\n"
    
with open("TextMatrix.txt","w") as archive:
    archive.write("Ingrese en la siguiente linea el numero de filas deseado:\n")
    archive.write(str(number_of_rows))
    archive.write("\n")
    archive.write("\n")
    archive.write("La matriz resultante sera:\n")
    archive.write("\n")
    archive.write(matrix_str)
    
archive.close()
