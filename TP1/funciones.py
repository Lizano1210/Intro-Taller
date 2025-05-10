# Elaborado por: Elías Lizano y Joshua Brenes
# Fecha de creación: 22/4/2025 7:00p.m
# Última modificación: 9/52025 11:00p.m
# Versión de python: 3.12.3

'''
FUNCIONES: En este archivo se encuentras todas las funciones usadas en la tarea programada, todas tienen 
separadores para su más sencilla busqueda.
'''

# Importación de librerias / modulos.
import names
import random 
import math 
import re
import pickle
import smtplib # Para reto 7

# --------------------------------------------------------------------------------------------------------- #
# RETO 1: BD Dínamica
# --------------------------------------------------------------------------------------------------------- #

'''
REGISTRAR ESTUDIANTE: Este segmento contiene la función que permite al usuario registrar nuevos estudiantes
en la base de datos.
'''

# Fuente 1 Generados aleatoriamente
def generaNombres(entrada,annoInicial,annoFinal,nota1,nota2,nota3):
    """
    Funcionamiento: Genera una lista de estudiantes ficticios con datos como nombre, género, carné, correo y notas, 
    y los guarda en un archivo de texto. También retorna la base de datos generada con todos los registros.
    Entradas:
    - entrada (int): Cantidad de estudiantes a generar.
    - annoInicial (int): Año mínimo para generar el carné estudiantil.
    - annoFinal (int): Año máximo para generar el carné estudiantil.
    - nota1 (float): Porcentaje asignado al primer examen.
    - nota2 (float): Porcentaje asignado al segundo examen.
    - nota3 (float): Porcentaje asignado al tercer examen.
    Salidas:
    - estudiantesGenerados (list): Lista de estudiantes generados. Cada estudiante es una lista con la estructura:
    [(nombre, apellido1, apellido2), sexo (bool), carné (str), correo (str),
    (nota1, nota2, nota3, nota_final, nota_final)].
    """
    fuente = open('testbD.txt', 'w') # Archivo no necesario se usa para testing
    estudiantesGenerados = []
    for i in range(entrada):
        sexo = random.choice([True, False])
        if sexo == True:
            nombre = names.get_first_name(gender = 'Male')
        else:
            nombre = names.get_first_name(gender = 'Female')
        pApellido = names.get_last_name()
        sApellido = names.get_last_name() 
        while True:
            if pApellido == sApellido:
                sApellido = names.get_last_name()
            else:
                break
        sedeEstudiante = sede()
        carne = f'{random.randint(int(annoInicial),int(annoFinal))}{random.choice(sedeEstudiante[1])}{random.randint(0,9999):04}'
        correo = f'{quitaTilde(nombre[0].lower())}{quitaTilde(pApellido.lower())}{carne[6:]}@estudianteclvz.cr'
        notas = (random.randint(1,100), random.randint(1,100), random.randint(1,100), 0.0, 0.0)
        notaReal1 = notas[0] * (nota1/100)
        notaReal2 = notas[1] * (nota2/100)
        notaReal3 = notas [2] * (nota3/100)
        notaFinal = (notaReal1+notaReal2+notaReal3)
        notaFinal = round(notaFinal, 1)
        notas = (notas[0], notas[1], notas[2], notaFinal, notaFinal)
        estudiante = [(nombre, pApellido, sApellido), sexo, carne, correo, notas]
        estudiantesGenerados.append(estudiante)
        fuente.write(f'{estudiante[0][0]}, {estudiante[0][1]}, {estudiante[0][2]}, {estudiante[1]}, {estudiante[2]}, {estudiante[3]}, {estudiante[4]} \n')
    fuente.close()
    print(f'Se genero {entrada} estudiantes')
    return estudiantesGenerados

