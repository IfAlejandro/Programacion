print ("Problema I")

num_ale= int(input("Ingrese la cantidad de número aleatorio que desea generar: ")) 
num_semi= int(input("Ingrese un valor inicial de al menos 4 digitos: "))

def medi(tam,num_semi):    #Funcion para sustraer los 4 numeros centrales.
    lim_s = tam // 2
    lim_i = tam + lim_s
    return str(num_semi)[-lim_i:-lim_s]

def cuadra_medi(num_ale,num_semi):      #Funcion para generar numeros aleatorios
    tam = len(str(num_semi))
    list_alea = []
    for i in range(num_ale): 
        num_semi = num_semi**2
        medi_1 = medi(tam,num_semi)
        #num_semi = int(medi_1)
        list_alea.append(float("0." + medi_1))
    return list_alea

coun = 1
while len(str(num_semi)) < 4 :
    num_semi = input("Vuelva a ingresar un valor:")
    coun += 1
    if coun == 4 :
        print("Ha alcanzado el limite de intentos")
        break

else:
    list = cuadra_medi(num_ale,num_semi)
    print(list)

print(" ")


print("Problema II")


print(" ")

total_high = int(input("Introduzca la profundidad del pozo:\n"))

ascended_distance = int(input("Introduzca la distancia que asciende el caracol:\n"))

descended_distance= int(input("Introduzca la distancia que desciende el caracol:\n"))

days_counter= 1

distance_reached=int((ascended_distance - descended_distance))

if distance_reached <= 0:
 print("El caracol no logrará salir del pozo")
 sys.exit()

while distance_reached < total_high:

 days_counter += 1
 distance_reached=int((ascended_distance - descended_distance) * days_counter)

print(f"Al caracol le tomará {days_counter} días salir del pozo")

print(" ")


print ("Problema III")


print(" ")

number_of_rows = int(input("Introduzca un numero de filas:\n"))

number_of_columns = int(input("Introduzca un numero de columnas:\n"))

matrix = []

last_value_even_row = 0

last_value_odd_row = 0

value = 0

for rows in range(1,number_of_rows + 1):
  list = []
  if rows % 2 != 0:
    for columns in range(1,number_of_columns + 1):
      list.append(last_value_even_row + columns)
      
    matrix.append(list)
    last_value_odd_row = list[-1]
  
  if rows % 2 == 0:
    for columns in range(1,number_of_columns + 1):
      list.append(last_value_odd_row + columns)
      
    list= list[::-1]  
    matrix.append(list)
    last_value_even_row = list[0]

print (matrix)

