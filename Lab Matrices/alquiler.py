#Elaborado por: Elías Lizano y Joshua Brenes
#Fecha de creación: 3/5/2025 9:00am.
#Última modificación: 3/5/2025 8:40pm.
#Versión de Python: 3.12.3
'''
ALQUILER: En este archivo encontrará todas las funciones E/S y Auxiliares del programa.
'''
import funciones 
import re 

def crearEdificioES():
    """
    Funcionamiento: Solicita al usuario la cantidad de pisos y apartamentos, valida los datos y crea la estructura inicial del edificio.
    Entradas:
    - Ninguna (los datos se solicitan mediante input).
    Salidas:
    - None (se llama al menú principal con los datos creados).
    """
    while True:
        try:
            p = int(input('Ingrese la cantidad de pisos de su edificio: '))
            a = int(input('Ingrese la cantidad de apartamentos por piso de su edificio: '))
            if p <= 0 or a <= 0:
                print('Los datos ingresados deben ser mayores a 0.') 
            else:
                break
        except ValueError:
            print('El dato ingresado no es válido, intentelo de nuevo.')
    edificio = funciones.crearEdificio(p,a)
    edificioAux = funciones.crearEdificio(p,a)
    return menu(edificio, p, a,edificioAux)

def alquilarApartamentoES(p,a,edificio):
    """
    Funcionamiento: Permite registrar un nuevo alquiler en un apartamento disponible, validando que esté desocupado y que el ingreso sea válido.
    Entradas:
    - p (int): Cantidad de pisos del edificio.
    - a (int): Cantidad de apartamentos por piso.
    - edificio (list): Matriz que representa el estado actual del edificio.
    Salidas:
    - mensaje (str): Confirmación del alquiler o mensaje de error.
    """
    for u in range(p):
        print(f'Piso {u+1}    {edificio[u]}')
    print('')
    print('Ingrese su nuevo alquiler en un espacio desalojado: ')
    while True:
        try:
            pAlqui = int(input('Ingrese el piso en el que se encuentre el nuevo alquiler: '))
            aAlqui = int(input('Ingrese el apartamento: '))
            if pAlqui > p or aAlqui > a:
                print('EL apartamento ingresado no existe. ')
                continue 
            if edificio[(pAlqui-1)][(aAlqui-1)] != [0]:
                print('No puede registrar un alquiler en un espacio ya existente.')
                continue
            break
        except ValueError:
            print('El dato ingresado no es válido, intentelo de nuevo.')
    while True:
        try:
            ingreso = int(input('Ingrese el ingreso de el nuevo alquiler: '))
            if ingreso <= 0:
                print('El ingreso debe ser mayor a 0')
                continue
            break
        except ValueError:
            print('El dato ingresado no es válido, intentelo de nuevo.')
    salida = funciones.nuevoAlquiler(pAlqui,aAlqui,ingreso,edificio)
    return salida[1]
    
def modificarRentaES(edificio,edificioAux,p,a):
    """
    Funcionamiento: Permite modificar la renta de un apartamento ya alquilado, validando que no esté vacío.
    Entradas:
    - edificio (list): Matriz actual del edificio.
    - edificioAux (list): Copia vacía del edificio usada para comparar.
    - p (int): Cantidad de pisos.
    - a (int): Cantidad de apartamentos por piso.
    Salidas:
    - mensaje (str): Confirmación de modificación o mensaje de error.
    """
    if edificio == edificioAux:
        return'El edificio esta vacío, no hay alquileres que modificar. '
    for u in range(p):
        print(f'Piso {u+1}    {edificio[u]}')
    print('')
    print('Seleccione el alquiler a modificar:')
    while True:
        try:
            pAlqui = int(input('Ingrese el piso en el que se encuentre el alquiler: '))
            aAlqui = int(input('Ingrese el apartamento: '))
            if pAlqui > p or aAlqui > a:
                print('EL apartamento ingresado no existe. ')
                continue 
            if edificio[(pAlqui-1)][(aAlqui-1)] == [0]:
                print('El apartamento actualmente esta desalojado, no se puede modificar su alquiler. ')
                continue
            break
        except ValueError:
            print('El dato ingresado no es válido, intentelo de nuevo.')
    while True:
        try:
            ingreso = int(input('Ingrese el nuevo monto del alquiler: '))
            if ingreso <= 0:
                print('El nuevo monto debe ser mayor a 0')
                continue
            break
        except ValueError:
            print('El dato ingresado no es válido, intentelo de nuevo.')
    salida = funciones.modificarAlquiler(pAlqui,aAlqui,ingreso,edificio)
    return salida[1]
    
