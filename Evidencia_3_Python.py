import pandas as pd
import sys
import sqlite3
import datetime
from datetime import date
from sqlite3 import Error
registro_ventas={}
venta_final= []
separador= "*********************************"
while True:
    print("\n***MENU***")
    print("1.- Registrar una venta")
    print("2.- Consultar una venta")
    print("3.- Reporte de venta")
    print("0.- Salir")
    opcion_usuario = int(input("Ingrese una opcion:  "))

    if opcion_usuario == 1:
        print("La forma en la que se presentan las listas es 1.- Descripcion, 2.- Cantidad de piezas vendidas, 3.- Precio")
        Brocha = ["Para la aplicación controlada del lápiz labial.",20,299.99]
        print ("Brocha")
        print (Brocha)
        print (separador)
        Labial = ["Powder Kiss. Formulado para colorear, definir y ostentar los labios.",22,199.99]
        print ("Labial")
        print (Labial)
        print (separador)
        Rimel = ["Máscara para pestañas a prueba de agua.",36,99.99]
        print ("Rimel")
        print (Rimel)
        print (separador)
        Base = ["Base que combina un acabado matte natural y cobertura media a total.",82,49.99]
        print ("Base")
        print (Base)
        print(separador)
        Corrector = ["Corrector líquido de cobertura media a matte de larga duración, 15 horas.",64,99.99]
        print ("Corrector de ojeras")
        print (Corrector)
        print (separador)
        opcion=1
        identificador = input("\nIngresa tu identificador: ")
        if identificador in  venta_final:
            print("\nEse identificador ya esta registrado, intenta con otro")
        else: 
            while opcion == 1: 
                nombr_articulo = input ("\nDime el nombre del producto: ")
                piezas_compradas= int(input("\nDime la cantidad de piezas compradas: "))
                precio_producto= float(input("\nDime el costo del producto: "))
                cantidad_total= piezas_compradas * precio_producto
                print("\nSu monto total a pagar es de $ ",cantidad_total)
                venta_producto= [nombr_articulo, piezas_compradas, precio_producto, round(cantidad_total, 2)]
                venta_final.append(venta_producto)
                opcion = int(input("\n ¿Deseas capturar otro articulo? \n(1-Si / 0-No): "))
            registro_ventas[identificador]=[venta_final]
            venta_final=[]
            numero = identificador
            numero_final = str(numero)
            fecha = date.today()
            fecha_final = fecha.strftime('%d%m%Y')
            folio = numero_final + fecha_final
            lista_folio = [folio]
            lista_identificador = [identificador]
            lista_producto = [nombr_articulo]
            lista_cantidad = [piezas_compradas]
            lista_preciou = [precio_producto]
            lista_preciot = [cantidad_total]
            dict = {"Folio" : lista_folio, "Identificador" : lista_identificador, "Producto" : lista_producto, "Cantidad" : lista_cantidad, "Precio unitario" : lista_preciou, "Precito total" : lista_preciot}
            df = pd.DataFrame(dict) 
            df.to_csv('Venta.csv')
            print ("Haz comprado ", lista_cantidad, "pieza(s) de ", lista_producto, "con un precio unitario de ", lista_preciou, "dando una cantidad total de ", lista_preciot)
            print ("Tu identificador es :", numero_final, "Y tu folio es: ", folio) 
    elif opcion_usuario == 2:
        id_buscar =(input("\nDime el identificador que quieres buscar: "))
        if id_buscar in registro_ventas.keys():
            print("\nLa venta con ese identificador es: ", identificador)
            productos_ticket=list(registro_ventas[identificador])
            listas=["Nombre", "Cantidad" , "Precio venta", "Precio total "]
            print(listas)
            for producto in range(0,len(productos_ticket)+1) : 
                print(productos_ticket[0][producto])
        else:
            print("\nLo siento, ese identificador no esta en la base de datos")
            
    elif opcion_usuario == 3:
        try:
             with sqlite3.connect("Evidencia3_Estructura.db") as conn:
                 print(sqlite3.version)
                 
                 mi_cursor = conn.cursor()
                 fecha_actual = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
                 datos = {"clave": 4, "nombre":"Fecha", "Fecha_Registro": fecha_actual}
                 query = (f"INSERT INTO PRODUCTO (CLAVE, Nombre) VALUES ({datos['clave']}, '{datos['nombre']}, '{datos['Fecha_Registro']}');")
                 
                 mi_cursor.execute(query, datos)
                 conn.comit()
                 print("El registro se agrego correctamente")
        except Error as e: 
            print (e) 
            
    elif opcion_usuario == 0:
        print ("Haz elegido salir. Gracias por tu preferencia.")
        break
    else: 
        print("Has introducido una opcion invalida")
        