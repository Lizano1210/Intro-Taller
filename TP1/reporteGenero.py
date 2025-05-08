#
#
#
#

'''
REPORTE POR GÉNERO: Este archivo se encarga de crear 2 reportes .docx, uno de hombres y otro de mujeres
donde se muestres sus datos ordenados por mejores notas.
'''
import pickle

def determinarGeneroyOrdenar():
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    # Asignación de variables
    listaHombres = []
    listaMujeres = []
    #------------------------
    for i in range(len(bD)):
        maxH = (None,0) # Recuerda documentar solución de este bug
        maxM = (None,0) # Ponemos None para evitar un registro de (0,0) en la base de datos.
        for e in bD:
            if e[1] == True:
                    if e in listaHombres:
                                continue
                    else:
                        if e[4][4] > maxH[1]:
                            maxH = (e, e[4][4])
                        else:
                            continue
            elif e[1] == False:
                    if e in listaMujeres:
                                continue
                    else:
                        if e[4][4] > maxM[1]:
                            maxM = (e, e[4][4])
                        else:
                            continue
        if maxH[0] == None:
              continue
        else:
              listaHombres.append(maxH[0])
        if maxM[0] == None:
              continue
        else:
              listaMujeres.append(maxM[0])
    return reporteGenero(bD, listaHombres, listaMujeres)
    
def reporteGenero(bD, listaHombres, listaMujeres):
      # Asignación de variables.
      with open('porcentaje.pkl', 'rb') as archivoPorce:
        notas = pickle.load(archivoPorce)
      totalEstudiantes = len(bD)
      totalHombres = len(listaHombres)
      totalMujeres = len(listaMujeres)
      # ------------------------------------------------
      reporteH = open('reporteHombres.docx', 'w')
      reporteH.write('Reporte de Hombres ordenados por notas. \n'
      '\n')
      for i in listaHombres:
            reporteH.write(f'Redondeo o nota de acta: {i[4][4]}. Notas obtenidas: {i[4][0:3]}. \n'
                           f'Nombre: {i[0]}. Carné: {i[2]}. Correo: {i[3]}. \n'
                           '\n')
      
      reporteH.write(f'El porcentaje aplicado a las evaluaciones es el siguiente: 1 - {notas[0]}%, 2 - {notas[1]}%, 3 - {notas[2]}%. \n'
                     f'En total hay {totalHombres} hombres, para un {round((totalHombres/totalEstudiantes *100))}% del total de estudiantes.')
      reporteH.close()
      reporteM = open('reporteMujeres.docx', 'w')
      reporteM.write('Reporte de Mujeres ordenadas por notas. \n'
      '\n')
      for i in listaMujeres:
            reporteM.write(f'Redondeo o nota de acta: {i[4][4]}. Notas obtenidas: {i[4][0:3]}. \n'
                           f'Nombre: {i[0]}. Carné: {i[2]}. Correo: {i[3]}. \n'
                           '\n')
      reporteM.write(f'El porcentaje aplicado a las evaluaciones es el siguiente: 1 - {notas[0]}%, 2 - {notas[1]}%, 3 - {notas[2]}%. \n'
                     f'En total hay {totalMujeres} mujeres, para un {round((totalMujeres/totalEstudiantes *100))}% del total de estudiantes.')
      reporteH.close()
      return print('Sus reportes por género se generaron satisfactoriamente. ')
      

                
                
