#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 13:14:23 2025

@author: Elías Lizano
"""
import re

     
def nomenclaturaVarillaAux(entrada):
    
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

def decoDiametro(entrada):
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
    if entrada[3] == "S":
        return "Proceso de Fabricación: Acero al carbono no soldable a temperatura ambiente."
    elif entrada[3] == "W":
        return "Proceso de Fabricación: Acero al carbono soldable a temperatura ambiente."
    
def decogA(entrada):
    if entrada[4:] == "40":
        return "Grados de acero: 2800kgf/cm2."
    elif entrada[4:] == "60":
        return "Grados de acero: 4200kgf/cm2."
    elif entrada[4:] == "60":
        return "Grados de acero: 5000kgf/cm2."
    

def nomenclaturaVarilla(entrada):
    print("El fabricante es: ", entrada[0:2])
    print(decoDiametro(entrada))
    print(decopF(entrada))
    print(decogA(entrada))
    
    return ""
    
print(nomenclaturaVarillaAux("SV5S60"))
print(nomenclaturaVarillaAux("SV5S55"))
print(nomenclaturaVarillaAux("SV9S60"))
print(nomenclaturaVarillaAux("SV5S6"))
print(nomenclaturaVarillaAux("Sv5S60"))

