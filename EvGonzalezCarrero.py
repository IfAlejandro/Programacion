print("Evaluacion Alejandro Gonzalez, Ederley Carrero")

import json

def add_product(product):
     new_product = {}

     price = input("Ingrese el precio del producto a agregar: \n")
     description = input("Ingrese una descripcion del producto a agregar: \n")
     
     new_product[product] = (price, description)
     tool_shop["Tools"][product] = (price, description)
  
     print(tool_shop)

     with open ("tool_shop.json", "w") as f:
        json.dump(tool_shop, f, indent = 2)
     
     return  print("Done")
   
def read_json(product_name):
   
     product_list = {}
     with open ("tool_shop.json", "r") as f:
          product_list = json.load(f)
     
     product_name = product_list["Tools"][product_name]
     print(product_name) 

     return print("Done")

def edit_product(product):
     
     with open ("tool_shop.json", "r") as f:   
       
       edit_product = {}
       
       price = input("Ingrese el precio del producto a agregar: \n")
       description = input("Ingrese una descripcion del producto a agregar: \n")
     
       edit_product[product] = (price, description)
       tool_shop["Tools"][product] = (price, description)
   
       print(tool_shop["Tools"][product])

     with open ("tool_shop.json", "w") as f:
       json.dump(tool_shop, f, indent = 2)
 
     return print("Done")
   
tool_shop = {"Tools": {"Martillo": ("15$","Pesa 5 kg")}}

# Se crea un json tool_shop
with open ("tool_shop.json", "w") as f:
     json.dump(tool_shop, f, indent = 2)


option = int(input("1- Agregar un Nuevo Producto. 2- Leer un Producto. 3- Editar un Producto. 4- Salir del programa: \n"))
x = 1

while x == 1:
# Agregar Producto
  if option == 1:

    product = input("Ingrese el nombre del producto a agregar: \n")
    new_product = add_product(product)
    option = int(input("1- Agregar un Nuevo Producto. 2- Leer un Producto. 3- Editar un Producto. 4- Salir del programa: \n"))

# Leer Producto
  elif option == 2:

    product = input("Ingrese el nombre del producto a leer: \n")
    print(read_json(product))
    option = int(input("1- Agregar un Nuevo Producto. 2- Leer un Producto. 3- Editar un Producto. 4- Salir del programa: \n"))

# Editar un producto
  elif option == 3:

    product = input("Ingrese el nombre del producto a editar: \n")
    print(edit_product(product))  
    option = int(input("1- Agregar un Nuevo Producto. 2- Leer un Producto. 3- Editar un Producto. 4- Salir del programa: \n"))

  elif option == 4:
    print("Adios")
    x = 0
    SystemExit
    

  elif option != 1 and option != 2 and option != 3 and option != 4:
    print("El numero suministrado es incorrecto. Intente nuevamente")
    option = int(input("1- Agregar un Nuevo Producto. 2- Leer un Producto. 3- Editar un Producto. 4- Salir del programa: \n"))