#Fuente 2 Extraidos de archivo
def leeNombres(porcentaje,annoInicial,annoFinal,nota1,nota2,nota3):
    """
    Funcionamiento: Lee nombres desde un archivo preexistente de estudiantes, selecciona un porcentaje aleatorio 
    de ellos, les genera un carné, correo y notas ficticias, y agrega esta nueva información a un archivo de salida. 
    Devuelve la base de datos con los estudiantes seleccionados y completados.
    Entradas:
    - porcentaje (float): Porcentaje de estudiantes que se deben seleccionar del archivo.
    - annoInicial (int): Año mínimo para generar el carné estudiantil.
    - annoFinal (int): Año máximo para generar el carné estudiantil.
    - nota1 (float): Porcentaje asignado al primer examen.
    - nota2 (float): Porcentaje asignado al segundo examen.
    - nota3 (float): Porcentaje asignado al tercer examen.
    Salidas:
    - estudiantesLeidos (list): Lista de estudiantes seleccionados y procesados. 
    Cada uno tiene la estructura:
    [(nombre, apellido1, apellido2), sexo (bool), carné (str), correo (str), 
    (nota1, nota2, nota3, nota_final, nota_final)].
    """
    estudiantesLeidos = []
    fuenteEstudiantes = open('estudiantes.txt','r')
    lineas = fuenteEstudiantes.readlines()
    fuenteEstudiantes.close()
    cantidad = len(lineas) #Cantidad de estudiantes
    redondeo = math.ceil(cantidad * (porcentaje/100))
    nombresExtraidos = random.sample(lineas, redondeo)
    fuente = open('testbD.txt', 'a') # Archivo no necesario se usa para testing
    for i in nombresExtraidos:
        nombre = i.strip()
        nombre = i.split(',')
        nombreEst = (nombre[0])
        Apellido1 = (nombre[1])
        Apellido2 = (nombre[2])
        if nombre[3] == 'Masculino\n':
            sexo = True
        else:
            sexo = False
        sedeEstudiante = sede()
        carne = f'{random.randint(int(annoInicial),int(annoFinal))}{random.choice(sedeEstudiante[1])}{random.randint(0,9999):04}'
        correo = f'{quitaTilde(nombreEst[0].lower())}{quitaTilde(Apellido1.lower())}{carne[6:]}@estudianteclvz.cr'
        notas = (random.randint(1,100), random.randint(1,100), random.randint(1,100), 0.0, 0.0)
        notaReal1 = notas[0] * (nota1/100)
        notaReal2 = notas[1] * (nota2/100)
        notaReal3 = notas [2] * (nota3/100)
        notaFinal = (notaReal1+notaReal2+notaReal3)
        notaFinal = round(notaFinal, 1)
        notas = (notas[0], notas[1], notas[2], notaFinal, notaFinal) 
        estudiantesLeidos.append([(nombreEst,Apellido1,Apellido2),sexo,carne,correo, notas])
        fuente.write(f'{nombre[0]}, {nombre[1]}, {nombre[2]}, {sexo}, {carne}, {correo}, {notas}\n')
    fuente.close()
    return estudiantesLeidos

