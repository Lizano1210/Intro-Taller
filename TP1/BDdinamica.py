#
#
#
#

'''
Base de datos dinamica: Este documento se encarga de crear la base de datos que utiliza todo el programa.
Funciones:
- generaNombres(): Genera entradas de la base datos creando nombres aleatoriamente.
- leeNombres(): Genera entradas de la base datos extrayendo los nombresde un documento.
- bdDinamicaES(): Junta las entradas de las 2 funciones anteriores en una sola base de datos universal.
- sedes(): Lee las sedes que se necesitan para la realización de los carné, las extrae de un documento externo, 
las codifica y almacena.
'''

#Importación de librerias/modulos
import names
import random 
import math 
import re
import pickle

# Fuente 1 Generados aleatoriamente
def generaNombres(entrada,annoInicial,annoFinal,nota1,nota2,nota3):
    """
    Funcionamiento: Genera una lista de estudiantes ficticios con datos como nombre, género, carné, correo y notas, 
    y los guarda en un archivo de texto. También retorna la base de datos generada con todos los registros.
    Entradas:
    - entrada (int): Cantidad de estudiantes a generar.
    - annoInicial (int): Año mínimo para generar el carné estudiantil.
    - annoFinal (int): Año máximo para generar el carné estudiantil.
    - nota1 (float): Porcentaje asignado al primer examen.
    - nota2 (float): Porcentaje asignado al segundo examen.
    - nota3 (float): Porcentaje asignado al tercer examen.
    Salidas:
    - estudiantesGenerados (list): Lista de estudiantes generados. Cada estudiante es una lista con la estructura:
    [(nombre, apellido1, apellido2), sexo (bool), carné (str), correo (str),
    (nota1, nota2, nota3, nota_final, nota_final)].
    """
    fuente = open('listaPrueba.txt', 'w')
    estudiantesGenerados = []
    for i in range(entrada):
        sexo = random.choice([True, False])
        if sexo == True:
            nombre = names.get_first_name(gender = 'Male')
        else:
            nombre = names.get_first_name(gender = 'Female')
        pApellido = names.get_last_name()
        sApellido = names.get_last_name() 
        while True:
            if pApellido == sApellido:
                sApellido = names.get_last_name()
            else:
                break
        sedeEstudiante = sede()
        carne = f'{random.randint(int(annoInicial),int(annoFinal))}{random.choice(sedeEstudiante[1])}{random.randint(0,9999):04}'
        correo = f'{nombre[0].lower()}{pApellido.lower()}{carne[6:]}@estudiantec.cr'
        notas = (random.randint(1,100), random.randint(1,100), random.randint(1,100), 0.0, 0.0)
        notaReal1 = notas[0] * (nota1/100)
        notaReal2 = notas[1] * (nota2/100)
        notaReal3 = notas [2] * (nota3/100)
        notaFinal = (notaReal1+notaReal2+notaReal3)
        notaFinal = round(notaFinal, 1)
        notas = (notas[0], notas[1], notas[2], notaFinal, notaFinal)
        estudiante = [(nombre, pApellido, sApellido), sexo, carne, correo, notas]
        estudiantesGenerados.append(estudiante)
        fuente.write(f'{estudiante[0][0]}, {estudiante[0][1]}, {estudiante[0][2]}, {estudiante[1]}, {estudiante[2]}, {estudiante[3]}, {estudiante[4]} \n')
    fuente.close()
    print(f'Se genero {entrada} estudiantes')
    return estudiantesGenerados

#Fuente 2 Extraidos de archivo
def leeNombres(porcentaje,annoInicial,annoFinal,nota1,nota2,nota3):
    """
    Funcionamiento: Lee nombres desde un archivo preexistente de estudiantes, selecciona un porcentaje aleatorio 
    de ellos, les genera un carné, correo y notas ficticias, y agrega esta nueva información a un archivo de salida. 
    Devuelve la base de datos con los estudiantes seleccionados y completados.
    Entradas:
    - porcentaje (float): Porcentaje de estudiantes que se deben seleccionar del archivo.
    - annoInicial (int): Año mínimo para generar el carné estudiantil.
    - annoFinal (int): Año máximo para generar el carné estudiantil.
    - nota1 (float): Porcentaje asignado al primer examen.
    - nota2 (float): Porcentaje asignado al segundo examen.
    - nota3 (float): Porcentaje asignado al tercer examen.
    Salidas:
    - estudiantesLeidos (list): Lista de estudiantes seleccionados y procesados. 
    Cada uno tiene la estructura:
    [(nombre, apellido1, apellido2), sexo (bool), carné (str), correo (str), 
    (nota1, nota2, nota3, nota_final, nota_final)].
    """
    estudiantesLeidos = []
    fuenteEstudiantes = open('estudiantes.txt','r')
    lineas = fuenteEstudiantes.readlines()
    fuenteEstudiantes.close()
    cantidad = len(lineas) #Cantidad de estudiantes
    redondeo = math.ceil(cantidad * (porcentaje/100))
    nombresExtraidos = random.sample(lineas, redondeo)
    fuente = open('listaPrueba.txt', 'a')
    for i in nombresExtraidos:
        nombre = i.strip()
        nombre = i.split(',')
        nombreEst = (nombre[0])
        Apellido1 = (nombre[1])
        Apellido2 = (nombre[2])
        if nombre[3] == 'Masculino\n':
            sexo = True
        else:
            sexo = False
        sedeEstudiante = sede()
        carne = f'{random.randint(int(annoInicial),int(annoFinal))}{random.choice(sedeEstudiante[1])}{random.randint(0,9999):04}'
        correo = f'{nombreEst[0].lower()}{Apellido1.lower()}{carne[6:]}@estudiantec.cr'
        notas = (random.randint(1,100), random.randint(1,100), random.randint(1,100), 0.0, 0.0)
        notaReal1 = notas[0] * (nota1/100)
        notaReal2 = notas[1] * (nota2/100)
        notaReal3 = notas [2] * (nota3/100)
        notaFinal = (notaReal1+notaReal2+notaReal3)
        notaFinal = round(notaFinal, 1)
        notas = (notas[0], notas[1], notas[2], notaFinal, notaFinal) 
        estudiantesLeidos.append([(nombreEst,Apellido1,Apellido2),sexo,carne,correo, notas])
        fuente.write(f'{nombre[0]}, {nombre[1]}, {nombre[2]}, {sexo}, {carne}, {correo}, {notas}\n')
    fuente.close()
    return estudiantesLeidos

