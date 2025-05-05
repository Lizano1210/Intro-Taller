#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Elaborado por: Elías Lizano Valerio
"""

#Reto 1
def estaOrdenado(cifra, ind, ubi):
    if ind == 0:
        memoria = 10
        while cifra > 0:
            cifraAux = cifra % 10
            if cifraAux < memoria:
                memoria = cifraAux
                resultado = True
            else:
                resultado = False
                return resultado
            cifra //= 10

    elif ind == 1:
        memoria = -1
        while cifra > 0:
            cifraAux = cifra % 10
            if cifraAux > memoria:
                memoria = cifraAux
                resultado = True
            else:
                resultado = False
                return resultado
            cifra //= 10
            
    return resultado 
    

def procesar(cifra, ind, ubi):
    while ubi > 1:
        cifra //= 10
        ubi = ubi -1
        
    return estaOrdenado(cifra, ind, ubi)
    

def estaOrdenadoAux(cifra, ind, ubi):
    try:
        cifra = int(cifra)
        if cifra < 100:
            return "La cifra debe tener al menos 3 digitos."
    except ValueError:
        return "Debe ingresar únicamente valores enteros."
    
    try:
        ind = int(ind)
        if ind > 1 or ind < 0:
            return "Debe ingresar únicamente 1 o 0."
    except ValueError:
        return "Debe ingresar únicamente valores enteros"
   
   #Variables necesarias para validar variable ubi.
    i = 0
    ubiAux = cifra
    while ubiAux > 0:
        i += 1
        ubiAux //= 10
   
    try:
        ubi = int(ubi)
        if ubi < 1 or ubi > i:
            return "Debe ingresar una ubicación mayor a 0 y menos a los dígitos de la cifra."
    except ValueError:
        return "Debe ingresar únicamente valores enteros."
    
    return procesar(cifra, ind, ubi)
     

def estaOrdenadoES(cifra, ind, ubi):
    #cifra = input("Ingrese el número a procesar: ")
    #ind = input("Ingrese la validación que desea realizar: ")
    #ubi = input("Ingrese la posición desde la que desea procesar el número: ")
    return print(estaOrdenadoAux(cifra, ind, ubi))

#Reto 2
def encontrarDifSimetricaES():
    x = input("Ingrese el primer valor: ")
    y = input("Ingrese el segundo valor: ")
    
    return encontrarDifSimetricaAux(x, y)

def encontrarDifSimetricaAux(x, y):
    try:
        x = int(x)
        if x < 1:
            return "Debe ingresar un valor entero, positivo y mayor a 0"
    except ValueError:
        return "Ingrese un valor entero."
    
    try: 
        y = int(y)
        if y < 1:
            return "Debe ingresar un valor entero, positivo y mayor a 0"
    except ValueError:
        return "Debe ingresar un valor entero. "
    
    return encontrarDifSimetrica(x, y)

def encontrarDifSimetrica(x, y):
    resultado = 0
    while x > 0:
        xAux = x % 10
        while y > 0:
            i = 0
            yAux = y % 10
            if yAux != xAux:
                resultado = resultado + yAux * 10 ** i
            i += 1
#RETO INCOMPLETO

#Reto 3
def obtenerSecuencia(n):
    i = 2
    resultado = 0
    while i <= n:
        resultado += (i**2) / (i+1) 
        i += 1
        
    return "El resultado de la sumatoria es:", resultado

def obtenerSecuenciaAux(n):
    try:
        n = int(n)
        if n < 1:
            return "Debe ingresar un número entero mayor a 0."
    except ValueError:
        return "Debe ingresar un número entero mayor a 0."
    
    return obtenerSecuencia(n)

def obtenerSecuenciaES(n):
    #n = input("Ingrese el número  a procesar; ")
    
    return print(obtenerSecuenciaAux(n))

# Programa Prinicipal 
print("RETO 1")
estaOrdenadoES("12",1,1)
estaOrdenadoES(12,1,1)
estaOrdenadoES(123,1,0)
estaOrdenadoES(123,1,5)
estaOrdenadoES(4321,2,1)
estaOrdenadoES(1234,0,3)
estaOrdenadoES(4321,1,2)
estaOrdenadoES(43567,1,3)
estaOrdenadoES(12534,0,1)
estaOrdenadoES(379,0,1)
estaOrdenadoES("a",1,1)#Ejemplo adicional
print("RETO 3")
obtenerSecuenciaES(-7)
obtenerSecuenciaES("siete")
obtenerSecuenciaES(7)
obtenerSecuenciaES(5)
obtenerSecuenciaES(3)


                        