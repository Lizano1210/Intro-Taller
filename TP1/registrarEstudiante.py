#
#
#
#

import re
import pickle

with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
def registrarEstudiante(bD):
        """"""
        datosEstudiante = [nombreCompleto, genero, carne, correo, notas]
        bD.append(datosEstudiante)
        return bD


def registrarEstudianteAux(nombreCompleto, genero, carne, correo, notas):
       while True:
        try:
            if re.match carne in bD:
                print("El número de carne ya existe.")
                continue
            if carne[0:5]>= "2026":
                print("El número de carne no es válido.")
                continue
            if re.match correo in bD:
                print("El correo ya existe.")
                continue
            if correo =! f'{nombre[0].lower()}{pApellido.lower()}{carne[6:]}@estudiantec.cr':
                print("El correo ingresado no es válido. ")
                continue
            if nFinal > 100 or nFinal <0:
                      print("La nota final no es válida.")
            break
        except:
                    
def registrarEstudianteES():
        """"""
        nombreCompleto = (nombre, apellido1, apellido2)
        nombre = str(input("Ingrese el nombre del estudiante: "))
        apellido1 = str(input("Ingrese el primer apellido del estudiante: "))
        apellido2 = str(input("Ingrese el segundo apellido del estudiante: ")) 
        genero = int(input("Digite (1) para masculino o (2) para femenino: "))
        carne = str(input("Ingrese el número de carne del estudiante: "))
        correo = str(input("Ingrese su correo electrónico: "))
        notas = (n1, n2, n3 ,nFinal)
        n1 = int(input("Ingrese la nota del primer parcial: "))
        n2 = int(input("Ingrese la nota del segundo parcial: "))
        n3 = int(input("Ingrese la nota del tercer parcial: "))
        return 