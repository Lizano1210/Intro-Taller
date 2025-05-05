#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 22:12:46 2025

@author: lizano
"""
def obtenerSecuencia(n):
    i = 2
    resultado = 0
    while i <= n:
        resultado += (i*2) / (i+1) 
        i += 1
        
    return resultado

def obtenerSecuenciaAux(n):
    try:
        n = int(n)
        if n < 1:
            return "Debe ingresar un número entero mayor a 0."
    except ValueError:
        return "Debe ingresar un número entero mayor a 0."
    
    return obtenerSecuencia(n)

def obtenerSecuenciaES():
    n = input("Ingrese el número  a procesar; ")
    
    return obtenerSecuenciaAux(n)
        