def bdDinamicaES():
    """
    Funcionamiento: Solicita datos al usuario para generar una base de datos dinámica de estudiantes, 
    combinando estudiantes generados aleatoriamente con otros leídos desde un archivo. 
    Valida los datos ingresados (años, porcentajes de notas, etc.) y construye una lista de estudiantes 
    con carné, correo y notas ficticias.
    Salidas:
    - bdDinamica (list): Lista combinada de estudiantes generados y leídos. Cada estudiante tiene la estructura:
    [(nombre, apellido1, apellido2), sexo (bool), carné (str), correo (str), 
    (nota1, nota2, nota3, nota_final, nota_final)].
    - annos (tuple): Tupla con el año inicial y final considerados para la generación de carnés.
    """
    bdDinamica = []
    while True:
        try:
            cantidad = int(input('Ingrese la cantidad de estudiantes de la cual desea la lista: '))
            porcentaje = int(input('Ingrese el porcentaje que se le aplicara a la cantidad: '))
            annoInicial = input('Ingrese el primer año de la primera generación a tener en cuenta: ')
            annoFinal = input('Ingrese el primer año de la última generación a tener en cuenta generación a tener en cuenta: ')
            if re.match(r'^\d{4}$', annoInicial) is None or re.match(r'^\d{4}$', annoFinal) is None:
                print('Debe ingresar un año unicamente. Con sus 4 dígitos.')
                continue
            if annoFinal < annoInicial:
                print('La última generación no puede ser anterior a la primera.')
                continue
            print('Notas, a continuación ingrese el porcentaje de valor de cada una de sus asignaciones. \n' \
            'Recuerde que los 3 porcentajes deben sumar 100.')
            nota1 = int(input('Ingrese el primer porcentaje de nota: '))
            nota2 = int(input('Ingrese el segundo porcentaje de nota: '))
            nota3 = int(input('Ingrese el tercer porcentaje de nota: '))
            porceNotas = (nota1,nota2,nota3)
            total = (nota1 + nota2 + nota3)
            if total != 100:
                print('Sus porcentajes de notas son invalidos, deben sumar 100')
                continue
            break
        except ValueError:
            print('Datos invalidos, solo debe ingresar números enteros.')
    entrada = math.ceil(cantidad * (porcentaje/100))
    fuente1 = generaNombres(entrada,annoInicial,annoFinal,nota1,nota2,nota3)
    fuente2 = leeNombres(porcentaje,annoInicial,annoFinal,nota1,nota2,nota3)
    bdDinamica = fuente1
    for i in fuente2:
        bdDinamica.append(i)
    annos = (annoInicial,annoFinal)
    with open('baseDatosDinamica.pkl', 'wb') as archivobD:
        pickle.dump(bdDinamica, archivobD)
    with open('rangoAnnos.pkl', 'wb') as archivoAnnos:
        pickle.dump(annos, archivoAnnos)
    with open('porcentaje.pkl', 'wb') as archivoPorce:
        pickle.dump(porceNotas, archivoPorce)
    #print(bdDinamica)
    return bdDinamica,annos

def sede():
    """
    Funcionamiento: Lee las sedes disponibles desde el archivo 'sedes.txt', asigna un código secuencial 
    (anteponiendo un 0) a cada una y retorna tanto la lista completa de sedes con sus códigos como una lista 
    sola de códigos.
    Salidas:
    - list: Una lista con dos elementos:
    - sedes (list): Lista de listas, cada una con el nombre de la sede y su código correspondiente.
    - codSedes (list): Lista de solo los códigos asignados a cada sede.
    """
    sedes = []
    codSedes = []
    archivoSedes = open('sedes.txt','r')
    lineasSedes = archivoSedes.readlines()
    archivoSedes.close()
    cantidadSedes = len(lineasSedes)
    contador = 0
    for i in (lineasSedes):
        sedeTexto = i.replace('\n','') # Eliminamos los \n presentes en el texto del archivo.
        contador += 1
        codSede = '0' + str(contador) # Variable con solo los codigos de sede
        sedeCompleta = [sedeTexto, codSede] # Variable con las sedes con nombre y codigo
        codSedes.append(codSede)
        sedes.append(sedeCompleta)
    #print(sedes)
    with open('sedes.pkl', 'wb') as archivoSedes:
        pickle.dump(sedes, archivoSedes)
    with open('sedesCod.pkl', 'wb') as archivoCodSedes:
        pickle.dump(codSedes, archivoCodSedes)
    return [sedes, codSedes]

def quitaTilde(texto): #Importante leer documentación de la función.
    '''
    En esta función utilizamos un método encontrado en internet que nos ayuda
    a eliminar tildes de los nombres, esto es especialmente importante por el
    punto 7 de la tarea. Donde los correos electronicos no pueden llevar tildes 
    para que el código sea funcional.
    Tengo entendido que ningún elemento lógico usado en esta función no ha sido utilizado
    en clase pero realizo esta aclaración por si se ve un poco fuera de lugar con respecto
    a lo usado en clase.
    '''
    import unicodedata #Es un modúlo que nos ayuda con manejar la codificación y descomposición de caracteres unicode
                       #Como las tildes en nuestro caso.
    texto = unicodedata.normalize('NFD', texto)  # normalize separa las letras con caracter combinante como tilde de sus letras
                                                 # Es decir si tenemos á separa ese caracter en a y '.
    sinTilde = '' # Se crea texto que se convertira en la misma palabra sin  las letras con tilde.
    for letra in texto:
        if not unicodedata.combining(letra): # combining revisa si la letra tiene un caracter combinante como la tilde.
            sinTilde += letra 
    return sinTilde

