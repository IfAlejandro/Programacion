#Ejercicio 1
num_1=0

while(num_1 <= 9 ):
    print(num_1)
    num_1 = num_1 + 1

#Ejercicio 2
num_2 = input("Ingrese un numero entero:")

try:
    num_2=int(num_2)
    acum = 0 
    k = 0
    while (k < num_2):
        k = k + 1
        acum = acum + k 
    print("La suma es:", acum)

except ValueError:
    print("Error no has ingreado un numero entero")