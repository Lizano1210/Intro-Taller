#
#
#
#

'''
Reporte XML: Crea un respaldo de la base de datos con un formato de XML.
'''

import BDdinamica
#bD = BDdinamica.bdDinamicaES()

def respaldoXML(bD, annos):
    respaldo = open('respaldoXML.xml', 'w', encoding='utf-8')
    anno = int(annos[0])
    annoFinal = int(annos[1])
    cantidad = annoFinal - anno
    cantidad += 1
    respaldo.write(f'<Estudiantes>\n')
    for e in range(cantidad):
        respaldo.write(f'      <Generación año="{anno}">\n')
        for i in bD:
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
        anno +=1
    respaldo.write(f'</Estudiantes>')
    return print(f'Su respaldo se genero satisfactoriamente.')
            

    
        