# --------------------------------------------------------------------------------------------------------- #
# RETO 2: Registrar estudiante.
# --------------------------------------------------------------------------------------------------------- #

'''
REGISTRAR ESTUDIANTE: Este segmento contiene la función que permite al usuario registrar nuevos estudiantes
en la base de datos.
'''

def registrarEstudianteES():
    """
    Funcionamiento: Registra un nuevo estudiante en la base de datos dinámica. Solicita datos personales, 
    carné, correo y notas. Realiza validaciones para formato, duplicados y consistencia con los rangos de 
    años definidos. Calcula la nota final según los porcentajes establecidos y actualiza la base de datos.

    Entradas:
    - Ninguna directa (solicita datos al usuario vía consola).
    - Carga los siguientes archivos:
    - 'baseDatosDinamica.pkl': para obtener la base actual.
    - 'porcentaje.pkl': para calcular la nota final.
    - 'rangoAnnos.pkl': para validar el año de ingreso.
    - También usa la función `sede()` para obtener códigos de sede.

    Salidas:
    - Actualiza la base de datos con un nuevo estudiante.

    Notas:
    - Se realiza una validación estricta del formato del carné usando expresiones regulares.
    - Se previene el ingreso duplicado de carné mediante una verificación previa.
    - El correo es generado con base en reglas específicas de formato y también validado con regex.
    - La nota final se calcula con pesos definidos por el usuario anteriormente y redondeo implícito mediante la fórmula.
    """

    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    with open('porcentaje.pkl', 'rb') as archivoPorce:
         porcentaje = pickle.load(archivoPorce)
    with open('rangoAnnos.pkl', 'rb') as archivoAnnos:
            annos = pickle.load(archivoAnnos)
    sedes = sede()[1]
    nombre = str(input("Ingrese el nombre del estudiante: "))
    apellido1 = str(input("Ingrese el primer apellido del estudiante: "))
    apellido2 = str(input("Ingrese el segundo apellido del estudiante: ")) 
    nombreCompleto = (nombre, apellido1, apellido2)
    #------------ Este bloque se encarga de hacer una lista con las generaciones que ingreso el usuario.-----
    annoInicial = int(annos[0])
    listaAnnos = []
    while annoInicial <= int(annos[1]):
        listaAnnos.append(annoInicial)
        annoInicial +=1
    #----------- Fin bloque generaciones --------------------------------------------------------------------
    while True:
        try:
            genero = input("Digite (1) para masculino o (2) para femenino: ")
            if re.match(f'^[12]$', genero) is None:
                print('Solo debe ingresar 1 o 2.')
                continue
            if genero == '1':
                genero = True
            else:
                genero = False
            break
        except ValueError:
            print('El dato ingresado no es valido, vuelvalo a intentar.')
    while True:
        try:   
            carne = str(input("Ingrese el número de carne del estudiante: \n"
                              "Debe formarse asi, primeros 4 digitos, año en el que ingreso a estudiar.\n"
                              "Su número de sede (que siempre sera un 0 seguido de su numero de sede.) \n"
                              "Los 4 ultimos dígitos son al azar a su elección: "))
            if re.match(f'^\d{{4}}({"|".join(sedes)})\d{{4}}$', carne) is None: 
                print('El carne no es valido, vuelvalo a intentar.')
                continue
            existe = False
            for i in bD:
                if carne == i[2]:
                    existe = True
                    break
                else:
                    continue
            if existe == True:
                print('El carne ya existe en la base de datos, vuelvalo a intentar.')
                continue
            annoIngreso = int(carne[0:4])
            if annoIngreso not in listaAnnos:
                print('El año de ingreso que dígito no existe dentro de los que componen la base de datos.\n' \
                f'{listaAnnos}')
                continue
            break
        except ValueError:
            print('El dato ingresado no es válido, vuelvalo a intentar.')
    while True:
        try:
            correo = str(input("Cree su correo electrónico:\n" \
                               "Escriba la primera letra de su nombre seguida de su primer apellido y\n" \
                               "los últimos 4 digitos de su carnet.\n"
                               "La primer letra de su nombre y su apellido DEBEN IR EN MINUSCULA: \n"))
            if re.match(f'^[{nombre[0].lower()}]({apellido1.lower()})({carne[-4:]})$', correo) is None:
                print('Su correo esta mal formado\n' \
                      'Escriba la primera letra de su nombre seguida de su primer apellido y\n' \
                      'los últimos 4 digitos de su carnet.\n' \
                      'La primer letra de su nombre y su apellido DEBEN IR EN MINUSCULA: \n')
                continue
            else:
                correo += '@estudiantec.cr'
                break
        except ValueError:
            print('El dato ingresado no es valido, intentelo de nuevo.')
    while True:
         try:    
            n1 = int(input("Ingrese la nota del primer parcial: "))
            if re.match('^([0-9]|[1-9][0-9]|100)$', str(n1)) is None:
                 print('El numero ingresado debe estar en el rango de 0-100.')
                 continue
            n2 = int(input("Ingrese la nota del segundo parcial: "))
            if re.match('^([0-9]|[1-9][0-9]|100)$', str(n2)) is None:
                 print('El numero ingresado debe estar en el rango de 0-100.')
                 continue
            n3 = int(input("Ingrese la nota del tercer parcial: "))
            if re.match('^([0-9]|[1-9][0-9]|100)$', str(n3)) is None:
                 print('El numero ingresado debe estar en el rango de 0-100.')
                 continue
            break
         except ValueError:
              print('El dato ingresado no es valido. Solo debe ingresar números enteros.')
    nFinal = (n1 * (porcentaje[0]/100))+(n2 * (porcentaje[1]/100))+(n3 * (porcentaje[2]/100))
    notas = (n1, n2, n3, nFinal, nFinal)
    estudiante = [nombreCompleto, genero, carne, correo, notas]
    bD.append(estudiante)
    #print(bD)
    with open('baseDatosDinamica.pkl', 'wb') as archivobD:
        pickle.dump(bD, archivobD)
    return

