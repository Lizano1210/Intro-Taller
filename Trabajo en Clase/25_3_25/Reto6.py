# -*- coding: utf-8 -*-
"""
Spyder Editor

    This is a temporary script file.
"""

def esPerfecto(num):
    """
    Funcionamiento:
    - Determina si un número es perfecto.
    Entradas:
    - num (int): Número a evaluar.
    Salidas:
    - bool: True si el número es perfecto, False en caso contrario.
    """
    #Definición de variables.
    numAux = 0
    i = 1
    resultado = 0
    
    while i < num:
        numAux = num % i
        if numAux == 0:
         resultado = resultado + i
        
        i += 1
        
    if resultado == num:
        return True
    else:
        return False
    

def esPerfectoAux(num):
    """
    Funcionamiento:
    - Valida si la entrada es un número entero positivo antes de enviarlo a la función `esPerfecto()`.
    Entradas:
    - num (int): Número ingresado por el usuario.
    Salidas:
    - str: Mensaje de error si el número no es válido.
    """
    if isinstance(num, float):
        return "Debe ingresar unicamente un número entero."
    
    try:
        num = int(num)
        if num < 0:
            return "El número ingresado debe ser mayor a 0."
    except ValueError:
        return "Debe ingresar unicamente un número entero."

    return esPerfecto(num)

def esPerfectoES(num):
    """
     Funcionamiento:
     - Recibe información del usuario y llama a `esPerfectoAux()` e imprime su resultado.
     Entradas:
     - num (int): Número ingresado.
     Salidas:
     - str: Imprime el resultado de `esPerfectoAux()`.
     """
     
    #num = input("Ingrese el número a analizar: ")
    
    return print(esPerfectoAux(num))
                
#Programa principal:
    
esPerfectoES(25.33)
esPerfectoES(-11)
esPerfectoES(6)
esPerfectoES(18)
esPerfectoES(28)
esPerfectoES(496)

            
    