# -*- coding: utf-8 -*-
'''Requerimientos'''
# Capital Actual $300.000.000
# 2 Autos Usados de cada segmento
from datetime import *

class AutomovilNuevo (object):
    def __init__(self, Segmento, CodigoInventario, Marca, Modelo, NumeroChasis, Color, AñoFabricacion, PrecioCompra, PrecioVenta):
        self.__CodigoInventario=CodigoInventario
        self.__Segmento=Segmento
        self.__Marca=Marca
        self.__Modelo=Modelo
        self.__NumeroChasis=NumeroChasis
        self.__Color=Color
        self.__AñoFabricacion=AñoFabricacion
        self.__PrecioCompra=PrecioCompra
        self.__PrecioVenta=PrecioVenta
    
    def getCodigoInventario(self):
        return self.__CodigoInventario
    
    def getSegmento(self):
        return self.__Segmento
    
    def getMarca(self):
        return self.__Marca
    
    def getModelo(self):
        return self.__Modelo
    
    def getNumeroChasis(self):
        return self.__NumeroChasis
    
    def getColor(self):
        return self.__Color
    
    def getAñoFabricacion(self):
        return self.__AñoFabricacion
    
    def getPrecioCompra(self):
        return self.__PrecioCompra
    
    def getPrecioVenta(self):
        return self.__PrecioVenta
    
    #Ppu es placa patente Unica
class AutomovilUsado(AutomovilNuevo):
    def __init__(self, Segmento, CodigoInventario, Marca, Modelo, NumeroChasis, Color, AñoFabricacion, PrecioCompra, PrecioVenta, DueñoAnterior, Ppu, RevisionTecnica ):
        AutomovilNuevo.__init__(self, Segmento, CodigoInventario, Marca, Modelo, NumeroChasis, Color, AñoFabricacion, PrecioCompra, PrecioVenta)
        
        self.__DueñoAnterior=DueñoAnterior
        self.__Ppu=Ppu
        self.__RevisionTecnica=RevisionTecnica
        
    def getDueñoAnterior(self):
        return self.__DueñoAnterior
    
    def getPpu(self):
        return self.__Ppu
    
    def getRevisionTecnica(self):
        return self.__RevisionTecnica
