#
#
#
#

import pickle   
import re

def determinarSede():
    count = 0
    with open('sedes.pkl', 'rb') as archivoSedes:
        sedes = pickle.load(archivoSedes)
    with open('sedesCod.pkl', 'rb') as archivoCodSedes:
        codSedes= pickle.load(archivoCodSedes)
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    print(f'Seleccione la sede de la cuál desea conocer sus estudiantes con mejor rendimiento: \n'
          f'')
    for i in sedes:
         print(f'{i[0]} --- {i[1]}.\n')
         count += 1
    print('')
    while True:
         try:
              sedeSelect = int(input('Ingrese el código de la sede: '))
              if re.match(f'^({"|".join(str(codSedes))})$', str(sedeSelect)) is None:
                   print('Opción Invalida, Ingrese unicamente un código de sede.')
                   continue
              break
         except ValueError:
              print('Opción Invalida, Ingrese unicamente un código de sede.')
    return generarReporteSede(bD, sedeSelect)

def generarReporteSede(bD, sedeSelect):
     mejoresEstudiantesSede = []
     for estudiante in bD:
            sedeEstudiante = int(estudiante[2][4:6])
            if sedeEstudiante == sedeSelect:
                 notasEstudiante = estudiante[4][0:3]
                 for i in notasEstudiante:
                      if i >= 70:
                           bRendimiento = True #Si la nota detectada es mayor a 70, realizamos la siguiente iteración.
                           continue 
                      else:
                           bRendimiento = False #Si la nota detectada es menor a 70, terminamos el ciclo y devolvemos False.
                           break
            else:
                 continue
            if bRendimiento == True:
                 mejoresEstudiantesSede.append(estudiante)
            else:
                 continue
     for buenEst in mejoresEstudiantesSede:
          print(f'{buenEst[0]}, {buenEst[1]}, {buenEst[2]}, {buenEst[3]}, {buenEst[4]}. \n')
     return    
    

                 
          
     
    
         
    