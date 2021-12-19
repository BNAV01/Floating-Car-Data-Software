# -*- coding: utf-8 -*-
#Main 
import Requerimientos as Rq
Salvar=open("AutomotoraPayaso.txt","a+")

a = 0
#Alerta de Revision Tecnica

while(a!=10):
    Rq.notificarRevisionTecnica()
    print("Opción 0 Para Ingresar Un Auto Nuevo")
    print("Opción 1 Para Ingresar Un Auto Usado")
    print("Opción 2 Para Verificar Stock Por Marca")
    print("Opción 3 Para Verificar Stock por Segmento")
    print("Opción 4 Para Vender Vehiculo")
    print("Opción 5 Para Ver Historial de Dueños De Un Auto Usado")
    print("Opción 6 Para Obtener Datos Del Vehiculo Mediante Numero De Chasis")
    print("Opción 7 Para Actualizar Precio Del Vehiculo")
    print("Opción 8 Para Actualizar Fecha De Revision Tecnica")
    print("Opción 9 Para Conocer La Utilidad Total")
    print("Opcion 10 Para Salir")
    a=int(input("Ingrese una opción-->"))
    # Ingresar Un Auto Nuevo
    if(a==0):
        
        print("-------------------------------------------------")
        print("Segmentos de autos")
        print("1. Microcoche/Kei car")
        print("2. Segmento A / Coche de ciudad / Minicompacto")
        print("3. Segmento B / Supermini / Subcompacto")
        print("4. Segmento C / Compacto / Familiar pequeño")
        print("5. Segmento D / Familiar / Mediano")
        print("6. Segmento E / Ejecutivos / Automóvil largo")
        print("7. TodoTerreno")
        print("8. SUV crossover")
        print("9. Automóvil deportivo")
        print("10. Furgoneta")
        print("11. Camioneta")
        print("-------------------------------------------------")

        Segmento=input("Ingrese Segmento del auto-->")
        Codigo=input("Ingrese Codigo de Inventario-->")
        Marca=input("Ingrese Marca-->")
        Modelo=input("Ingrese Modelo-->")
        Chasis=input("Ingrese Numero de Chasis-->")
        Color=input("Ingrese Color del auto-->")
        Fabricacion=input("Ingrese Año de Fabricacion-->")
        Compra=input("Ingrese Precio de Compra-->")
        Venta=input("Ingrese Precio de Venta-->")
        An=Rq.AutomovilNuevo(Segmento, Codigo, Marca, Modelo, Chasis, Color, Fabricacion, Compra, Venta)
        Rq.agregarAutoNuevo(An)

    elif(a==1):
        #Ingresar Un Auto Usado
        print("-------------------------------------------------")
        print("Segmentos de autos")
        print("1. Microcoche/Kei car")
        print("2. Segmento A / Coche de ciudad / Minicompacto")
        print("3. Segmento B / Supermini / Subcompacto")
        print("4. Segmento C / Compacto / Familiar pequeño")
        print("5. Segmento D / Familiar / Mediano")
        print("6. Segmento E / Ejecutivos / Automóvil largo")
        print("7. TodoTerreno")
        print("8. SUV crossover")
        print("9. Automóvil deportivo")
        print("10. Furgoneta")
        print("11. Camioneta")
        print("-------------------------------------------------")
        
        #Salvar.writelines(("------------------------------\n"))
        Segmento=input("Ingrese Segmento del auto-->")
        Codigo=input("Ingrese Codigo de Inventario-->")
        Marca=input("Ingrese Marca-->")
        Modelo=input("Ingrese Modelo-->")
        Chasis=input("Ingrese Numero de Chasis-->")
        Color=input("Ingrese Color del auto-->")
        Fabricacion=input("Ingrese Fecha de Fabricacion-->")
        Compra=input("Ingrese Precio de Compra-->")
        Venta=input("Ingrese Precio de Venta-->")
        Dueño=input("Ingrese Propietario Anterior-->")
        Ppu=input("Ingrese Placa Patente-->")
        Revision=input("Ingrese Proxima Fecha de Revision Tecnica-->")
        Av=Rq.AutomovilUsado(Segmento, Codigo, Marca, Modelo, Chasis, Color, Fabricacion, Compra, Venta, Dueño, Ppu, Revision)
        Rq.agregarAutoViejo(Av)

    elif(a==2):
        #Verificar Stock Por Marca
        Rq.verificarStockPorMarca()
    
    elif(a==3):
        #Verificar Stock Por Segmento
        Rq.verificarStockPorSegmento()
        
    elif(a==4):
        #Para Vender Vehiculo
        borrar=input("Ingrese Codigo De Inventario Del Auto A Vender-->")
        borrar=f" {borrar}"
        Rq.VenderAuto(borrar)
       
    elif(a==5):
        #Historial de Dueños De Un Auto Usado
        Patente=input("Ingrese Patente Del Auto Para Saber Su Dueño Anterior-->")
        Patente=f" {Patente}"
        Rq.obtenerDueños(Patente)
    elif(a==6):
        #Obtener Datos Del Vehiculo Mediante Numero De Chasis
        chasis=input("Ingrese El Numero De Chasis A Buscar-->")
        chasis = f" {chasis}"
        Rq.obtenerDatos(chasis)
            
    elif(a==7):
        #Actualizar Precio Del Vehiculo
        Codigo=input("Ingrese Codigo De Inventario Del Auto A Vender-->")
        Precio=int(input("Ingrese Nuevo Precio Del Auto Elegido-->"))
        Codigo=f" {Codigo}"
        Rq.ActualizarPrecio(Codigo, Precio)
    
    elif(a==8):
        #Actualizar Fecha De Revision Tecnica
        Placa=input("Ingrese La Patente Del Vehiculo A Actualizar La Fecha De Revision Tecnica-->")
        Placa=f" {Placa}"
        Rq.AFRT(Placa)
        
    elif(a==9):
        #Conocer La Utilidad Total
        Rq.CalcularUtilidad()
    elif(a==10):
        print("Saliendo del programa\n")
        print("""                    88 88                        
                    88 ""                        
                    88                           
,adPPYYba,  ,adPPYb,88 88  ,adPPYba,  ,adPPYba,  
""     `Y8 a8"    `Y88 88 a8"     "8a I8[    ""  
,adPPPPP88 8b       88 88 8b       d8  `"Y8ba,   
88,    ,88 "8a,   ,d88 88 "8a,   ,a8" aa    ]8I  
`"8bbdP"Y8  `"8bbdP"Y8 88  `"YbbdP"'  `"YbbdP"'  
              """)
        break
    else:
        print("Opcion No Valida")
        
    print("-------------------------------------------------")  

Salvar.close()