def agregarAutoNuevo(AutoNuevo):
    Salvar=open('AutomotoraPayaso.txt','r',encoding='utf8')
    lAux2 = Salvar.readlines()
    lAux1 = []
    for m in range(len(lAux2)):
        if m == "------------------------------\n":
            continue
        else:
            lAux1.append(lAux2[m])
            #lAux1.append(m.split(":"))
        # lAux1.append(m)
    lAux1[1] = lAux1[1].split(":")
    for k in range (len(lAux1)):
        if lAux1[k][0] == " Capital":
            CapitalActual = lAux1[k][1]
        else:
           continue
    CapitalActual = CapitalActual.replace("\n", "")
    CapitalActual = CapitalActual.replace(" ", "")
    CapitalActual = int(CapitalActual) - int(AutoNuevo.getPrecioCompra())
    lAux1[1][0] = " Capital:"
    lAux1[1][1]=f" {CapitalActual}\n"
    Salvar.close()
    Salvar=open('AutomotoraPayaso.txt','w+',encoding='utf8')
    for n in range(len(lAux1)):
        Salvar.writelines(lAux1[n])
    Salvar.close()  
    ###############    
    # Salvar=open("AutomotoraPayaso.txt","r")
    # lLineas = Salvar.readlines()
    # for k in lLineas:
    #     if k == " Capital: 300000000\n":
    #         CapitalActual = k
    #     else:
    #        continue
    # CapitalActual = CapitalActual.replace(" Capital:", "")
    # CapitalActual = CapitalActual.replace("\n", "")
    # CapitalActual = int(CapitalActual) - int(AutoNuevo.getPrecioCompra())
    # lLineas[1]=f" Capital: {CapitalActual}\n"
    # Salvar=open("AutomotoraPayaso.txt","w+")
    # Salvar.writelines(lLineas)
    # Salvar.close()
    ################
    # Salvar=open('AutomotoraPayaso.txt','r',encoding='utf8')
    # lAux = []
    # for m in Salvar:
    #     if m == "------------------------------\n":
    #         continue
    #     else:
    #         lAux.append(m.split(":"))
    # for i in range (len(lAux)):
    #     lAux[i][1] = lAux[i][1].replace("\n", "")
    # for k in range (len(lAux)):
    #     if lAux[k][0] == " Capital":
    #         CapitalActual = lAux[k][1]
    #     else:
    #        continue
    # CapitalActual = CapitalActual.replace("\n", "")
    # CapitalActual = int(CapitalActual) - int(AutoNuevo.getPrecioCompra())
    # lAux[0][1]=f" {CapitalActual}\n"
    # Salvar=open("AutomotoraPayaso.txt","w+")
    # Salvar.writelines(lAux)
    # Salvar.close()    
    ################
    # Salvar=open('AutomotoraPayaso.txt','r',encoding='utf8')
    # lAux = []
    # for m in Salvar:
    #     if m == "------------------------------\n":
    #         continue
    #     else:
    #         lAux.append(m.split(":"))
    # print("1.-###")
    # print(lAux)
    # for i in range (len(lAux)):
    #     lAux[i][1] = lAux[i][1].replace("\n", "")
    # print("2.-###")
    # print(lAux)
    # for k in range (len(lAux)):
    #     if lAux[k][0] == " Capital":
    #         CapitalActual = lAux[k][1]
    #     else:
    #        continue
    # print("3.-###")
    # print(lAux)
    # CapitalActual = CapitalActual.replace(" ", "")
    # CapitalActual = int(CapitalActual) - int(AutoNuevo.getPrecioCompra())
    # lAux[0][1]=f" {CapitalActual}\n"
    # print(lAux[0][1])
    # print("4.-###")
    # print(lAux[0])
    # print("5.-###")
    # print(lAux)
    # Salvar=open("AutomotoraPayaso.txt","w+")
    # Salvar.writelines(lAux)
    # Salvar.close()  
    ################
    Salvar=open("AutomotoraPayaso.txt","a+")
    Salvar.writelines((" Segmento: ",AutoNuevo.getSegmento()))
    Salvar.writelines(("\n Codigo Inventario: ",AutoNuevo.getCodigoInventario()))
    Salvar.writelines(("\n Marca: ",AutoNuevo.getMarca()))
    Salvar.writelines(("\n Modelo: ",AutoNuevo.getModelo()))
    Salvar.writelines(("\n Chasis: ",AutoNuevo.getNumeroChasis()))
    Salvar.writelines(("\n Color: ",AutoNuevo.getColor()))
    Salvar.writelines(("\n Fecha de Fabricacion: ",AutoNuevo.getAñoFabricacion()))
    Salvar.writelines(("\n Precio de Compra: ",AutoNuevo.getPrecioCompra()))
    Salvar.writelines(("\n Precio de Venta: ",AutoNuevo.getPrecioVenta()))
    Salvar.writelines(("\n Tipo: Nuevo"))
    Salvar.writelines("\n------------------------------\n")
    Salvar.close()
    
