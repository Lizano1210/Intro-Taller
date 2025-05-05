#Elaborado por: Joshua Brenes
#Fecha de Creación: 26/04/2025 12:36
#última modificación: 26/04/2025 20:00
#versión de python: 3.10.12

def DecodificarNeumáticos(entrada):
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
        return "El ancho de la llanta que usa su vehículo es: 165 milímetros"\
                "Para un 70% de la relación altura y ancho"\
                   f"Con construcción {radial} " \
                   "Su diámetro es de 14 pulgadas " \
                   f"Su índice de carga es de 84, por ende, permite un soporte de {soporte} kg" \
                   f"Cuidado, la velocidad máxima que soporta su llanta es de {velocidad} Km/h"
    if entrada[8:10]== "87":
        velocidad=int(240) 
        return "El ancho de la llanta que usa su vehículo es: 195 milímetros"\
                   "Para un 55% de la relación altura y ancho" \
                   f"Con construcción {radial} " \
                   "Su diámetro es de 16 pulgadas " \
                   f"Su índice de carga es de 87, por ende, permite un soporte de {soporte} kg" \
                   f"Cuidado, la velocidad máxima que soporta su llanta es de {velocidad} Km/h"
       
    return

def DecodificarNeumáticosAux(entrada):
    """
    """
    construcción=["R","D"]
    carga=["84","87"]
    if entrada[-1] != "R" and len(entrada) != 11: #Caracteres
        return "El código indicado no corresponde a una lectura correcta de un neumático."
    if entrada[5]not in construcción: #Radial o Diagonal
        return "La construcción del radial es incorrecta para poder decodificar el neumático. "
    if entrada[8:10]not in carga: #Capacidad de carga
        return "La capacidad de carga es incorrecta para poder decodificar el neumático."
    return DecodificarNeumáticos(entrada)

def DecodificarNeumáticosES():
    """
    """
    print(DecodificarNeumáticosAux("16570R1484T"))
    print(DecodificarNeumáticosAux("19555D1687V"))
    print(DecodificarNeumáticosAux("19555D1687AA"))
    print(DecodificarNeumáticosAux("19555B1687ZR"))
    print(DecodificarNeumáticosAux("16570R1450T"))

#Programa principal
DecodificarNeumáticosES()