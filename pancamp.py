
import json 
import time
import os 
def abrirArchivo():
    datos=[]
    with open("precios.json", encoding="utf-8") as openfile:
        datos=json.load(openfile)
        print(datos)
    return datos
"""
jjj=abrirArchivo()
print(jjj)
"""
def openArchivo():
    miarchivo=[]
    with open("info.json", encoding="utf-8") as openfile:
        datos=json.load(openfile)
        print(miarchivo)
    return miarchivo

def guardarArchivo(midato):
    with open("info.json", "w") as file:
        json.dump(midato,file)

def menu():
    print("===============PANCAMP ==================\n"
      " Elige la opcion a la que quieres acceder\n "
      "1. Venta\n"
      "2. compras\n"
      "3. Generación de informes \n"
      "4. Salir\n"
      "=====================================")
miArchivo=[]
booleanito=True
while booleanito==True:
    menu()
    print("Elige una opción por favor")
    opc=int(input())
    
    if opc==1:
        print("============VENTAS============\n")  
        id=input("ingresa un id ")
        fecha=input("ingrese la fecha ")
        usuario=input("ingrese el nombre de usuario: ")
        direccion=input("ingrese la dirección: ")
        Nameencargado=input("ingrese el nombre del encargado: ")
        cargo=input("ingrese el cargo: ")
        producto=input("ingrese el nombre del producto:  ")
        cantidad=input("ingrese la cantidad:  ")
        miArchivo[0]["ventas"].append({"id":id,"fecha":fecha,"usuario":usuario,"direccion":direccion, "nameencargado":Nameencargado, "cargo":cargo, "producto":producto, "cantidad":cantidad})
        print("se ha creado con exito!!")
        guardarArchivo(miArchivo)
       