def agregarAutoViejo(AutoViejo):

    Salvar=open('AutomotoraPayaso.txt','r',encoding='utf8')
    lAux2 = Salvar.readlines()
    lAux1 = []
    for m in range(len(lAux2)):
        if m == "------------------------------\n":
            continue
        else:
            lAux1.append(lAux2[m])
            #lAux1.append(m.split(":"))
        # lAux1.append(m)
    lAux1[1] = lAux1[1].split(":")
    for k in range (len(lAux1)):
        if lAux1[k][0] == " Capital":
            CapitalActual = lAux1[k][1]
        else:
           continue
    CapitalActual = CapitalActual.replace("\n", "")
    CapitalActual = CapitalActual.replace(" ", "")
    CapitalActual = int(CapitalActual) - int(AutoViejo.getPrecioCompra())
    lAux1[1][0] = " Capital:"
    lAux1[1][1]=f" {CapitalActual}\n"
    Salvar.close()
    Salvar=open('AutomotoraPayaso.txt','w+',encoding='utf8')
    for n in range(len(lAux1)):
        Salvar.writelines(lAux1[n])
    Salvar.close()  
    
    Salvar=open("AutomotoraPayaso.txt","a+")
    Salvar.writelines((" Segmento: ",AutoViejo.getSegmento()))
    Salvar.writelines(("\n Codigo Inventario: ",AutoViejo.getCodigoInventario()))
    Salvar.writelines(("\n Marca: ",AutoViejo.getMarca()))
    Salvar.writelines(("\n Modelo: ",AutoViejo.getModelo()))
    Salvar.writelines(("\n Chasis: ",AutoViejo.getNumeroChasis()))
    Salvar.writelines(("\n Color: ",AutoViejo.getColor()))
    Salvar.writelines(("\n Fecha de Fabricacion: ",AutoViejo.getAñoFabricacion()))
    Salvar.writelines(("\n Precio de Compra: ",AutoViejo.getPrecioCompra()))
    Salvar.writelines(("\n Precio de Venta: ",AutoViejo.getPrecioVenta()))
    Salvar.writelines(("\n Tipo: Usado"))
    Salvar.writelines(("\n Propietario Anterior: ",AutoViejo.getDueñoAnterior()))
    Salvar.writelines(("\n Placa Patente: ",AutoViejo.getPpu()))
    Salvar.writelines(("\n Fecha Proxima Revision Tecnica: ",AutoViejo.getRevisionTecnica()))
    Salvar.writelines("\n------------------------------\n")
    Salvar.close()
    
def obtenerDatos(chasis):
    archivo=open('AutomotoraPayaso.txt','r',encoding='utf8')
    #ELIMINAR SEPARADORES DE TEXTO
    l1 = []
    for x in archivo:
        if x == "------------------------------\n":
            continue
        else:
            l1.append(x.split(":"))
    #ELIMINAR SALTO DE LINEA
    for i in range (len(l1)):
        l1[i][1] = l1[i][1].replace("\n", "")
        
    for j in range(len(l1)):
        if l1[j][0] == " Tipo" and l1[j][1] == " Usado":
            if l1[j-5][0]==" Chasis":
                if l1[j-5][1]==str(chasis):
                    print("\n")
                    print(l1[j-8][0], ":", l1[j-8][1])
                    print(l1[j-7][0], ":", l1[j-7][1])
                    print(l1[j-6][0], ":", l1[j-6][1])
                    print(l1[j-5][0], ":", l1[j-5][1])
                    print(l1[j-4][0], ":", l1[j-4][1])
                    print(l1[j-3][0], ":", l1[j-3][1])
                    print(l1[j-2][0], ":", l1[j-2][1])
                    print(l1[j-1][0], ":", l1[j-1][1])
                    print(l1[j][0], ":", l1[j][1])
                    print(l1[j+1][0], ":", l1[j+1][1])
                    print(l1[j+2][0], ":", l1[j+2][1])
                    print(l1[j+3][0], ":", l1[j+3][1])
                    print("\n")
                    break
                elif l1[j-5][1]!=str(chasis):
                    continue
                else: 
                    print("El Chasis No Existe")
                    break
        elif l1[j][0] == " Tipo" and l1[j][1] == " Nuevo":
            if l1[j-5][0]==" Chasis":
                if l1[j-5][1]==str(chasis):
                    print("\n")
                    print(l1[j-8][0], ":", l1[j-8][1])
                    print(l1[j-7][0], ":", l1[j-7][1])
                    print(l1[j-6][0], ":", l1[j-6][1])
                    print(l1[j-5][0], ":", l1[j-5][1])
                    print(l1[j-4][0], ":", l1[j-4][1])
                    print(l1[j-3][0], ":", l1[j-3][1])
                    print(l1[j-2][0], ":", l1[j-2][1])
                    print(l1[j-1][0], ":", l1[j-1][1])
                    print(l1[j][0], ":", l1[j][1])
                    print("\n")
                    break
                elif l1[j-5][1]!=str(chasis):
                    continue  
        archivo.close()
        
