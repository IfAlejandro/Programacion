print("Problema II")

print(" ")

number_of_terms = int(input("Ingrese la cantadidad de terminos a ejecutar:\n"))

result = 0

if number_of_terms == 1:
 
 result= (1/(1**6))
 
elif number_of_terms % 2 == 0 and number_of_terms > 0: 
 
 cicle_number= int(number_of_terms/2)
 sum_count = -1

 for i in range(1,cicle_number+1):
   sum_count +=1
   result = float(result + (1/((i+sum_count)**6)) - (1/((i+1+sum_count)**6)))
   
elif number_of_terms%2 !=0 and number_of_terms > 0: 

 value_even = 0 
 cicle_number= int((number_of_terms-1)/2)
 sum_count = -1

 for i in range(1,cicle_number+1):
   sum_count +=1
   value_even = float(value_even + (1/((i+sum_count)**6)) - (1/((i+1+sum_count)**6)))

 value_odd = float(1/((number_of_terms)**6))

result = value_even + value_odd

print (f"El resultado de la serie con {number_of_terms} terminos será")

print (result)

print(" ")


print ("Problema III")

print(" ")

number_of_rows_and_columns = int(input("Introduzca un numero de filas y columnas par:\n"))

value_numbers  = 0

matrix = []

list = []

counter_one = 0

counter_two= 0

for r in range(1,number_of_rows_and_columns+1):
  list = []

  for c in range(1,number_of_rows_and_columns+1):
    value_numbers  += 1
    list.append(value_numbers )

  matrix.append(list) 

value_numbers  = 0

for r in range(1,number_of_rows_and_columns+1):
  list = []
  
  for c in range(1,number_of_rows_and_columns+1):
    value_numbers += 1
    list.append(value_numbers )

  if r % 2 != 0:
    matrix [counter_one] = list 
    counter_one += 1

  elif r % 2 == 0: 
    counter_two -= 1
    matrix[counter_two] = list 

print (matrix)


 



