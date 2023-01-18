print ('Bienvenido a la Calculadora')

num1=int(input('Ingresar un Valor:'))

num2=int(input('Ingresar un Valor:'))

Operacion=input('Ingresar Operacion (+,-,*,/)')

if Operacion == '+':
    print(int(input(num1+num2)))

if Operacion == '-':
    print(int(input(num1-num2)))

if Operacion == '*':
    print(int(input(num1*num2)))

if Operacion == '/':
    print(int(input(num1/num2)))

while not Operacion == '+,-,*,/':
 print('Operacion Invalida. Intentos Restante (2)')
 break

Operacion=input('Ingresar Operacion (+,-,*,/)')

if Operacion == '+':
    print(int(input(num1+num2)))

if Operacion == '-':
    print(int(input(num1-num2)))

if Operacion == '*':
    print(int(input(num1*num2)))

if  Operacion == '/':
    print(int(input(num1/num2)))
    
while not Operacion == '+,-,*,/':
 print('Operacion Invalida. Intentos Restante (1)')
 break

Operacion=input('Ingresar Operacion (+,-,*,/)')

if Operacion == '+':
    print(int(input(num1+num2)))

if Operacion == '-':
    print(int(input(num1-num2)))

if Operacion == '*':
    print(int(input(num1*num2)))

if  Operacion == '/':
    print(int(input(num1/num2)))

while not Operacion == '+,-,*,/':
 print('Operacion Invalida. Intentos Restante (0)')
 break

print('Adios')
exit