def desalojarES(edificio,edificioAux,p,a):
    """
    Funcionamiento: Permite desalojar un apartamento, validando que esté ocupado.
    Entradas:
    - edificio (list): Matriz actual del edificio.
    - edificioAux (list): Copia vacía del edificio usada para comparar.
    - p (int): Cantidad de pisos.
    - a (int): Cantidad de apartamentos por piso.
    Salidas:
    - mensaje (str): Confirmación del desalojo o mensaje de error.
    """
    if edificio == edificioAux:
        return'El edificio esta vacío, no hay alquileres que desalojar. '
    for u in range(p):
        print(f'Piso {u+1}    {edificio[u]}')
    print('')
    print('Seleccione el alquiler a desalojar:')
    while True:
        try:
            pAlqui = int(input('Ingrese el piso en el que se encuentre el alquiler: '))
            aAlqui = int(input('Ingrese el apartamento: '))
            if pAlqui > p or aAlqui > a:
                print('EL apartamento ingresado no existe. ')
                continue 
            if edificio[(pAlqui-1)][(aAlqui-1)] == [0]:
                print('El apartamento actualmente esta desalojado, no se puede desalojar. ')
                continue
            break
        except ValueError:
            print('El dato ingresado no es válido, intentelo de nuevo.')
    salida = funciones.desalojar(pAlqui,aAlqui,edificio)
    return salida [1]

def ingresoxAlquilerES(edificio, edificioAux, p, a):
    """
    Funcionamiento: Calcula el ingreso por alquiler según la opción del usuario (por apartamento, piso, columna o total).
    Entradas:
    - edificio (list): Matriz actual del edificio.
    - edificioAux (list): Copia vacía del edificio usada para validar estado.
    - p (int): Cantidad de pisos.
    - a (int): Cantidad de apartamentos por piso.
    Salidas:
    - ingreso (str): Valor calculado o mensaje de advertencia.
    """
    print('Ingreso por alquiler. \nSeleccione una opción.\n' 
    '\n' 
    'Dígite la tecla indicada según cada opción. \n' 
    '1. Por apartamento. \n' 
    '2. Por piso. \n' 
    '3. Por columna. \n' 
    '4. Por totalidad del edificio. \n'  
    '')

    while True:
        opcion = int(input('Dígite una opción: '))
        if opcion in (1,2,3,4):
            break
        else:
            print('El dato ingresado es invalido, intente de nuevo.')

    if opcion == 1:
        if edificio == edificioAux:
            return 'El edificio esta vacío, no hay alquileres que reportar. '
        for u in range(p):
            print(f'Piso {u+1}    {edificio[u]}')
        print('')
        print('Seleccione el alquiler a reportar:')
        while True:
            try:
                pAlqui = int(input('Ingrese el piso en el que se encuentre el alquiler: '))
                aAlqui = int(input('Ingrese el apartamento: '))
                if pAlqui > p or aAlqui > a:
                    print('EL apartamento ingresado no existe. ')
                    continue 
                if edificio[(pAlqui-1)][(aAlqui-1)] == [0]:
                    print('El apartamento actualmente esta desalojado, no hay un alquiler para reportar. ')
                    continue
                break
            except ValueError:
                print('El dato ingresado no es válido, intentelo de nuevo.')
        salida = funciones.porApartamento(pAlqui, aAlqui, edificio)
        return salida[1]
    
    if opcion == 2:
        if edificio == edificioAux:
            return 'El edificio esta vacío, no hay alquileres que reportar. '
        for u in range(p):
            print(f'Piso {u+1}    {edificio[u]}')
        print('')
        print('Seleccione el piso a reportar:')
        while True:
            try:
                pAlqui = int(input('Ingrese el piso del cual quiere generar un reporte: '))
                if pAlqui > p:
                    print('El piso ingresado no existe. ')
                    continue 
                if edificio[(pAlqui-1)] == edificioAux[(pAlqui-1)]:
                    print('El apartamento actualmente esta desalojado, no hay un alquiler para reportar. ')
                    continue
                break
            except ValueError:
                print('El dato ingresado no es válido, intentelo de nuevo.')
        salida = funciones.porPiso(pAlqui, edificio)
        return salida[1]
    
    if opcion == 3:
        if edificio == edificioAux:
            return 'El edificio esta vacío, no hay alquileres que reportar. '
        for u in range(p):
            print(f'Piso {u+1}    {edificio[u]}')
        print('')
        print('Seleccione la columna a reportar:')
        while True:
            try:
                colum = int(input('Ingrese la columna de la cual quiere generar un reporte: '))
                if colum > a:
                    print('La columna ingresada no existe. ')
                    continue 
                if edificio[(colum-1)] == edificioAux[(colum-1)]:
                    print('El apartamento actualmente esta desalojado, no hay un alquiler para reportar. ')
                    continue
                break
            except ValueError:
                print('El dato ingresado no es válido, intentelo de nuevo.')
        salida = funciones.porColumna(colum,edificio,p)
        return salida[1]
    
    if opcion == 4:
        salida = funciones.totalEdificio(edificio)
        return salida[1]
    