# --------------------------------------------------------------------------------------------------------- #
# RETO 3: Generar reporte HTML y .csv
# --------------------------------------------------------------------------------------------------------- #

'''
Reporte HTML: Este segmento genera un reporte en html con todos los estudiantes, sus datos, y un reporte de estadistica
al final. Tambien reespalda ese mismo reporte en un .csv
'''

def crearReporte():
    """
    Funcionamiento: Genera un reporte visual en HTML y un respaldo en CSV con la información de los estudiantes 
    almacenados en una base de datos. El reporte incluye detalles personales, notas parciales, nota final y el 
    estado del estudiante (aprobado, reposición o reprobado).
    Entradas:
    - bD (list): Base de datos dinamica de estudiantes. 
    Salidas:
    - None (imprime en consola un mensaje confirmando la generación del reporte y guarda dos archivos):
    - 'reporteHTML.html': Reporte visual en formato HTML.
    - 'respaldoCSV.csv': Respaldo en formato CSV con la misma información.
    """
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
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
        notaFinal = i[4][4]
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

# --------------------------------------------------------------------------------------------------------- #
# RETO 4: Respaldo en XML
# --------------------------------------------------------------------------------------------------------- #

'''
Reporte XML: Crea un respaldo de la base de datos con un formato de XML.
'''

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
            
# --------------------------------------------------------------------------------------------------------- #
# RETO 5: Reporte por género
# --------------------------------------------------------------------------------------------------------- #

'''
REPORTE POR GÉNERO: Este archivo se encarga de crear 2 reportes .docx, uno de hombres y otro de mujeres
donde se muestres sus datos ordenados por mejores notas.
'''

