print ("Problema I")

amount_of_numbers = int(input("Introduzca un numero:\n"))

digit = 0
digit_operation = 0
result = 0
counter = 0
cycling_number = 0
value = amount_of_numbers

if amount_of_numbers <= 1:
   print ("N = 0")

else: 

 for number in range(2,amount_of_numbers):

   cycling_number = number

   while cycling_number != 89 or cycling_number != 1:

     operation_value = cycling_number
    
     while operation_value != 0:

        if operation_value > 10: 
          
          digit = operation_value % 10
          digit_operation = digit ** 2 
          result = digit_operation + result
          operation_value //= 10
          cycling_number = result

        else:
          digit = operation_value
          digit_operation = digit ** 2 
          operation_value //= 10
          result = digit_operation + result
      
     cycling_number = result
  
   if cycling_number == 89:
     counter += 1
      

result = str(counter*100/amount_of_numbers)
      
print (result+"%")

