print ("Ejercicio 1")

first_word=input("Ingresar una palabra: ")

if " " in first_word:
 print("Error, no se ingreso una palabra: ")
 first_word=input("Ingresar una palabra nuevamente: ")

else:
 print(" ")

if (first_word.isnumeric())==True:
 print("Error, no se ingreso una palabra: ")
 first_word=input("Ingresar una palabra nuevamente: ")

second_word=input("Ingresar otra palabra: ")

if (second_word.isnumeric())==True:
 print("Error, no se ingreso una palabra: ")
 second_word=input("Ingresar una palabra nuevamente: ")

if (second_word.isspace())==True:
 print("Error, no se ingreso una palabra: ")
 second_word=input("Ingresar una palabra nuevamente: ")

if sorted(first_word)==sorted(second_word):
   print("Las palabras son un anagrama. ")

else:
   print("Las palabras no son un anagrama. ")

print ("Ejercicio 2")
  
first_oration=input("ingrese una oracion: ")

if (first_oration.isnumeric())==True:
 print("Error, no se ingreso una oracion: ")
 first_oration=input("Ingresar una oracion nuevamente: ")

if (first_oration.isnumeric())==True:
 print("Error, no se ingreso una oracion: ")
 first_oration=input("Ingresar una oracion nuevamente: ")

first_oration = first_oration.lower()

split_oration = first_oration.split(" ")
  
first_word = split_oration[0][0]

for i in range(1, len(split_oration)):
        individual_word = split_oration[i]
        if (individual_word[0] != first_word):
           print ("false")
           break
                 
else:
 print ("true")







 
