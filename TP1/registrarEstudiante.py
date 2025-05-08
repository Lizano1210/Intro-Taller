#
#
#
#

'''
REGISTRAR ESTUDIANTE: Este documento contiene la función que permite al usuario registrar nuevos estudiantes
en la base de datos.
'''

import re
import pickle
import BDdinamica
            
def registrarEstudianteES():
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    with open('porcentaje.pkl', 'rb') as archivoPorce:
         porcentaje = pickle.load(archivoPorce)
    with open('rangoAnnos.pkl', 'rb') as archivoAnnos:
            annos = pickle.load(archivoAnnos)
    sedes = BDdinamica.sede()[1]
    nombre = str(input("Ingrese el nombre del estudiante: "))
    apellido1 = str(input("Ingrese el primer apellido del estudiante: "))
    apellido2 = str(input("Ingrese el segundo apellido del estudiante: ")) 
    nombreCompleto = (nombre, apellido1, apellido2)
    #------------ Este bloque se encarga de hacer una lista con las generaciones que ingreso el usuario.-----
    annoInicial = int(annos[0])
    listaAnnos = []
    while annoInicial <= int(annos[1]):
        listaAnnos.append(annoInicial)
        annoInicial +=1
    #----------- Fin bloque generaciones --------------------------------------------------------------------
    while True:
        try:
            genero = input("Digite (1) para masculino o (2) para femenino: ")
            if re.match(f'^[12]$', genero) is None:
                print('Solo debe ingresar 1 o 2.')
                continue
            if genero == '1':
                genero = True
            else:
                genero = False
            break
        except ValueError:
            print('El dato ingresado no es valido, vuelvalo a intentar.')
    while True:
        try:   
            carne = str(input("Ingrese el número de carne del estudiante: \n"
                              "Debe formarse asi, primeros 4 digitos, año en el que ingreso a estudiar.\n"
                              "Su número de sede (que siempre sera un 0 seguido de su numero de sede.) \n"
                              "Los 4 ultimos dígitos son al azar a su elección: "))
            if re.match(f'^\d{{4}}({"|".join(sedes)})\d{{4}}$', carne) is None: 
                print('El carne no es valido, vuelvalo a intentar.')
                continue
            existe = False
            for i in bD:
                if carne == i[2]:
                    existe = True
                    break
                else:
                    continue
            if existe == True:
                print('El carne ya existe en la base de datos, vuelvalo a intentar.')
                continue
            annoIngreso = int(carne[0:4])
            if annoIngreso not in listaAnnos:
                print('El año de ingreso que dígito no existe dentro de los que componen la base de datos.\n' \
                f'{listaAnnos}')
                continue
            break
        except ValueError:
            print('El dato ingresado no es válido, vuelvalo a intentar.')
    while True:
        try:
            correo = str(input("Cree su correo electrónico:\n" \
                               "Escriba la primera letra de su nombre seguida de su primer apellido y\n" \
                               "los últimos 4 digitos de su carnet.\n"
                               "La primer letra de su nombre y su apellido DEBEN IR EN MINUSCULA: \n"))
            if re.match(f'^[{nombre[0].lower()}]({apellido1.lower()})({carne[-4:]})$', correo) is None:
                print('Su correo esta mal formado\n' \
                      'Escriba la primera letra de su nombre seguida de su primer apellido y\n' \
                      'los últimos 4 digitos de su carnet.\n' \
                      'La primer letra de su nombre y su apellido DEBEN IR EN MINUSCULA: \n')
                continue
            else:
                correo += '@estudiantec.cr'
                break
        except ValueError:
            print('El dato ingresado no es valido, intentelo de nuevo.')
    while True:
         try:    
            n1 = int(input("Ingrese la nota del primer parcial: "))
            if re.match('^([0-9]|[1-9][0-9]|100)$', str(n1)) is None:
                 print('El numero ingresado debe estar en el rango de 0-100.')
                 continue
            n2 = int(input("Ingrese la nota del segundo parcial: "))
            if re.match('^([0-9]|[1-9][0-9]|100)$', str(n2)) is None:
                 print('El numero ingresado debe estar en el rango de 0-100.')
                 continue
            n3 = int(input("Ingrese la nota del tercer parcial: "))
            if re.match('^([0-9]|[1-9][0-9]|100)$', str(n3)) is None:
                 print('El numero ingresado debe estar en el rango de 0-100.')
                 continue
            break
         except ValueError:
              print('El dato ingresado no es valido. Solo debe ingresar números enteros.')
    nFinal = (n1 * (porcentaje[0]/100))+(n2 * (porcentaje[1]/100))+(n3 * (porcentaje[2]/100))
    notas = (n1, n2, n3, nFinal, nFinal)
    estudiante = [nombreCompleto, genero, carne, correo, notas]
    bD.append(estudiante)
    print(bD)
    with open('baseDatosDinamica.pkl', 'wb') as archivobD:
        pickle.dump(bD, archivobD)
    return




    