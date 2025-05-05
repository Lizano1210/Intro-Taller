#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Elaborado por: Elías Lizano, Joshua Brenes
Fecha de creación: 24/4/25 7:00p.m
Última modificación: 26/4/25 9:00p.m
Versión de Python: 3.12
"""

import re

# Reto 1A (Sin ER)
#Variables
diametro = ["3","4","5","6","8"]
pF = ["S","W"]
gradosAcero = ["40","60","70"]
     
def nomenclaturaVarillaAux(entrada):
    """
    Funcionamiento:
    Verifica que la entrada cumpla con el formato esperado para varillas, sin usar expresiones regulares.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Mensaje de error si la validación falla, o llama nomenclaturaVarilla si pasa.
    """    
    if len(entrada) != 6:
        return "Debe indicar 6 valores exactamente."
    
    if  entrada[0:2].isupper() == False:
        return "Las siglas de fabricante deben ser únicamente mayúsculas."
    
    if entrada[2] not in diametro:
        return "El diámetro de entrada no es un valor permitido."
    
    if entrada[3] not in pF:
        return "Debe ingresar un proceso de fabricación válido (S o W)"
    
    if entrada[4:] not in gradosAcero:
        return "El grado del acero no es un valor permitido."
    
    return nomenclaturaVarilla(entrada)

def decoDiametro(entrada):
    """
    Funcionamiento:
    Decodifica el diámetro de la varilla en función del tercer carácter de la entrada.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del diámetro de la varilla.
    """
    if entrada[2] == "3":
        return "El diámetro de la varilla es: 3/8 pulgadas."
    elif entrada[2] == "4":
        return "El diámetro de la varilla es: 1/2 pulgadas."
    elif entrada[2] == "5":
        return "El diámetro de la varilla es: 5/8 pulgadas."
    elif entrada[2] == "6":
        return "El diámetro de la varilla es: 3/4 pulgadas."
    elif entrada[2] == "8":
        return "El diámetro de la varilla es: 1 pulgadas."
    
def decopF(entrada):
    """
    Funcionamiento:
    Decodifica el proceso de fabricación basado en el cuarto carácter.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del proceso de fabricación.
    """
    if entrada[3] == "S":
        return "Proceso de Fabricación: Acero al carbono no soldable a temperatura ambiente."
    elif entrada[3] == "W":
        return "Proceso de Fabricación: Acero al carbono soldable a temperatura ambiente."
    
def decogA(entrada):
    """
    Funcionamiento:
    Decodifica el grado del acero basado en los dos últimos caracteres.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del grado del acero.
    """
    if entrada[4:] == "40":
        return "Grados de acero: 2800kgf/cm2."
    elif entrada[4:] == "60":
        return "Grados de acero: 4200kgf/cm2."
    elif entrada[4:] == "60":
        return "Grados de acero: 5000kgf/cm2."
    

def nomenclaturaVarilla(entrada):
    """
    Funcionamiento:
        Imprime la decodificación completa de la nomenclatura de varillas.

    Entradas:
        entrada (str): Código a decodificiar.

    """
    print("El fabricante es: ", entrada[0:2])
    print(decoDiametro(entrada))
    print(decopF(entrada))
    print(decogA(entrada))
    
    return ""

# Reto 1B (Con ER)
def nomenclaturaVarillaAuxB(entrada):
    """
    Funcionamiento:
    Verifica que la entrada cumpla con el formato esperado para varillas usando expresiones regulares.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Mensaje de error si la validación falla, o llama nomenclaturaVarilla si pasa.
    """
    if len(entrada) != 6:
        return "Debe indicar 6 valores exactamente."
    
    if re.match('^[A-Z]+$', entrada[0:2]) is None:
        return "Las siglas de fabricante deben ser únicamente mayúsculas."
    
    if re.match('^[3,4,5,6,8]$', entrada[2]) is None:
        return "El diámetro de entrada no es un valor permitido."
    
    if re.match('^[S,W]$', entrada[3]) is None:
        return "Debe ingresar un proceso de fabricación válido (S o W)"
    
    if re.match('^[40,60,70]+$', entrada[4:]) is None:
        return "El grado del acero no es un valor permitido."
    
    return nomenclaturaVarilla(entrada)

def decoDiametroB(entrada):
    """
    Funcionamiento:
    Decodifica el diámetro de la varilla para la versión que utiliza expresiones regulares.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del diámetro de la varilla.
    """
    if entrada[2] == "3":
        return "El diámetro de la varilla es: 3/8 pulgadas."
    elif entrada[2] == "4":
        return "El diámetro de la varilla es: 1/2 pulgadas."
    elif entrada[2] == "5":
        return "El diámetro de la varilla es: 5/8 pulgadas."
    elif entrada[2] == "6":
        return "El diámetro de la varilla es: 3/4 pulgadas."
    elif entrada[2] == "8":
        return "El diámetro de la varilla es: 1 pulgadas."
    
def decopFB(entrada):
    """
    Funcionamiento:
    Decodifica el proceso de fabricación para la versión que utiliza expresiones regulares.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del proceso de fabricación.
    """
    if entrada[3] == "S":
        return "Proceso de Fabricación: Acero al carbono no soldable a temperatura ambiente."
    elif entrada[3] == "W":
        return "Proceso de Fabricación: Acero al carbono soldable a temperatura ambiente."
    
def decogAB(entrada):
    """
    Funcionamiento:
    Decodifica el grado del acero para la versión que utiliza expresiones regulares.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del grado del acero.
    """
    if entrada[4:] == "40":
        return "Grados de acero: 2800kgf/cm2."
    elif entrada[4:] == "60":
        return "Grados de acero: 4200kgf/cm2."
    elif entrada[4:] == "60":
        return "Grados de acero: 5000kgf/cm2."
    

def nomenclaturaVarillaB(entrada):
    """
    Funcionamiento:
    Imprime la decodificación completa de la nomenclatura de varillas (versión B).

    Entradas:
    entrada (str): Código a decodificiar.
    """
    print("El fabricante es: ", entrada[0:2])
    print(decoDiametro(entrada))
    print(decopF(entrada))
    print(decogA(entrada))
    
    return ""
    
#Reto 2A (Sin ER)
#Variables
sd = ["MicroSD", 'MicroSDHC', "MicroSDXC"]
claseUHS = ["U1", "U3"]
busUHS = ['I', 'II']
clase = ['2','4','6','10'] 

def nomenclaturaSDAux(entrada):
    """
    Funcionamiento:
    Verifica que la entrada cumpla el formato de tarjetas SD sin usar expresiones regulares.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Mensaje de error si falla, o llama nomenclaturaSD si pasa.
    """
    if entrada == '':
        return 'Debe ingresar un texto para poder decodificar.'
    
    for i in sd:
        if i in entrada:
            break
    else: return 'El texto brindado no es posible de decodificar.'
    
    for i in claseUHS:
        if i in entrada:
            break
    else: return 'El texto brindado no es posible de decodificar.'
    
    for i in busUHS:
        if i in entrada:
            break
    else: return 'El texto brindado no es posible de decodificar.'
    
    for i in clase:
        if i in entrada:
            break
    else: return 'El texto brindado no es posible de decodificar.'
    
    return nomenclaturaSD(entrada)

def nomenclaturaSD(entrada):
    """
    Funcionamiento:
    Imprime la decodificación completa de la tarjeta SD.

    Entradas:
    entrada (str): Código a decodificiar.
    """
    print('Usted está usando:')
    print(decoSD(entrada))
    print(decoClaseUHS(entrada))
    print(decoBusUHS(entrada))
    print(decoClase(entrada))
    return ""
    
def decoSD(entrada):
    """
    Funcionamiento:
    Decodifica el tipo y capacidad base de la tarjeta SD.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del tipo de tarjeta.
    """

    if sd[0] in entrada:
        return 'Una tarjeta: MicroSD con capacidad de: 16 MB o 32 MB, etc sin bus UHS.'
    elif sd[1] in entrada:
        return 'Una tarjeta: MicroSD con capacidad de: 4 MB o 8 MB, etc con bus UHS.'
    elif sd[2] in entrada:
        return 'Una tarjeta: MicroSDXC con capacidad de: 64 GB o 128 GB, etc con bus UHS.'
    
def decoClaseUHS(entrada):
    """
    Funcionamiento:
    Decodifica la clase UHS de la tarjeta SD.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción de la velocidad mínima de escritura.
    """
    if claseUHS[0] in entrada:
        return 'Velocidad mínima de escritura: 10MB/s'
    elif claseUHS[1] in entrada:
        return 'Velocidad mínima de escritura: 30MB/s'
    
def decoBusUHS(entrada):
    """
    Funcionamiento:
    Decodifica el tipo de bus UHS de la tarjeta SD.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción de la velocidad máxima de lectura/escritura.
    """
    if busUHS[0] in entrada:
        return 'Velocidad máxima de lectura/escritura: 104 MB/s'
    if busUHS[1] in entrada:
        return 'Velocidad máxima de lectura/escritura: 312 MB/s'
    
def decoClase(entrada):
    """
    Funcionamiento:
    Decodifica la clase estándar de la tarjeta SD.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción de la velocidad mínima de escritura.
    """
    if clase[0] in entrada:
        return 'Velocidad mínima de escritura: 2 MB/s'
    if clase[1] in entrada:
        return 'Velocidad mínima de escritura: 4 MB/s'
    if clase[2] in entrada:
        return 'Velocidad mínima de escritura: 6 MB/s'
    if clase[3] in entrada:
        return 'Velocidad mínima de escritura: 10 MB/s'
    
#Reto 2B (Con ER)
#Variables
sd = ["MicroSD", 'MicroSDHC', "MicroSDXC"]
claseUHS = ["U1", "U3"]
busUHS = ['I', 'II']
clase = ['2','4','6','10'] 

def nomenclaturaSDAuxB(entrada):
    """
    Funcionamiento:
    Verifica que la entrada cumpla el formato de tarjetas SD usando expresiones regulares.

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Mensaje de error si falla, o invoca nomenclaturaSD si pasa.
    """
    if entrada == '':
        return 'Debe ingresar un texto para decodificar.'
    
    if re.match('^(MicroSD|MicroSDHC|MicroSDXC)+(U1|U3)+(I|II)+(2|4|6|10)$', entrada) is None:
        return 'El texto brindado no es posible de decodificar.'
    
    return nomenclaturaSD(entrada)

def nomenclaturaSDB(entrada):
    """
    Funcionamiento:
    Imprime la decodificación completa de la tarjeta SD (versión B).

    Entradas:
    entrada (str): Texto de entrada.
    """
    print('Usted está usando:')
    print(decoSD(entrada))
    print(decoClaseUHS(entrada))
    print(decoBusUHS(entrada))
    print(decoClase(entrada))
    return ""
    
def decoSDB(entrada):
    """
    Funcionamiento:
    Decodifica el tipo y capacidad base de la tarjeta SD (versión B).

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción del tipo de tarjeta.
    """
    if sd[0] in entrada:
        return 'Una tarjeta: MicroSD con capacidad de: 16 MB o 32 MB, etc sin bus UHS.'
    elif sd[1] in entrada:
        return 'Una tarjeta: MicroSD con capacidad de: 4 MB o 8 MB, etc con bus UHS.'
    elif sd[2] in entrada:
        return 'Una tarjeta: MicroSDXC con capacidad de: 64 GB o 128 GB, etc con bus UHS.'
    
def decoClaseUHSB(entrada):
    """
    Funcionamiento:
    Decodifica la clase UHS de la tarjeta SD (versión B).

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción de la velocidad mínima de escritura.
    """
    if claseUHS[0] in entrada:
        return 'Velocidad mínima de escritura: 10MB/s'
    elif claseUHS[1] in entrada:
        return 'Velocidad mínima de escritura: 30MB/s'
    
def decoBusUHSB(entrada):
    """
    Funcionamiento:
    Decodifica el bus UHS de la tarjeta SD (versión B).

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción de la velocidad máxima de lectura/escritura.
    """
    if busUHS[0] in entrada:
        return 'Velocidad máxima de lectura/escritura: 104 MB/s'
    if busUHS[1] in entrada:
        return 'Velocidad máxima de lectura/escritura: 312 MB/s'
    
def decoClaseB(entrada):
    """
    Funcionamiento:
    Decodifica la clase estándar de la tarjeta SD (versión B).

    Entradas:
    entrada (str): Código a decodificiar.

    Salidas:
    str: Descripción de la velocidad mínima de escritura.
    """
    if clase[0] in entrada:
        return 'Velocidad mínima de escritura: 2 MB/s'
    if clase[1] in entrada:
        return 'Velocidad mínima de escritura: 4 MB/s'
    if clase[2] in entrada:
        return 'Velocidad mínima de escritura: 6 MB/s'
    if clase[3] in entrada:
        return 'Velocidad mínima de escritura: 10 MB/s'

#Reto 3A (Sin ER)
def DecodificarNeumáticos(entrada):
    """
    Funcionamiento:
    Decodifica un código de neumático e interpreta sus características principales.

    Entradas:
    entrada (str): Código de neumático.

    Salidas:
    str: Mensaje descriptivo de las características del neumático.
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
    Funcionamiento:
    Verifica si un código de neumático cumple las condiciones necesarias para decodificarse.

    Entradas:
    entrada (str): Código de neumático.

    Salidas:
    str: Mensaje de error o resultado de decodificación.
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
    Funcionamiento:
    Prueba la función de decodificación de neumáticos con varios ejemplos.

    Entradas:
    Ninguna.

    Salidas:
    Ninguna (la función realiza impresiones).
    """
    print(DecodificarNeumáticosAux("16570R1484T"))
    print(DecodificarNeumáticosAux("19555D1687V"))
    print(DecodificarNeumáticosAux("19555D1687AA"))
    print(DecodificarNeumáticosAux("19555B1687ZR"))
    print(DecodificarNeumáticosAux("16570R1450T"))
    
#Reto 3B (Con ER)
def DecodificarNeumáticosB(entrada):
    """
    Funcionamiento:
    Decodifica un código de neumático usando expresiones regulares para validaciones previas.

    Entradas:
    entrada (str): Código de neumático.

    Salidas:
    str: Mensaje descriptivo de las características del neumático.
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

def DecodificarNeumáticosAuxB(entrada):
    """
    Funcionamiento:
    Verifica si un código de neumático cumple las condiciones necesarias para decodificarse (versión B).

    Entradas:
    entrada (str): Código de neumático.

    Salidas:
    str: Mensaje de error o resultado de decodificación.
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

def DecodificarNeumáticosESB():
    """
    Funcionamiento:
    Prueba la función de decodificación de neumáticos (versión B) con varios ejemplos.

    Entradas:
    Ninguna.

    Salidas:
    Ninguna (la función realiza impresiones).
    """
    print(DecodificarNeumáticosAux("16570R1484T"))
    print(DecodificarNeumáticosAux("19555D1687V"))
    print(DecodificarNeumáticosAux("19555D1687AA"))
    print(DecodificarNeumáticosAux("19555B1687ZR"))
    print(DecodificarNeumáticosAux("16570R1450T"))