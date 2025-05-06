#
#
#
#

'''
Gestión de curva: Aplica un redondeo a la nota final de todos los estudiantes, el porcentaje de rendondeo 
es ingresado por el usuario, posterior se separa a los estudiantes segun su estado final y se crea un 
reporte html para cada estado respectivamente.
'''

def gestionCurva(bD):
    while True: # Se solicita curva al usuario.
        try:
            curva = int(input(f'Por favor ingrese el porcentaje de curva que desea aplicar a los estudiantes.\n'))
            if curva < 0 or curva > 100:
                print('El porccentaje ingresado debe encontrarse entre 0% y 100%')
                continue
            break
        except ValueError:
            print('Debe ingresar unicamente un número entero.')
    for i in bD: # Se aplica la curva en la base de datos.
        notas = i[4] 
        notaF = (i[4][4] + (notas[4] * (curva/100)))
        notaF = round(notaF, 1)
        notasCurva = notas[:4] + (notaF,)
        i[4] = notasCurva
    return reportePorEstado(bD)


def reportePorEstado(bD):
    aprobados = 0
    reposicion = 0
    reprobados = 0
    cantidadEstudiantes = len(bD)
    reporte = open('aprobadosHTML.html','w', encoding='utf-8')
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
    reporte.write('<h1>Reporte de estudiantes aprobados, Tarea Programada #1.</h1>\n')
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
    for i in bD:
        nombre = i[0][0]
        ap1 = i[0][1]
        ap2 = i[0][2]
        carne = i[2]
        correo = i[3]
        notas = i[4][0:4]
        notaFinal = float(i[4][4]) #Nota a la que se le aplico la curva
        if notaFinal >= 70:
            resultado = 'Aprobado'
            aprobados += 1
        else:
            continue
        if i[1] == True:
         genero = 'Masculino'
        else:
            genero = 'Femenino'
        reporte.write('<tr>\n')
        reporte.write(f'<td>{nombre}</td><td>{ap1} {ap2}</td><td>{genero}</td><td>{carne}</td><td>{correo}</td>' \
                      f'<td>{notas}</td><td>{resultado}</td>\n')
        reporte.write('</tr>\n')
    reporte.write('<tr>\n')
    reporte.write(f'<th colspan="7">Para el estado "Aprobado", hay {aprobados} cantidad de estudiantes luego de la curva, del total de {cantidadEstudiantes} ' \
                  f'estudiantes, Si hubiera alumnos que cambiaron de estado deben estar en su archivo correspondiente.</th>\n.')
    reporte.write('</tr>\n')
    reporte.write('</table>\n')
    reporte.write('</body>\n')
    reporte.write('</html>')
    reporte.close
    print(f'Su reporte de aprobados se genero satisfactoriamente.')
    reporte = open('reposicionHTML.html','w', encoding='utf-8')
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
    reporte.write('<h1>Reporte de estudiantes para reposición, Tarea Programada #1.</h1>\n')
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
    for i in bD:
        nombre = i[0][0]
        ap1 = i[0][1]
        ap2 = i[0][2]
        carne = i[2]
        correo = i[3]
        notas = i[4][0:4]
        notaFinal = i[4][4] #Nota a la que se le aplico la curva
        if notaFinal >= 60:
            resultado = 'Reposición'
            reposicion += 1
        else:
            continue
        if i[1] == True:
         genero = 'Masculino'
        else:
            genero = 'Femenino'
        reporte.write('<tr>\n')
        reporte.write(f'<td>{nombre}</td><td>{ap1} {ap2}</td><td>{genero}</td><td>{carne}</td><td>{correo}</td>' \
                      f'<td>{notas}</td><td>{resultado}</td>\n')
        reporte.write('</tr>\n')
    reporte.write(f'<th colspan="7">Para el estado "Reposición", hay {reposicion} cantidad de estudiantes luego de la curva, del total de {cantidadEstudiantes} ' \
                  f'estudiantes, Si hubiera alumnos que cambiaron de estado deben estar en su archivo correspondiente.</th>\n.')
    reporte.write('</tr>\n')
    reporte.write('</table>\n')
    reporte.write('</body>\n')
    reporte.write('</html>')
    reporte.close
    print(f'Su reporte de estudiantes a reposición se genero satisfactoriamente.')
    reporte = open('reprobadosHTML.html','w', encoding='utf-8')
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
    reporte.write('<h1>Reporte de estudiantes reprobados, Tarea Programada #1.</h1>\n')
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
    for i in bD:
        nombre = i[0][0]
        ap1 = i[0][1]
        ap2 = i[0][2]
        carne = i[2]
        correo = i[3]
        notas = i[4][0:4]
        notaFinal = i[4][4] #Nota a la que se le aplico la curva
        if notaFinal < 60:
            resultado = 'Reprobado'
            reprobados += 1
        else:
            continue
        if i[1] == True:
         genero = 'Masculino'
        else:
            genero = 'Femenino'
        reporte.write('<tr>\n')
        reporte.write(f'<td>{nombre}</td><td>{ap1} {ap2}</td><td>{genero}</td><td>{carne}</td><td>{correo}</td>' \
                      f'<td>{notas}</td><td>{resultado}</td>\n')
        reporte.write('</tr>\n')
    reporte.write(f'<th colspan="7">Para el estado "Reprobado", hay {reprobados} cantidad de estudiantes luego de la curva, del total de {cantidadEstudiantes} ' \
                  f'estudiantes, Si hubiera alumnos que cambiaron de estado deben estar en su archivo correspondiente.</th>\n.')
    reporte.write('</tr>\n')
    reporte.write('</table>\n')
    reporte.write('</body>\n')
    reporte.write('</html>')
    reporte.close
    print(f'Su reporte de estudiantes a reposición se genero satisfactoriamente.')
    return bD



