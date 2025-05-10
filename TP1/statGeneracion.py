#
#
#
#

import pickle

def estadisticaGeneracion():
        with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
        with open('rangoAnnos.pkl', 'rb') as archivoAnnos:
            annos = pickle.load(archivoAnnos)
        anno = int(annos[0])
        annoFinal = int(annos[1])
        cantidad = annoFinal - anno #Se define para cuantas generaciones se debe crear un reporte.
        cantidad += 1
        totalApro = 0
        totalRepro = 0
        totalRepo = 0
        for e in range(cantidad): #Ciclo que incrementa la generación.
                 print(f'Generación {anno}') 
                 aprobados = 0
                 reprobados = 0
                 reposicion = 0
                 totalGeneracion = 0
                 for estudiante in bD: #Ciclo que imprime la entrada de un estudiante de la generación definida en el ciclo anterior.
                    generacion = estudiante[2][0:4]
                    if generacion == str(anno):
                         notas = estudiante[4]
                         notaFinal = notas[4]
                         if notaFinal >=70:
                            aprobados += 1
                            totalApro += 1
                            totalGeneracion += 1
                         if notaFinal >=60 and notaFinal < 70:
                            reposicion +=1
                            totalRepo += 1
                            totalGeneracion += 1
                         if notaFinal < 60:
                            reprobados += 1
                            totalRepro += 1
                            totalGeneracion += 1
                    else:
                         continue
                 print (f"Estudiantes que irán a reposición: {reposicion}")
                 print (f"Estudiantes aprobados: {aprobados}")
                 print (f"Estudiantes reprobados: {reprobados}")
                 print (f"La generación {anno}, tiene un total de {totalGeneracion} estudiantes.\n")
                 anno += 1
        print('Se han analizado todas las generaciones!\n')
        print('Estadisticas globales: \n')
        print(f'El total de estudiantes que tuvieron que ir reposición fue de:{totalRepo}.')
        print(f'El total de estudiantes que fueron aprobados fue de: {totalApro}.')
        print(f'El total de estudiantes que fueron reprobados fue de: {totalRepro}.')
        return

                 
                    

                 
                    

                    
        
       
#def estadisticaGeneracionAux():
     #while True:
        #if estudiante not in bD:
        #print("Estudiante no encontrado en la base de datos.")
        #break
#return
          
          