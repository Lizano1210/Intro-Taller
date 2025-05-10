#
#
#
#

'''
Reporte XML: Crea un respaldo de la base de datos con un formato de XML.
'''

import BDdinamica
import pickle
#bD = BDdinamica.bdDinamicaES()

def respaldoXML():
    """
    Funcionamiento: Genera un archivo XML con la información de los estudiantes, organizados por generación según el año
    de su carné. Cada entrada incluye nombre completo, género, carné, correo, notas y estado académico.
    Entradas:
    - bD (list): Base de datos dinamica de estudiantes.
    Salidas:
    - None (imprime un mensaje en consola y genera el archivo 'respaldoXML.xml').
    """
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    with open('rangoAnnos.pkl', 'rb') as archivoAnnos:
            annos = pickle.load(archivoAnnos)
    respaldo = open('respaldoXML.xml', 'w', encoding='utf-8')
    anno = int(annos[0])
    annoFinal = int(annos[1])
    cantidad = annoFinal - anno #Se define para cuantas generaciones se debe crear un respaldo.
    cantidad += 1
    respaldo.write(f'<Estudiantes>\n')
    for e in range(cantidad): #Ciclo que incrementa la generación.
        respaldo.write(f'      <Generación año="{anno}">\n')
        for i in bD: #Ciclo que imprime la entrada de un estudiante de la generación definida en el ciclo anterior.
            generacion = i[2][0:4]
            if generacion == str(anno):
                nombre = f'{i[0][0]} {i[0][1]} {i[0][2]}'
                genero = i[1]
                carne = i[2]
                correo = i[3]
                nota1 = i[4][0]
                nota2 = i[4][1]
                nota3 = i[4][2]
                notaF = i[4][3] 
                if notaF >= 70:
                    resultado = 'Aprobado'
                elif notaF >= 60:
                    resultado = 'Reposición'
                elif notaF < 60:
                    resultado = 'Reprobado'
                if genero == True:
                    genero = 'Masculino'
                else:
                    genero = 'Femenino'
                respaldo.write(f'            <Estudiante carne="{carne}">\n')
                respaldo.write(f'                  <nombre>{nombre}</nombre>\n')
                respaldo.write(f'                  <genero>{genero}</genero>\n')
                respaldo.write(f'                  <correo>{correo}</correo>\n')
                respaldo.write(f'                  <notas>{nota1},{nota2},{nota3},{notaF},{notaF}</notas>\n')
                respaldo.write(f'                  <estado>{resultado}</estado>\n')
                respaldo.write(f'            </Estudiante>\n')
            else:
                continue
        respaldo.write(f'      </Generación>\n')
        anno +=1 #Se incrementa la variable anno para que en el próximo ciclo se imprima la siguiente generación.
    respaldo.write(f'</Estudiantes>')
    return print(f'Su respaldo se genero satisfactoriamente.')
            

    
        