def reporteTotalES(edificio, edificioAux):
    """
    Funcionamiento: Genera un reporte con todos los apartamentos alquilados y sus ingresos si el edificio no está vacío.
    Entradas:
    - edificio (list): Matriz actual del edificio.
    - edificioAux (list): Copia vacía del edificio usada para validar estado.
    Salidas:
    - reporte (str): Información completa del estado del edificio o advertencia si está vacío.
    """
    if edificio == edificioAux:
        return'El edificio esta vacío, no se puede generar un reporte. '
    salida = funciones.reporteTotal(edificio)
    return salida



'''
Menú
'''
def menu(edificio, p, a,edificioAux):
    """
    Funcionamiento: Muestra el menú principal y ejecuta la opción elegida por el usuario hasta que este decida salir.
    Entradas:
    - edificio (list): Matriz actual del edificio.
    - p (int): Cantidad de pisos.
    - a (int): Cantidad de apartamentos por piso.
    - edificioAux (list): Copia vacía del edificio usada para validaciones.
    Salidas:
    - None (flujo controlado internamente).
    """
    print('Administrados de propiedades. \nSeleccione una opción.\n' 
    '\n' 
    'Dígite la tecla indicada según cada opción. \n' 
    '1. Alquilar apartamento. \n' 
    '2. Modificar renta. \n' 
    '3. Desalojar. \n' 
    '4. Indicar ingreso por alquiler. \n' 
    '5. Reporte total del edificio. \n' 
    '6. Salir. \n' 
    '')

    while True:
        opcion = int(input('Dígite una opción: '))
        if opcion in (1,2,3,4,5,6):
            break
        else:
            print('El dato ingresado es invalido, intente de nuevo.')

    if opcion == 1:
        print(alquilarApartamentoES(p,a,edificio))
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu(edificio, p, a,edificioAux)
    if opcion == 2:
        print(modificarRentaES(edificio,edificioAux,p,a))
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu(edificio, p, a,edificioAux)
    if opcion == 3:
        print(desalojarES(edificio,edificioAux,p,a))
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu(edificio, p, a,edificioAux)
    if opcion == 4:
        print(ingresoxAlquilerES(edificio, edificioAux, p, a))
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu(edificio, p, a,edificioAux)
    if opcion == 5:
        print(reporteTotalES(edificio, edificioAux))
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu(edificio, p, a,edificioAux)
    
    if opcion == 6:
        print('Gracias por utilizar nuestro servicio.')
        input()
        exit()

# Programa Principal
crearEdificioES()