def obtenerDueños(placa):
    archivo=open('AutomotoraPayaso.txt','r',encoding='utf8')
    #ELIMINAR SEPARADORES DE TEXTO
    l1 = []
    for x in archivo:
        if x == "------------------------------\n":
            continue
        else:
            l1.append(x.split(":"))
    #ELIMINAR SALTO DE LINEA
    for i in range (len(l1)):
        l1[i][1] = l1[i][1].replace("\n", "")
        
    for j in range(len(l1)):
        if l1[j][0] == " Tipo" and l1[j][1] == " Usado":
            if l1[j+1][0]==" Propietario Anterior":
                if l1[j+2][1]==str(placa): 
                    print(l1[j+1][0], ":", l1[j+1][1])
                    print(l1[j+2][0], ":", l1[j+2][1])
                    print(l1[j-7][0], ":", l1[j-7][1])
                    print(l1[j-6][0], ":", l1[j-6][1])
                    print("\n")
                elif l1[j+2][1]!=str(placa):
                    continue
                else: 
                    print("La placa no Existe")
                    break
        else:
            continue
    archivo.close()
    
def VenderAuto(codigoInventario):
    archivo=open('AutomotoraPayaso.txt','r',encoding='utf8') 
    l1 = []
    for x in archivo:
        if x == "------------------------------\n":
            continue
        else:
            l1.append(x.split(":"))
            
    for i in range (len(l1)):
        l1[i][1] = l1[i][1].replace("\n", "")
    aux = 0    
    for j in range(len(l1)):
        if l1[j][0] == " Tipo" and l1[j][1] == " Usado":
            if l1[j-8][0]==" Codigo Inventario":
                if l1[j-8][1]==str(codigoInventario):
                    aux = l1[j-1][1] 
                    aux = int(aux)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)  
                    break
                elif l1[j-8][1]!=str(codigoInventario):
                    continue
                else: 
                    print("El Auto no existe")
                    break
        elif l1[j][0] == " Tipo" and l1[j][1] == " Nuevo":
            if l1[j-8][0]==" Codigo Inventario":
                if l1[j-8][1]==str(codigoInventario):
                    aux = l1[j-1][1] 
                    aux = int(aux)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    l1.pop(j-9)
                    break
                elif l1[j-8][1]!=str(codigoInventario):
                    continue                
                else:
                    print("El Auto no existe")
                    break

    archivo2=open('AutomotoraPayaso.txt','w+',encoding='utf8')
    archivo2.write(f"------------------------------\n")
    for l in range(len(l1)):
        if l1[l][0] == " Fecha Proxima Revision Tecnica":
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
            #archivo2.write(f"------------------------------\n")
        elif l1[l][0] == " Segmento":
            archivo2.write(f"------------------------------\n")
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
        elif l1[l][0] == " Capital":
            archivo2.write(f"{l1[l][0]}: {aux+int(l1[l][1])}\n")
            aux = 0
        else:
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
    archivo2.write(f"------------------------------\n")
    
    archivo.close()
    archivo2.close()
     
