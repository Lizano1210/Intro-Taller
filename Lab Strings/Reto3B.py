#Elaborado por: Joshua Brenes
#Fecha de Creaci—n: 26/04/2025 12:36
#œltima modificaci—n: 26/04/2025 18:33
#versi—n de python: 3.10.12

import re

def DecodificarNeum‡ticos(entrada):
    """
    """
    soporte=''
    radial=''
    if entrada[-1]== "T":
        soporte= int(500)
    if entrada[-1]== "V":
        soporte=int(545)
   
    if entrada[5]=="D":
        radial= "diagonal"
    if entrada[5]== "R":
        radial= "radial"
    if entrada[8:10]== "84":
        velocidad=int(190)
        return "El ancho de la llanta que usa su veh’culo es: 165 mil’metros"\
                "Para un 70% de la relaci—n altura y ancho"\
                   f"Con construcci—n {radial} " \
                   "Su di‡metro es de 14 pulgadas " \
                   f"Su ’ndice de carga es de 84, por ende, permite un soporte de {soporte} kg" \
                   f"Cuidado, la velocidad m‡xima que soporta su llanta es de {velocidad} Km/h"
    if entrada[8:10]== "87":
        velocidad=int(240) 
        return "El ancho de la llanta que usa su veh’culo es: 195 mil’metros"\
                   "Para un 55% de la relaci—n altura y ancho" \
                   f"Con construcci—n {radial} " \
                   "Su di‡metro es de 16 pulgadas " \
                   f"Su ’ndice de carga es de 87, por ende, permite un soporte de {soporte} kg" \
                   f"Cuidado, la velocidad m‡xima que soporta su llanta es de {velocidad} Km/h"
       
    return

def DecodificarNeum‡ticosAux(entrada):
    """
    """
    if entrada[-1] != "R" and len(entrada) != 11: #Caracteres
        return "El c—digo indicado no corresponde a una lectura correcta de un neum‡tico."
    if re.match('^[D,R]+$', entrada[5]) is None: #Radial o Diagonal
        return "La construcci—n del radial es incorrecta para poder decodificar el neum‡tico. "
    if re.match('^(84|87)$', entrada[8:10]) is None: #Capacidad de carga
        return "La capacidad de carga es incorrecta para poder decodificar el neum‡tico."
    return DecodificarNeum‡ticos(entrada)

def DecodificarNeum‡ticosES():
    """
    """
print(DecodificarNeum‡ticosAux("16570R1484T"))
print(DecodificarNeum‡ticosAux("19555D1687V"))
print(DecodificarNeum‡ticosAux("19555D1687AA"))
print(DecodificarNeum‡ticosAux("19555B1687ZR"))
print(DecodificarNeum‡ticosAux("16570R1450T"))

#Programa principal
DecodificarNeum‡ticosES()