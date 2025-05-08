#
#
#
#

'''
APLAZADOS EN AL MENOS 2 RUBROS(.pdf):
'''
import pickle

def determinarAplazados():
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    #Definición de variables
    listaAplazados = []
    totalEstudiantes = len(bD)
    notaMin = 70
    notaMax = 0
    repro2 = 0
    repro3 = 0
    #-----------------------
    for i in bD:
          count = 0
          notas = i[4]
          if notas[0] < 70:
                if notas[0] < notaMin:
                      notaMin = notas[0]
                elif notas[0] > notaMax:
                      notaMax = notas[0]
                count += 1
          if notas[1] < 70:
                if notas[1] < notaMin:
                      notaMin = notas[1]
                elif notas[1] > notaMax:
                      notaMax = notas[1]
                count += 1
          if notas[2] < 70:
                if notas[2] < notaMin:
                      notaMin = notas[2]
                elif notas[2] > notaMax:
                      notaMax = notas[2]
                count += 1
    #----------------------------------- En este ultimo bloque determinamos si es aplazado en 2 o más rubros.
          if count == 2:
                repro2 += 1
                listaAplazados.append(i)
          elif count == 3:
                repro3 += 1
                listaAplazados.append(i)
    return reporteAplazados(listaAplazados, totalEstudiantes, notaMin, notaMax, repro2, repro3)
    

def reporteAplazados(listaAplazados, totalEstudiantes, notaMin, notaMax, repro2, repro3):
      totalAplazados = len(listaAplazados)
      porcentaje = ((totalAplazados/totalEstudiantes) * 100)
      reporte = open('aplazados2Rubros.pdf', 'w')
      reporte.write('Lista de estudiantes aplazados en al menos 2 rubros. \n')
      for i in listaAplazados:
            reporte.write(f'{i[4]}, {i[0][0]} {i[0][1]} {i[0][2]}, {i[2]}, {i[3]}.\n')
      reporte.write(f'Hubo un total de {totalAplazados} estudiantes que tuvieron este inconveniente para un porcentaje de ' \
                    f'{porcentaje}%, respecto al total de estudiantes de la base de datos ({totalEstudiantes}).\n')
      reporte.write(f'Reporte de nota mínima: {notaMin}.\n')
      reporte.write(f'Reporte de nota máxima: {notaMax}.\n')
      reporte.write(f'Cantidad de reprobados en 2 exámenes: {repro2}.\n')
      reporte.write(f'Cantidad de reprobados en 3 exámenes: {repro3}.\n')
      return print('Su reporte en PDF ha sido generado satisfactoriamente.')

      

