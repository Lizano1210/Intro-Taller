#
#
#
#

import BDdinamica

#bD = BDdinamica.bdDinamicaES() 

def crearReporte(bD):
    archivo = open('reporteHTML.html','w', encoding='utf-8')
    archivo.write('<html>\n')
    archivo.write('<head><title>Reporte en HTML, Tarea Programada #1</title></head>\n')
    archivo.write('<body>\n')
    archivo.write('<h1>Reporte en HTML, Tarea Programada #1</h1>\n')
    archivo.write("<table border='1'>\n")
    archivo.write('<tr>\n')
    archivo.write('<th>Detalle de notas.</th>\n')
    archivo.write('</tr>\n')
    archivo.write('<tr>\n')
    archivo.write('<th>Nombre</th>\n')
    archivo.write('<th>Apellido 1</th>\n')
    archivo.write('<th>Apellido 2</th>\n')
    archivo.write('<th>Género</th>\n')
    archivo.write('<th>Carné</th>\n')
    archivo.write('<th>Correo</th>\n')
    archivo.write('<th>Notas</th>\n')
    archivo.write('<th>Estado</th>\n')
    archivo.write('</tr>\n')
    for i in bD:
        nombre = i[0][0]
        ap1 = i[0][1]
        ap2 = i[0][2]
        carne = i[2]
        correo = i[3]
        notas = i[4][0:4]
        notaFinal = i[4][3]
        if notaFinal >= 70:
            resultado = 'Aprobado'
        elif notaFinal >= 60:
            resultado = 'Reposición'
        else:
            resultado = 'Reprobado'
        if i[1] == True:
         genero = 'Masculino'
        else:
            genero = 'Femenino'
        archivo.write('<tr>\n')
        archivo.write(f'<td>{nombre}</td><td>{ap1}</td><td>{ap2}</td><td>{genero}</td><td>{carne}</td><td>{correo}</td>' \
                      f'<td>{notas}</td><td>{resultado}</td>\n')
        archivo.write('</tr>\n')
    archivo.write('</table>\n')
    archivo.write('</body>\n')
    archivo.write('</html>')
    archivo.close