print("Problema 3")

# Importando la libreria de NumPy.
import numpy as np

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



