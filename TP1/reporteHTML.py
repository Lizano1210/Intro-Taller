#
#
#
#

import BDdinamica

bD = BDdinamica.bdDinamicaES() 

def crearReporte(bD):
    archivo = open('reporteHTML.html','w')
    archivo.write('<html>\n')
    archivo.write('<head><title>Reporte en HTML, Tarea Programada #1</title></head>\n')
    archivo.write('<body>\n')
    archivo.write('<h1>Detalle de Notas</h1>\n')
    archivo.write("<table border='1'>\n")
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
        if i[4][4] >= 70:
            resultado = 'Aprobado'
        if i[4][4] >= 60:
            resultado = 'Reposición'
        else:
            resultado = 'Reprobado'
        if i[1] == True:
         genero = 'Masculino'
        else:
            genero = 'Femenino'
    
    archivo.write('</table>\n')
    archivo.write('</body>\n')
    archivo.write('</html>')