def determinarGeneroyOrdenar():
    """
    Funcionamiento: Clasifica a los estudiantes en hombres y mujeres, y genera listas ordenadas 
    por nota final en orden descendente. Luego, genera un reporte por género con los datos organizados. 
    Se utiliza una lógica de selección iterativa para encontrar al estudiante con la mejor nota de cada género sin repetir registros.

    Entradas:
    - Ninguna directamente (la función carga internamente la base de datos desde un archivo pickle).

    Salidas:
    - None (solo genera reportes llamando a la función `reporteGenero`).

    Nota: Se corrigió un bug inicializando los máximos (`maxH`, `maxM`) como `(None, 0)` en lugar de `(0, 0)` 
    para evitar que se agregue un registro inválido a las listas de hombres o mujeres.
    """

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
      """
      Funcionamiento: Genera dos reportes en formato .docx (en realidad archivos de texto plano con extensión .docx) 
      con información de estudiantes hombres y mujeres, incluyendo sus notas, nombre, carné y correo. 
      También muestra el porcentaje de cada grupo respecto al total.

      Entradas:
      - bD (list): Base de datos completa de estudiantes.
      - listaHombres (list): Lista de estudiantes identificados como hombres.
      - listaMujeres (list): Lista de estudiantes identificadas como mujeres.

      Salidas:
      - None (solo imprime un mensaje indicando que los reportes fueron generados).
      """

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
      
# --------------------------------------------------------------------------------------------------------- #
# RETO 6: Gestionar curva.
# --------------------------------------------------------------------------------------------------------- #

'''
Gestión de curva: Aplica un redondeo a la nota final de todos los estudiantes, el porcentaje de rendondeo 
es ingresado por el usuario, posterior se separa a los estudiantes segun su estado final y se crea un 
reporte html para cada estado respectivamente.
'''

def gestionCurva():
    """
    Funcionamiento: Solicita al usuario un porcentaje de curva y lo aplica a la nota final de todos los estudiantes
    en la base de datos. Actualiza la nota final curva para cada estudiante y luego genera un reporte por estado
    (usando la función `reportePorEstado`).
    Entradas:
    - bD (list): Base de datos dinamica de estudiantes.
    Salidas:
    - dict: Diccionario generado por `reportePorEstado()` con conteo de estudiantes según su estado académico
    (Aprobado, Reposición, Reprobado).
    """
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
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
    with open('baseDatosDinamica.pkl', 'wb') as archivobD:
        pickle.dump(bD, archivobD)
    return reportePorEstado(bD)


def reportePorEstado(bD):
    """
    Funcionamiento: Genera tres archivos HTML que contienen reportes visuales separados de estudiantes aprobados,
    en reposición y reprobados según su nota final ajustada (nota con curva). También muestra la cantidad de
    estudiantes en cada estado.
    Entradas:
    - bD (list): Base de datos dinamica de estudiantes.
    Salidas:
    - list: Retorna la misma base de datos `bD` sin modificaciones estructurales, solo con las notas finales curvas
    ya actualizadas.
    """
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
    print(f'Su reporte de estudiantes reprobados se genero satisfactoriamente.')
    return bD

# --------------------------------------------------------------------------------------------------------- #
# RETO 7: Envió de correos para reposición.
# --------------------------------------------------------------------------------------------------------- #

def determinarReposicion():
    """
    Funcionamiento: Recorre la base de datos de estudiantes para identificar aquellos que deben 
    realizar examen de reposición (nota final entre 60 y 69.99). Luego, genera y envía correos a cada
    uno de ellos informando su situación.

    Entradas:
    - Ninguna (la función carga los datos desde un archivo pickle).

    Salidas:
    - str: Resultado devuelto por la función que envía los correos a los estudiantes en reposición.
    """
    # Importación de base de datos e inicialización de variables.
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    listaReposicion = []
    # --------------------------------------------------------- #        
    for i in bD:
        notaFinal = i[4][4]
        if notaFinal >= 70:
            continue
        elif notaFinal >= 60:
            listaReposicion.append(i)
        elif notaFinal < 60:
            continue
    return enviarCorreos(listaReposicion)

