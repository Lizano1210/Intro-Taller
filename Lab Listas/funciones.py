#Elaborado por: Elías Lizano y Joshua Brenes
#Fecha de creación: 1/5/2025 7:30am.
#Última modificación: 1/5/2025 8:30pm.
#Versión de Python: 3.12.3
'''
FUNCIONES: En este documento encontrará todas las funciones de procesamiento
del programa.
'''
import re

# Definición de variables 
recuperadosDonantes=["303500621","101110218","412340987","267893456","154328765","534561234","187674329","265437654","243214321","187654321","187659870","687659870","887659870","945659823"]
# recuperadosDonantes: Lista previamente brindada por la profesora.

def nuevoDonante(nD):
    """
    Funcionamiento: Valida si una cédula tiene el formato correcto.
    Entradas:
    - nD (str): Número de cédula a evaluar
    Salidas:
    - resultado (str o bool): Mensaje de error si la cédula ya existe o es inválida o True si es válida y nueva
    """
    if nD in recuperadosDonantes:
        return 'No puede ingresar un donante ya existente.'
    if re.match("^\d{1}\d{8}$", nD) is None:
        return 'El número de cédula ingresado no es válido.'
    return True 

def decodificarDonador(entrada):
    """
    Funcionamiento: Decodifica el número de cédula de un donante y muestra su lugar de origen,
    así como el tomo y asiento si aplica.
    Entradas:
    - entrada (str): Número de cédula del donante
    Salidas:
    - resultado (str): Mensaje que describe la procedencia del donante, el tomo y el asiento, 
      o si se trata de un nacionalizado/nacimiento especial, o si no es donante registrado
    """
    if entrada in recuperadosDonantes:
        if entrada[0]== "1":
            return "Usted es de San José, está \n" \
                   f"registrado en el tomo {entrada[1:5]}, y el \n" \
                   f"asiento {entrada[5:]}"
        elif entrada[0]== "2":
            return "Usted es de Alajuela, está \n" \
                   f"registrado en el tomo {entrada[1:5]}, y el \n" \
                   f"asiento {entrada[5:]}"
        elif entrada[0]== "3":
            return "Usted es de Cartago, está \n" \
                   f"registrado en el tomo {entrada[1:5]}, y el \n" \
                   f"asiento {entrada[5:]}"
        elif entrada[0]== "4":
            return "Usted es de Heredia, está \n" \
                   f"registrado en el tomo {entrada[1:5]}, y el \n" \
                   f"asiento {entrada[5:]}"
        elif entrada[0]== "5":
            return "Usted es de Guanacaste, está \n" \
                   f"registrado en el tomo {entrada[1:5]}, y el \n" \
                   f"asiento {entrada[5:]}"
        elif entrada[0]== "6":
            return "Usted es de Puntarenas, está \n" \
                   f"registrado en el tomo {entrada[1:5]}, y el \n" \
                   f"asiento {entrada[5:]}"
        elif entrada[0]== "7":
            return "Usted es de Limón, está \n" \
                   f"registrado en el tomo {entrada[1:5]}, y el \n" \
                   f"asiento {entrada[5:]}"
        elif entrada[0]== "8":
            return "Nacionalizado o naturalizado. \n" \
                   "(Extranjero)."
        elif entrada[0]== "9":
            return "Partida especial de nacimientos \n" \
                   "(Casos especiales)"
    else:
        return "El donador no es un donante aún."

def listaRN(oplistaRN):
    """
    Funcionamiento: Filtra la lista de donantes según la provincia.
    Entradas:
    - oplistaRN (int): Código de provincia (1 a 9)
    Salidas:
    - listaRNAux (list): Lista de cédulas correspondientes a la provincia
    - contador (int): Cantidad de donantes de esa provincia
    - provincia (str): Nombre de la provincia o categoría especial correspondiente
    """
    listaRNAux = []
    contador = 0
    provincia = ''
    if oplistaRN == 1:
        provincia = 'San José'
        for i in recuperadosDonantes:
            if i[0] == '1':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 2:
        provincia = 'Alajuela'
        for i in recuperadosDonantes:
            if i[0] == '2':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 3:
        provincia = 'Cartago'
        for i in recuperadosDonantes:
            if i[0] == '3':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 4:
        provincia = 'Heredia'
        for i in recuperadosDonantes:
            if i[0] == '4':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 5:
        provincia = 'Guanacaste'
        for i in recuperadosDonantes:
            if i[0] == '5':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 6:
        provincia = 'Puntarenas'
        for i in recuperadosDonantes:
            if i[0] == '6':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 7:
        provincia = 'Limón'
        for i in recuperadosDonantes:
            if i[0] == '7':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 8:
        provincia = 'nacionalizados o naturalizados'
        for i in recuperadosDonantes:
            if i[0] == '8':
                listaRNAux.append(i)
                contador += 1
    if oplistaRN == 9:
        provincia = 'de partida especial de nacimientos'
        for i in recuperadosDonantes:
            if i[0] == '9':
                listaRNAux.append(i)
                contador += 1
    
    return listaRNAux, contador, provincia
    