def ActualizarPrecio(codigoInventario, precio):
    archivo=open('AutomotoraPayaso.txt','r',encoding='utf8')
    l1 = []
    for x in archivo:
        if x == "------------------------------\n":
            continue
        else:
            l1.append(x.split(":"))
            
    for i in range (len(l1)):
        l1[i][1] = l1[i][1].replace("\n", "")
           
    for j in range(len(l1)):
        if l1[j][0] == " Tipo" and l1[j][1] == " Usado":
            if l1[j-8][0]==" Codigo Inventario":
                if l1[j-8][1]==str(codigoInventario):
                    l1[j-1][1] = f" {precio}"
                    break
                elif l1[j-8][1]!=str(codigoInventario):
                    continue
                else: 
                    print("El Auto no existe")
                    break
        elif l1[j][0] == " Tipo" and l1[j][1] == " Nuevo":
            if l1[j-8][0]==" Codigo Inventario":
                if l1[j-8][1]==str(codigoInventario):
                    l1[j-1][1] = f" {precio}"
                    break
                elif l1[j-8][1]!=str(codigoInventario):
                    continue                
                else:
                    print("El Auto no existe")
                    break
                
    archivo2=open('AutomotoraPayaso.txt','w+',encoding='utf8')
    archivo2.write(f"------------------------------\n")
    for l in range(len(l1)):
        if l1[l][0] == " Fecha Proxima Revision Tecnica":
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
            #archivo2.write(f"------------------------------\n")
        elif l1[l][0] == " Segmento":
            archivo2.write(f"------------------------------\n")
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
        elif l1[l][0] == " Capital":
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
            aux = 0
        else:
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
    archivo2.write(f"------------------------------\n")
        
    archivo.close()
    archivo2.close()
    
def CalcularUtilidad():
    archivo=open('AutomotoraPayaso.txt','r',encoding='utf8')
    l1 = []
    for x in archivo:
        if x == "------------------------------\n":
            continue
        else:
            l1.append(x.split(":"))
            
    for i in range (len(l1)):
        l1[i][1] = l1[i][1].replace("\n", "")
    auxUsado = 0
    auxNuevo = 0       
    for j in range(len(l1)):
        if l1[j][0] == " Tipo" and l1[j][1] == " Usado":
            if l1[j-1][0]==" Precio de Venta":
                auxUsado = auxUsado + ((int(l1[j-1][1])-int(l1[j-2][1]))*0.75)
        elif l1[j][0] == " Tipo" and l1[j][1] == " Nuevo":
            if l1[j-1][0]==" Precio de Venta":
                auxNuevo = auxNuevo + ((int(l1[j-1][1])-int(l1[j-2][1]))*0.85)
    print("Utilidad De Venta De Autos Usados -->", int(auxUsado))
    print("Utilidad De Venta De Autos Nuevos -->", int(auxNuevo))
    
def AFRT(patente):
    archivo=open('AutomotoraPayaso.txt','r',encoding='utf8')
    l1 = []
    for x in archivo:
        if x == "------------------------------\n":
            continue
        else:
            l1.append(x.split(":"))
            
    for i in range (len(l1)):
        l1[i][1] = l1[i][1].replace("\n", "")
        
    for j in range(len(l1)):
        if l1[j][0] == " Tipo" and l1[j][1] == " Usado":
            if l1[j+3][0] == " Fecha Proxima Revision Tecnica":
                if l1[j+2][1] == str(patente):
                    z = l1[j+3][1]
                    z = z.split("-")
                    z[0] = int(z[0])+1
                    z[0] = f" {z[0]}"
                    z = "-".join([str(item) for item in z])
                    l1[j+3][1] = z
                    break
                elif l1[j+2][1] != str(patente):
                    continue
                else:
                    continue
            elif l1[j+3][0] != " Fecha Proxima Revision Tecnica":
                pass
        else:
            continue       
    archivo2=open('AutomotoraPayaso.txt','w+',encoding='utf8')
    archivo2.write(f"------------------------------\n")
    for l in range(len(l1)):
        if l1[l][0] == " Fecha Proxima Revision Tecnica":
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
        elif l1[l][0] == " Segmento":
            archivo2.write(f"------------------------------\n")
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
        else:
            archivo2.write(f"{l1[l][0]}:{l1[l][1]}\n")
    archivo2.write(f"------------------------------\n")  

    archivo.close()
    archivo2.close()
    