def enviarCorreos(listaReposicion):
     """
    Funcionamiento: Envía un correo electrónico personalizado a cada estudiante en estado de reposición, 
    utilizando SMTP con conexión segura. El mensaje informa sobre la nota final y los detalles del 
    examen de reposición.

    Entradas:
    - listaReposicion: Lista de estudiantes que deben reponer (cada elemento contiene nombre, cédula, sede, correo y notas).

    Salidas:
    - str: Mensaje confirmando que los correos fueron enviados satisfactoriamente.
    """
     # Importación de funciones e inicialización de variables.
     from email.mime.text import MIMEText   
     from email.mime.multipart import MIMEMultipart
     mail = 'testlv@lizano.live'
     pswrd = 'Testlv123.'
     # ----------------------------------------------------- # 
     with smtplib.SMTP_SSL('smtp.hostinger.com', 465) as server:
           server.login(mail, pswrd)
            # Construcción del correo.
           for i in listaReposicion:
                correoEST = i[3]
                nombre = f'{i[0][0]} {i[0][1]} {i[0][2]}'
                # Un objeto Mime es un tipo de objeto que contiene varias partes de un mensaje, asunto, destino, origen etc...
                correo = MIMEMultipart() # Se le aplica a las variable las propiedades de un objeto MIME
                correo['Subject'] = 'Examen de Reposición'
                correo['From'] = mail
                correo['To'] = correoEST
                cuerpo = f'''
Estimado/a estudiante, {nombre}.

Se le informa que debido a que su nota final fue {i[4][4]}, usted se encuentra en estado de reposición.
Debe presentarse el día 12 de Octubre a las 3:00p.m con identificación personal y su material de trabajo.

Saludos coordiales,
Coordinación Académica
'''
                correo.attach(MIMEText(cuerpo, 'plain', 'utf-8')) # ERROR CORREGIDO: Agregamos utf-8 para evitar problemas con caracteres especiales.
                msg = correo.as_string()
                # Conexión al servidor 
                server.sendmail(mail, correoEST, msg)
     return 'Correos enviados satisfactoriamente.'

# --------------------------------------------------------------------------------------------------------- #
# RETO 8: Aplazados en al menos 2 rubros (.pdf)
# --------------------------------------------------------------------------------------------------------- #

'''
APLAZADOS EN AL MENOS 2 RUBROS(.pdf):
'''

def determinarAplazados():
    """
    Funcionamiento: Identifica a los estudiantes que han reprobado al menos dos rubros 
    y genera un reporte detallado con estadísticas relacionadas.

    Entradas:
    - No recibe entradas externas. La información se extrae directamente desde el archivo 
    'baseDatosDinamica.pkl'.

    Salidas:
    - Llama a la función 'reporteAplazados' para generar un archivo PDF con los resultados y muestra 
    un mensaje de confirmación.
    """
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
      """
    Funcionamiento: Genera un archivo PDF de texto plano con un reporte de estudiantes que han reprobado 
    al menos dos rubros (exámenes), incluyendo sus datos, estadísticas de notas y conteo de casos.

    Entradas:
    - listaAplazados: Lista con los estudiantes que reprobaron al menos dos rubros.
    - totalEstudiantes: Cantidad total de estudiantes en la base de datos.
    - notaMin: Nota mínima registrada entre los aplazados.
    - notaMax: Nota máxima registrada entre los aplazados.
    - repro2: Cantidad de estudiantes que reprobaron exactamente dos rubros.
    - repro3: Cantidad de estudiantes que reprobaron los tres rubros.

    Salidas:
    - Imprime un mensaje indicando que el reporte fue generado correctamente y guarda el archivo 
    'aplazados2Rubros.pdf'.
    """

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

# --------------------------------------------------------------------------------------------------------- #
# RETO 9: Estadística por generación
# --------------------------------------------------------------------------------------------------------- #

'''
Estadística por generación: Genera un reporte por generación de los estudiantes reprobados, aprobados
y a reposición presentes en cada una.
'''