def bdDinamicaES():
    """
    Funcionamiento: Solicita datos al usuario para generar una base de datos dinámica de estudiantes, 
    combinando estudiantes generados aleatoriamente con otros leídos desde un archivo. 
    Valida los datos ingresados (años, porcentajes de notas, etc.) y construye una lista de estudiantes 
    con carné, correo y notas ficticias.
    Salidas:
    - bdDinamica (list): Lista combinada de estudiantes generados y leídos. Cada estudiante tiene la estructura:
    [(nombre, apellido1, apellido2), sexo (bool), carné (str), correo (str), 
    (nota1, nota2, nota3, nota_final, nota_final)].
    - annos (tuple): Tupla con el año inicial y final considerados para la generación de carnés.
    """
    bdDinamica = []
    while True:
        try:
            cantidad = int(input('Ingrese la cantidad de estudiantes de la cual desea la lista: '))
            porcentaje = int(input('Ingrese el porcentaje que se le aplicara a la cantidad: '))
            annoInicial = input('Ingrese el primer año de la primera generación a tener en cuenta: ')
            annoFinal = input('Ingrese el primer año de la última generación a tener en cuenta generación a tener en cuenta: ')
            if re.match(r'^\d{4}$', annoInicial) is None or re.match(r'^\d{4}$', annoFinal) is None:
                print('Debe ingresar un año unicamente. Con sus 4 dígitos.')
                continue
            if annoFinal < annoInicial:
                print('La última generación no puede ser anterior a la primera.')
                continue
            print('Notas, a continuación ingrese el porcentaje de valor de cada una de sus asignaciones. \n' \
            'Recuerde que los 3 porcentajes deben sumar 100.')
            nota1 = int(input('Ingrese el primer porcentaje de nota: '))
            nota2 = int(input('Ingrese el segundo porcentaje de nota: '))
            nota3 = int(input('Ingrese el tercer porcentaje de nota: '))
            total = (nota1 + nota2 + nota3)
            if total != 100:
                print('Sus porcentajes de notas son invalidos, deben sumar 100')
                continue
            break
        except ValueError:
            print('Datos invalidos, solo debe ingresar números enteros.')
    entrada = math.ceil(cantidad * (porcentaje/100))
    fuente1 = generaNombres(entrada,annoInicial,annoFinal,nota1,nota2,nota3)
    fuente2 = leeNombres(porcentaje,annoInicial,annoFinal,nota1,nota2,nota3)
    bdDinamica = fuente1
    for i in fuente2:
        bdDinamica.append(i)
    annos = (annoInicial,annoFinal)
    with open('baseDatosDinamica.pkl', 'wb') as archivobD:
        pickle.dump(bdDinamica, archivobD)
    with open('rangoAnnos.pkl', 'wb') as archivoAnnos:
        pickle.dump(annos, archivoAnnos)
    print(bdDinamica)
    return bdDinamica,annos

def sede():
    """
    Funcionamiento: Lee las sedes disponibles desde el archivo 'sedes.txt', asigna un código secuencial 
    (anteponiendo un 0) a cada una y retorna tanto la lista completa de sedes con sus códigos como una lista 
    sola de códigos.
    Salidas:
-   list: Una lista con dos elementos:
    - sedes (list): Lista de listas, cada una con el nombre de la sede y su código correspondiente.
    - codSedes (list): Lista de solo los códigos asignados a cada sede.
    """
    sedes = []
    codSedes = []
    archivoSedes = open('sedes.txt','r')
    lineasSedes = archivoSedes.readlines()
    archivoSedes.close()
    cantidadSedes = len(lineasSedes)
    contador = 0
    for i in (lineasSedes):
        sedeTexto = i.replace('\n','')
        contador += 1
        codSede = '0' + str(contador)
        sedeCompleta = [sedeTexto, codSede]
        codSedes.append(codSede)
        sedes.append(sedeCompleta)
    #print(sedes)
    return [sedes, codSedes]









