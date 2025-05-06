#
#
#
#

'''
Reporte HTML: Este archivo genera un reporte en html con todos los estudiantes, sus datos, y un reporte de estadistica
al final. Tambien reespalda ese mismo reporte en un .csv
'''

import BDdinamica
#bD = BDdinamica.bdDinamicaES() 

def crearReporte(bD):
    aprobados = 0
    reposicion = 0
    reprobados = 0
    cantidadEstudiantes = len(bD)
    reporte = open('reporteHTML.html','w', encoding='utf-8')
    respaldo = open('respaldoCSV.csv', 'w')
    respaldo.write('Reporte en HTML Tarea Programada #1 \n')
    respaldo.write('Detalle de notas. \n')
    reporte.write('<html>\n') 
    reporte.write('<head>\n') 
    reporte.write('<title>Reporte en HTML, Tarea Programada #1</title>\n')
    reporte.write('<style>\n')
    reporte.write('    body {\n')
    reporte.write('        font-family: Arial;\n')
    reporte.write('        background-color: #bdafaf\n')
    reporte.write('   }\n')
    reporte.write('   table {\n')
    reporte.write('        border-collapse: collapse;\n')
    reporte.write('        width: 100%;\n')
    reporte.write('        margin-top: 25px;')
    reporte.write('   }\n')
    reporte.write('   th, td {\n')
    reporte.write('       padding: 8px;\n')
    reporte.write('       text-align: center;\n')
    reporte.write('   }\n')
    reporte.write('   th {\n')
    reporte.write('      background-color: #ad91b0;\n')
    reporte.write('   }\n')
    reporte.write('   tr:nth-child(even) {\n')  #Para que las lineas intercalen el color.
    reporte.write('       background-color: #909090\n')
    reporte.write('   }\n')
    reporte.write('</style>\n')
    reporte.write('</head>\n')
    reporte.write('<body>\n')
    reporte.write('<h1>Reporte en HTML, Tarea Programada #1</h1>\n')
    reporte.write("<table border='1'>\n")
    reporte.write('<tr>\n')
    reporte.write('<th colspan="7">Detalle de notas.</th>\n')
    reporte.write('</tr>\n')
    reporte.write('<tr>\n')
    reporte.write('<th>Nombre</th>\n')
    reporte.write('<th>Apellidos</th>\n')
    reporte.write('<th>Género</th>\n')
    reporte.write('<th>Carné</th>\n')
    reporte.write('<th>Correo</th>\n')
    reporte.write('<th>Notas</th>\n')
    reporte.write('<th>Estado</th>\n')
    reporte.write('</tr>\n')
    respaldo.write('Nombre,Apellidos,Género,Carné,Correo,Notas,Estado \n')
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
            aprobados += 1
        elif notaFinal >= 60:
            resultado = 'Reposición'
            reposicion += 1
        elif notaFinal < 60:
            resultado = 'Reprobado'
            reprobados += 1
        if i[1] == True:
         genero = 'Masculino'
        else:
            genero = 'Femenino'
        reporte.write('<tr>\n')
        reporte.write(f'<td>{nombre}</td><td>{ap1} {ap2}</td><td>{genero}</td><td>{carne}</td><td>{correo}</td>' \
                      f'<td>{notas}</td><td>{resultado}</td>\n')
        reporte.write('</tr>\n')
        respaldo.write(f'{nombre},{ap1} {ap2},{genero},{carne},{correo},{notas[0]} {notas[1]} {notas[2]} {notas[3]},{resultado} \n')
    porApro = ((aprobados/cantidadEstudiantes) *100) #% De cuantos aprobaron
    porApro = round(porApro, 1)
    porRepro = ((reprobados/cantidadEstudiantes) *100) #% De cuantos reprobaron
    porRepro = round(porRepro, 1)
    porRepo = ((reposicion/cantidadEstudiantes) *100) #% De cuantos van a reposición
    porRepo = round(porRepo, 1)
    reporte.write('<tr>\n')
    reporte.write(f'<th colspan="7">La base de datos posee {cantidadEstudiantes} estudiantes, de los cuales hay: {aprobados} ' \
                  f'aprobados para un {porApro}%, {reposicion} a reposición para un {porRepo}%, {reprobados} reprobados para un {porRepro}%.</th>\n')
    reporte.write('</tr>\n')
    reporte.write('</table>\n')
    reporte.write('</body>\n')
    reporte.write('</html>')
    reporte.close
    return print(f'Su reporte se genero satisfactoriamente.')