def estadisticaGeneracion():
        """
        Funcionamiento: Genera e imprime estadísticas académicas por generación en un rango de años, 
        mostrando la cantidad de estudiantes aprobados, reprobados y en reposición, tanto por generación 
        como en total.

        Entradas:
        - No recibe parámetros directamente. Carga internamente dos archivos:
        - 'baseDatosDinamica.pkl': contiene la base de datos de los estudiantes.
        - 'rangoAnnos.pkl': contiene el año inicial y final del rango a analizar.

        Salidas:
        - Imprime estadísticas en pantalla y no retorna ningún valor.
        """
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

# --------------------------------------------------------------------------------------------------------- #
# RETO 10: Reporte por sede con buen rendimiento.
# --------------------------------------------------------------------------------------------------------- #

def determinarSede():
    """
    Funcionamiento: Solicita al usuario seleccionar una sede válida y muestra los estudiantes con 
    buen rendimiento académico en esa sede.

    Entradas:
    - No recibe parámetros directamente. Carga internamente tres archivos:
    - 'sedes.pkl': contiene los nombres y ubicaciones de las sedes.
    - 'sedesCod.pkl': contiene los códigos numéricos válidos de las sedes.
    - 'baseDatosDinamica.pkl': contiene la base de datos dinámica de estudiantes.

    Salidas:
    - Llama a la función generarReporteSede con los datos cargados y el código de sede seleccionado.
    """
    count = 0
    with open('sedes.pkl', 'rb') as archivoSedes:
        sedes = pickle.load(archivoSedes)
    with open('sedesCod.pkl', 'rb') as archivoCodSedes:
        codSedes= pickle.load(archivoCodSedes)
    with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
    print(f'Seleccione la sede de la cuál desea conocer sus estudiantes con mejor rendimiento: \n'
          f'')
    for i in sedes:
         print(f'{i[0]} --- {i[1]}.\n')
         count += 1
    print('')
    while True:
         try:
              sedeSelect = int(input('Ingrese el código de la sede: '))
              if re.match(f'^({"|".join(str(codSedes))})$', str(sedeSelect)) is None:
                   print('Opción Invalida, Ingrese unicamente un código de sede.')
                   continue
              break
         except ValueError:
              print('Opción Invalida, Ingrese unicamente un código de sede.')
    return generarReporteSede(bD, sedeSelect)

def generarReporteSede(bD, sedeSelect):
     """
     Funcionamiento: Filtra y muestra por pantalla los estudiantes de una sede específica cuya nota 
     en cada uno de los tres parciales sea mayor o igual a 70.
    
     Entradas:
     - bD (list): Base de datos con la información de los estudiantes. Cada elemento es una lista con la forma:
       [nombre, apellido, carné, correo, (nota1, nota2, nota3, notaFinal, copiaFinal)].
     - sedeSelect (int): Código numérico de la sede que se desea analizar (extraído de las posiciones 4 y 5 del carné).
    
     Salidas:
     - Imprime en consola la información de los estudiantes con buen rendimiento de la sede seleccionada.
     """
     mejoresEstudiantesSede = []
     for estudiante in bD:
            sedeEstudiante = int(estudiante[2][4:6])
            if sedeEstudiante == sedeSelect:
                 notasEstudiante = estudiante[4][0:3]
                 for i in notasEstudiante:
                      if i >= 70:
                           bRendimiento = True #Si la nota detectada es mayor a 70, realizamos la siguiente iteración.
                           continue 
                      else:
                           bRendimiento = False #Si la nota detectada es menor a 70, terminamos el ciclo y devolvemos False.
                           break
            else:
                 continue
            if bRendimiento == True:
                 mejoresEstudiantesSede.append(estudiante)
            else:
                 continue
     for buenEst in mejoresEstudiantesSede:
          print(f'{buenEst[0]}, {buenEst[1]}, {buenEst[2]}, {buenEst[3]}, {buenEst[4]}. \n')
     return    

# --------------------------------------------------------------------------------------------------------- #