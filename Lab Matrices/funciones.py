#Elaborado por: Elías Lizano y Joshua Brenes
#Fecha de creación: 3/5/2025 9:00am.
#Última modificación: 3/5/2025 8:40pm.
#Versión de Python: 3.12.3
'''
FUNCIONES: En este archivo encontrara todas las funciones de procesamiento del programa.
'''
import re

def crearEdificio(p,a):
    """
    Funcionamiento: Crea una estructura de edificio con p pisos y a apartamentos por piso. Cada apartamento inicia desocupado.
    Entradas:
    - p (int): Cantidad de pisos
    - a (int): Cantidad de apartamentos por piso
    Salidas:
    - edificio (list): Estructura del edificio representada como una lista de listas
    """
    edificio = []
    for i in range(p):
        edificio.append([])
    for e in range(p):
        for o in range(a):
            edificio[e].append([0])
    return edificio


def nuevoAlquiler(pAlqui,aAlqui,ingreso,edificio):
    """
    Funcionamiento: Registra un nuevo alquiler en el apartamento especificado.
    Entradas:
    - pAlqui (int): Número de piso del apartamento
    - aAlqui (int): Número de apartamento
    - ingreso (int): Monto del alquiler a registrar
    - edificio (list): Estructura actual del edificio
    Salidas:
    - edificio (list): Estructura actualizada del edificio
    - mensaje (str): Confirmación del registro del alquiler
    """
    pAlqui -= 1
    aAlqui -= 1
    edificio[pAlqui][aAlqui] = ingreso
    return edificio, 'Se ha registrado el nuevo alquiler satisfactoriamente.' 

def modificarAlquiler(pAlqui,aAlqui,ingreso,edificio):
    """
    Funcionamiento: Modifica el monto de alquiler de un apartamento, validando que el nuevo monto sea distinto y solicitando confirmación.
    Entradas:
    - pAlqui (int): Número de piso del apartamento
    - aAlqui (int): Número de apartamento
    - ingreso (int): Nuevo monto del alquiler
    - edificio (list): Estructura actual del edificio
    Salidas:
    - edificio (list): Estructura actualizada del edificio (si se confirma el cambio)
    - mensaje (str): Resultado de la operación (confirmación o cancelación)
    """
    pAlqui -= 1
    aAlqui -= 1
    if ingreso == edificio[pAlqui][aAlqui]:
        return 'No se pudo modificar el alquiler pues el monto ingresado es igual al monto actual. '
    if ingreso > edificio[pAlqui][aAlqui]:
        estado = 'aumentar'
    if ingreso < edificio[pAlqui][aAlqui]:
        estado = 'disminuir'
    diferencia = ingreso - edificio[pAlqui][aAlqui]
    respuesta = input(str(f'El alquiler de su apartamento va a {estado} {diferencia}$, quiere confirmar la operación? \n'
    'De ser el caso, responda sí: '))
    if re.match('^(S|s)(i|I|í|Í|){2}', respuesta) is None:
          return 'Se cancelo la operación. '
    edificio[pAlqui][aAlqui] = ingreso
    return edificio, f'Se ha modificado el alquiler del apartamento {aAlqui+1} del piso {pAlqui+1}, el alquiler va a {estado} {diferencia}$'

def desalojar(pAlqui,aAlqui,edificio):
    """
    Funcionamiento: Desaloja el apartamento especificado, tras confirmar la operación con el usuario.
    Entradas:
    - pAlqui (int): Número de piso del apartamento
    - aAlqui (int): Número de apartamento
    - edificio (list): Estructura actual del edificio
    Salidas:
    - edificio (list): Estructura actualizada del edificio
    - mensaje (str): Resultado de la operación (confirmación o cancelación)
    """
    pAlqui -= 1
    aAlqui -= 1
    respuesta = input(str(f'El estado actual de su alquiler es {edificio[pAlqui][aAlqui]}, quiere confirmar la operación? \n'
    'De ser el caso, responda sí: '))
    if re.match('^(S|s)(i|I|í|Í|){2}', respuesta) is None:
          return 0, 'Se cancelo la operación. '
    edificio[pAlqui][aAlqui] = [0]
    return edificio, f'Se ha desalojado el alquiler del apartamento {aAlqui+1} del piso {pAlqui+1}.'