def notificarRevisionTecnica():

    # Salvar=open('AutomotoraPayaso.txt','r',encoding='utf8')
    # lAux = []
    # for m in Salvar:
    #     if m == "------------------------------\n":
    #         continue
    #     else:
    #         lAux.append(m.split(":"))
    # for i in range (len(lAux)):
    #     lAux[i][1] = lAux[i][1].replace("\n", "")
    # for k in range(len(lAux)):
    #     if lAux[k][0] == " Capital":
    #         CapitalActual = lAux[k][1]
    #         print(f"{lAux[k][0]} disponible:{lAux[k][1]}")
    #     else:
    #        continue
    # print(lAux)
    
    ######################
    # Salvar=open('AutomotoraPayaso.txt','r',encoding='utf8')
    # lAux2 = Salvar.readlines()
    # lAux1 = []
    # for m in range(len(lAux2)):
    #     if m == "------------------------------\n":
    #         continue
    #     else:
    #         lAux1.append(lAux2[m])
    #         #lAux1.append(m.split(":"))
    #     # lAux1.append(m)
    # lAux1[1] = lAux1[1].split(":")
    # for k in range (len(lAux1)):
    #     if lAux1[k][0] == " Capital":
    #         CapitalActual = lAux1[k][1]
    #     else:
    #        continue
    # CapitalActual = CapitalActual.replace("\n", "")
    # CapitalActual = CapitalActual.replace(" ", "")
    # CapitalActual = int(CapitalActual) - 8000000
    # lAux1[1][0] = " Capital:"
    # lAux1[1][1]=f" {CapitalActual}\n"
    # Salvar.close()
    # Salvar=open('AutomotoraPayaso.txt','w+',encoding='utf8')
    # for n in range(len(lAux1)):
    #     Salvar.writelines(lAux1[n])
    # Salvar.close()  
    ######################    
    archivo=open('AutomotoraPayaso.txt','r',encoding='utf8')
    #ELIMINAR SEPARADORES DE TEXTO
    fechaHoy = datetime.now()
    l1 = []
    for x in archivo:
        if x == "------------------------------\n":
            continue
        else:
            l1.append(x.split(":"))
    #ELIMINAR SALTO DE LINEA
    for i in range (len(l1)):
        l1[i][1] = l1[i][1].replace("\n", "")
    
    for l in range(len(l1)):
        if l1[l][0] == " Tipo" and l1[l][1] == " Usado":
            if l1[l+3][0] == " Fecha Proxima Revision Tecnica":
                aux = l1[l+3][1]
                aux = aux.replace(" ", "")
                aux = datetime.strptime(aux, "%Y-%m-%d")
                fechaFinal = fechaHoy - aux 
                fechaFinal = str(fechaFinal).split(" ", 1)
                if len(fechaFinal) == 1:
                    fechaFinal[0] = 0
                else: 
                    fechaFinal.pop(1)
                fechaFinal = "".join([str(dia) for dia in fechaFinal])
                fechaFinal = int(fechaFinal)*-1
                if fechaFinal > 0 and fechaFinal <= 30:
                    print(f"""                    ╔═════════════════════════════════╗
                    ║ Revision Tecnica                ║
                    ║ N°Inventario -->{l1[l-8][1]}        ║
                    ║ Dias Restantes -->  {fechaFinal}          ║
                    ╚═════════════════════════════════╝""")
                    continue
                elif fechaFinal == 0:
                    print(f"""                    ╔═════════════════════════════════╗
                    ║ Revision Tecnica                ║
                    ║ N°Inventario -->{l1[l-8][1]}        ║
                    ║ Dias Restantes -->   !!HOY!!    ║
                    ╚═════════════════════════════════╝""")                    
                    continue
                else: 
                    continue
            else:
                continue
        else:
            continue
    archivo.close()


if __name__ =="__main__":
    print("Esta es la clase! Esto no se ejecuta")