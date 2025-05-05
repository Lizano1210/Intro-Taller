#
#
#
#

import BDdinamica

#bD = BDdinamica.bdDinamicaES() 

def crearReporte(bD):
    aprobados = 0
    reposicion = 0
    reprobados = 0
    cantidadEstudiantes = len(bD)
    reporte = open('reporteHTML.html','w', encoding='utf-8')
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
    reporte.write('   tr:nth-child(even) {\n')
    reporte.write('       background-color: #909090\n')
    reporte.write('   }\n')
    reporte.write('</style>\n')
    reporte.write('</head>\n')
    reporte.write('<body>\n')
    reporte.write('<h1>Reporte en HTML, Tarea Programada #1</h1>\n')
    reporte.write("<table border='1'>\n")
    reporte.write('<tr>\n')
    reporte.write('<th colspan="8">Detalle de notas.</th>\n')
    reporte.write('</tr>\n')
    reporte.write('<tr>\n')
    reporte.write('<th>Nombre</th>\n')
    reporte.write('<th>Apellido 1</th>\n')
    reporte.write('<th>Apellido 2</th>\n')
    reporte.write('<th>Género</th>\n')
    reporte.write('<th>Carné</th>\n')
    reporte.write('<th>Correo</th>\n')
    reporte.write('<th>Notas</th>\n')
    reporte.write('<th>Estado</th>\n')
    reporte.write('</tr>\n')
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
        reporte.write(f'<td>{nombre}</td><td>{ap1}</td><td>{ap2}</td><td>{genero}</td><td>{carne}</td><td>{correo}</td>' \
                      f'<td>{notas}</td><td>{resultado}</td>\n')
        reporte.write('</tr>\n')
    porApro = ((aprobados/cantidadEstudiantes) *100)
    porRepro = ((reprobados/cantidadEstudiantes) *100)
    porRepo = ((reposicion/cantidadEstudiantes) *100)
    reporte.write('<tr>\n')
    reporte.write(f'<th colspan="8">La base de datos posee {cantidadEstudiantes} estudiantes, de los cuales hay: {aprobados} ' \
                  f'aprobados para un {porApro}%, {reposicion} a reposición para un {porRepo}%, {reprobados} reprobados para un {porRepro}%.</th>\n')
    reporte.write('</tr>\n')
    reporte.write('</table>\n')
    reporte.write('</body>\n')
    reporte.write('</html>')
    reporte.close