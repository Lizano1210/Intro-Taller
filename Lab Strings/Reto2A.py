#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 01:04:00 2025

@author: lizano
"""
#Variables
sd = ["MicroSD", 'MicroSDHC', "MicroSDXC"]
claseUHS = ["U1", "U3"]
busUHS = ['I', 'II']
clase = ['2','4','6','10'] 

def nomenclaturaSDAux(entrada):
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
    print('Usted está usando:')
    print(decoSD(entrada))
    print(decoClaseUHS(entrada))
    print(decoBusUHS(entrada))
    print(decoClase(entrada))
    return ""
    
def decoSD(entrada):
    if sd[0] in entrada:
        return 'Una tarjeta: MicroSD con capacidad de: 16 MB o 32 MB, etc sin bus UHS.'
    elif sd[1] in entrada:
        return 'Una tarjeta: MicroSD con capacidad de: 4 MB o 8 MB, etc con bus UHS.'
    elif sd[2] in entrada:
        return 'Una tarjeta: MicroSDXC con capacidad de: 64 GB o 128 GB, etc con bus UHS.'
    
def decoClaseUHS(entrada):
    if claseUHS[0] in entrada:
        return 'Velocidad mínima de escritura: 10MB/s'
    elif claseUHS[1] in entrada:
        return 'Velocidad mínima de escritura: 30MB/s'
    
def decoBusUHS(entrada):
    if busUHS[0] in entrada:
        return 'Velocidad máxima de lectura/escritura: 104 MB/s'
    if busUHS[1] in entrada:
        return 'Velocidad máxima de lectura/escritura: 312 MB/s'
    
def decoClase(entrada):
    if clase[0] in entrada:
        return 'Velocidad mínima de escritura: 2 MB/s'
    if clase[1] in entrada:
        return 'Velocidad mínima de escritura: 4 MB/s'
    if clase[2] in entrada:
        return 'Velocidad mínima de escritura: 6 MB/s'
    if clase[3] in entrada:
        return 'Velocidad mínima de escritura: 10 MB/s'
    
    
print(nomenclaturaSDAux(''))
print(nomenclaturaSDAux('micro'))
print(nomenclaturaSDAux('MicroDU1I10'))
print(nomenclaturaSDAux('MicroSDU1I10'))
print(nomenclaturaSDAux('MicroSDXCU3II6'))