
import json #libreria json

def abrirArchivo():
    datos=[]
    with open("precios.json", encoding="utf-8") as openfile:#esto es para abrir el json de precios
        datos=json.load(openfile)
    return datos
"""
jjj=abrirArchivo()
print(jjj)
"""
def openArchivo():
    miarchivo=[]
    with open("info.json", encoding="utf-8") as openfile:#esto es para abrir el json de info
        miarchivo=json.load(openfile)
    return miarchivo

def guardarArchivo(midato):
    with open("info.json", "w") as file:#esto es para guardar info en el json de info
        json.dump(midato,file)

def menu():#primer menú o principal
    print("==============PANCAMP=================\n"
      " ELIGE LA OPCIÖN A LA QUE QUIERES ACCEDER\n"
      "1. REGISTROS DE VENTAS\n"
      "2. REGISTROS DE COMPRAS\n"
      "3. GENERACION DE INFORMES \n"
      "4. VER PRODUCTOS\n"
      "5. SALIR\n"
      "========================================")
    
def genrinfo():#segundo menú
    print("==============PANCAMP=================\n"
      " ELIGE LA OPCIÖN A LA QUE QUIERES ACCEDER\n"
      "1. INFORMES DE VENTAS\n"
      "2. INFORMES DE STOCK \n"
      "3. SALIR\n"
      "========================================")
def menuproduct():#tercer menú
    print("==============PRODUCTOS=================\n"
      " ELIGE LA OPCIÖN A LA QUE QUIERES ACCEDER\n"
      "1. PANADERIA\n"
      "2. PASTELERIA\n"
      "3. BEBIDAS\n"
      "4. PROMOCIONES\n"
      "5. SALIR\n"
      "========================================")
    
info=openArchivo()
product=abrirArchivo()
booleanito=True
while booleanito==True:
    menu()#abre el primer menú
    print("Elige una opción por favor")
    opc=int(input())
    
    if opc==1:

        info=openArchivo()
        #pide info para agregar cada registro de venta
        print("============REGISTRO DE VENTAS============\n")  
        fecha=input("ingrese la fecha :  ")
        usuario=input("ingrese el nombre de usuario : ")
        direccion=input("ingrese la dirección : ")
        Nameencargado=input("ingrese el nombre del encargado : ")
        cargo=input("ingrese el cargo : ")
        producto=input("ingrese el nombre del producto :  ")
        cantidad=int(input("ingrese la cantidad :  "))
        precio=int(input("ingrese el precio del producto : "))

        valort=precio*cantidad#lo utilice para calcular el valor total de la compra
        print("======================================")
        info[0]["recibosventas"].append({"Fecha":fecha,"Usuario":usuario,"Direccion":direccion, "Nombre del encargado":Nameencargado, "Cargo":cargo, "Producto":producto, "Cantidad":cantidad ,"Precio":precio, "Precio total":valort})
        print("Se ha creado con exito!!")
        guardarArchivo(info)
    if opc==2:
        info=openArchivo()
        #pide la info para crear los registrod de compras
        print("============REGISTRO DE COMPRAS============\n")  
        fecha=input("Fecha de compra:  ")
        proveedor=input("Nombre del proveedor: ")
        contacto=input("Número de conctacto: ")
        producto=input("Nombre del producto comprado :  ")
        cantidad=int(input("Cantidad del producto :  "))
        precio=int(input("Precio individual: "))
        valort=precio*cantidad
        print("======================================")

        info[0]["recibosCompras"].append({"Fecha":fecha,"Proveedor":proveedor,"Conctacto":contacto, "Producto":producto, "Cantidad":cantidad ,"Precio":precio, "Precio total":valort})
        print("Se ha creado con exito!!")
        guardarArchivo(info)#guarda la informacion anterior en el json
    if opc==3:
        this=True
        while this==True:
            genrinfo()#muetra el segundo menú
            print("Elige una opción por favor")
            opci=int(input())
            if opci==1:
                
                another=True
                while another==True:
                    info=openArchivo()#le da la opción al usuario de busca por fecha especifica o ver todo los informes de ventas
                    print("==============INFORMES DE VENTAS==============")
                    print("Si buscas los informes de una fecha en especifico escribe (ver)\n"
                            "si de lo contrario quieres verlos todos escribe (all) y (s) para salir")
                    elección=input()
                    #muestra los informes por fechas especificas
                   
                    if elección=="ver":
                        punch=True
                        while punch==True:
                            cell=0
                            print("Ingrese la fecha de las ventas que busca")
                            fordate=input()
                            print("")
                            for i in info[0]["recibosventas"]:
                                if i["Fecha"]==fordate:
                                    cell=1 
                                    print("=========================================================")
                                    print("Fecha:  ",i["Fecha"])
                                    print("Producto:  ",i["Producto"])
                                    print("Cantidad vendida:  ",i["Cantidad"])
                                    print("Precio:  ",i["Precio"])
                                    print("Precio Total:  ",i["Precio total"])
                                    print("=========================================================")
                                    print("")
                                    punch=False
                            if cell==0:
                                print("No hay registro de venta con esta fecha")

                                  
                    #muestra todo los informes   
                    if elección=="all":
                        for i in info[0]["recibosventas"]:
                            print("=========================================================")
                            print("Fecha:  ",i["Fecha"])
                            print("Producto:  ",i["Producto"])
                            print("Cantidad vendida:  ",i["Cantidad"])
                            print("Precio:  ",i["Precio"])
                            print("Precio Total:  ",i["Precio total"])
                            print("=========================================================")
                            print("")

                    if elección=="s":
                        print("regresando al menú anterior...")
                        another=False

            if opci==2:
                #muestra los informes de compra
                info=openArchivo()
                print("==============INFORMES DE COMPRAS==============")      
                for i in info[0]["recibosCompras"]:
                    print("=========================================================")
                    print("Producto:  ",i["Producto"])
                    print("Cantidad stock:  ",i["Cantidad"])
                    print("=========================================================")
                    print("")
            if opci==3:
                print("regresando al menú principal...")
                this=False
                
    if opc==4:
        #esta opción muestra todo los productos  que hay para vender or sesiones
        kameha=True
        while kameha==True:
            print("")
            menuproduct()
            print("elige una opción ")
            choose=int(input())
            print("")
            if choose==1:
                print("======PANADERIA======")
                for i in product["Panaderia"]:
                    print(i)
            if choose==2:
                print("======PASTELERIA======")
                for i in product["Pasteleria"]:
                    print(i)
            if choose==3:
                print("======BEBIDAS======")
                for i in product["Bebidas"]:
                    print(i)
            if choose==4:
                print("======PROMOCIONES======")
                for i in product["Apartado de promociones"]:
                    print(i)
            if choose==5:
                print("")
                print("regresando al menú principal...")
                kameha=False


    if opc==5:#finaliz el programa
        print("Saliendo del programa...")
        booleanito=False

    #desarrollado por Botello Garcia Yurley t.i: 1066085539
                                
        
                





