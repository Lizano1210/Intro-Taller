#
#
#
#

#Importación de librerias
import names
import random 
import math 
import re

# Fuente 1
def generaNombres(entrada,annoInicial,annoFinal,nota1,nota2,nota3):
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

#Fuente 2
def leeNombres(porcentaje,annoInicial,annoFinal,nota1,nota2,nota3):
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
    print(bdDinamica)
    return bdDinamica,annos

def sede():
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