def porApartamento(pAlqui, aAlqui, edificio):
    """
    Funcionamiento: Devuelve el monto de alquiler de un apartamento específico.
    Entradas:
    - pAlqui (int): Número de piso
    - aAlqui (int): Número de apartamento
    - edificio (list): Estructura del edificio
    Salidas:
    - edificio (list): Estructura del edificio (sin cambios)
    - mensaje (str): Información del monto de alquiler del apartamento
    """
    pAlqui -= 1
    aAlqui -= 1
    return edificio, f'El ingreso del apartamento {aAlqui+1} del piso {pAlqui+1} es de {edificio[pAlqui][aAlqui]}$.'

def porPiso(pAlqui,edificio):
    """
    Funcionamiento: Imprime la información de todos los apartamentos de un piso y calcula el total de ingresos del mismo.
    Entradas:
    - pAlqui (int): Número de piso
    - edificio (list): Estructura del edificio
    Salidas:
    - edificio (list): Estructura del edificio (sin cambios)
    - mensaje (str): Total de ingresos del piso
    """
    pAlqui -= 1
    total = 0
    contador = 0
    for i in edificio[pAlqui]:
        if i == [0]:
            total += 0
            continue
        total += i
        contador += 1
        print(f'Piso {pAlqui+1}: \n'
              f'Apartamento {contador}: \n'
              f'Monto de alquiler {i}: \n'
              '')
    return edificio, f'Para un total de ingresos del piso {pAlqui+1} de {total}$.'

def porColumna(colum,edificio,p):
    """
    Funcionamiento: Imprime la información de todos los apartamentos en una columna específica y calcula el total de ingresos.
    Entradas:
    - colum (int): Número de columna (apartamento en la misma posición en cada piso)
    - edificio (list): Estructura del edificio
    - p (int): Cantidad de pisos
    Salidas:
    - edificio (list): Estructura del edificio (sin cambios)
    - mensaje (str): Total de ingresos de la columna
    """
    colum -= 1
    total = 0
    monto = 0
    contador = 0
    for i in edificio:
        monto = edificio[contador][colum]
        if monto == [0]:
            contador += 1
            continue
        total += monto 
        contador += 1
        print(f'Piso {contador}: \n'
              f'Apartamento {colum+1}: \n'
              f'Monto de alquiler {monto}$: \n'
              '')
    return edificio, f'Para un total de ingresos de la columna {colum+1} de {total}$.'

def totalEdificio(edificio):
    """
    Funcionamiento: Imprime la información de todos los apartamentos del edificio y calcula el total de ingresos.
    Entradas:
    - edificio (list): Estructura del edificio
    Salidas:
    - edificio (list): Estructura del edificio (sin cambios)
    - mensaje (str): Total de ingresos del edificio
    """
    total = 0
    monto = 0
    contador = 0
    contadorAux = 0
    for i in edificio:
        contadorAux = 0
        for e in edificio[contador]:
            monto = edificio[contador][contadorAux]
            if monto == [0]:
                contadorAux += 1
                continue
            total += monto 
            contadorAux += 1
            print(f'Piso {contador+1}: \n'
                f'Apartamento {contadorAux}: \n'
                f'Monto de alquiler {monto}$: \n'
                '')
        contador += 1
    return edificio, f'Para un total de ingresos totales del edificio de {total}$.'

def reporteTotal(edificio):
    """
    Funcionamiento: Calcula y muestra el total de apartamentos alquilados y desocupados, junto con sus porcentajes.
    Entradas:
    - edificio (list): Estructura del edificio
    Salidas:
    - mensaje (str): Reporte del estado general del edificio en términos de ocupación
    """
    totalAlquilados = 0
    totalDesocupados = 0
    contador = 0
    contadorAux = 0

    for i in edificio:
        #contador = 0
        for e in i:
            if e == [0]:
                totalDesocupados += 1
                continue 
            totalAlquilados += 1
            #contador += 1
    total = totalAlquilados + totalDesocupados
    return (f'Total de apartamentos alquilados: {totalAlquilados}, para un porcentaje de: {totalAlquilados/total*100}.\n'
          f'Total de apartamentos desocupados: {totalDesocupados}, para un porcentaje de: {totalDesocupados/total*100}.')
    
