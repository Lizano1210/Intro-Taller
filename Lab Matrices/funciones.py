#Elaborado por: Elías Lizano y Joshua Brenes
#Fecha de creación: 3/5/2025 9:00am.
#Última modificación: 3/5/2025 8:40pm.
#Versión de Python: 3.12.3
import re

def crearEdificio(p,a):
    edificio = []
    for i in range(p):
        edificio.append([])
    for e in range(p):
        for o in range(a):
            edificio[e].append([0])
    return edificio


def nuevoAlquiler(pAlqui,aAlqui,ingreso,edificio):
    pAlqui -= 1
    aAlqui -= 1
    edificio[pAlqui][aAlqui] = ingreso
    return edificio, 'Se ha registrado el nuevo alquiler satisfactoriamente.' 

def modificarAlquiler(pAlqui,aAlqui,ingreso,edificio):
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
    pAlqui -= 1
    aAlqui -= 1
    respuesta = input(str(f'El estado actual de su alquiler es {edificio[pAlqui][aAlqui]}, quiere confirmar la operación? \n'
    'De ser el caso, responda sí: '))
    if re.match('^(S|s)(i|I|í|Í|){2}', respuesta) is None:
          return 0, 'Se cancelo la operación. '
    edificio[pAlqui][aAlqui] = [0]
    return edificio, f'Se ha desalojado el alquiler del apartamento {aAlqui+1} del piso {pAlqui+1}.'

def porApartamento(pAlqui, aAlqui, edificio):
    pAlqui -= 1
    aAlqui -= 1
    return edificio, f'El ingreso del apartamento {aAlqui+1} del piso {pAlqui+1} es de {edificio[pAlqui][aAlqui]}$.'

def porPiso(pAlqui,edificio):
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
    
