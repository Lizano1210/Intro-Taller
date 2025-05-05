#Elaborado por: Elías Lizano y Joshua Brenes
#Fecha de creación: 1/5/2025 7:30am.
#Última modificación: 1/5/2025 8:40pm.
#Versión de Python: 3.12.3
'''
LISTAS: En este documento encontrará todas las funciones de E/S, Auxiliares y menú del programa.
'''
import funciones
import re

def nuevoDonanteES():
    """
    Funcionamiento: Solicita y valida la cédula de 4 nuevos donantes, agregándolos a la lista si son válidos.
    Entradas:
    - Ninguna entrada directa (input dentro de la función)
    Salidas:
    - resultado (str): Mensaje de confirmación de registro exitoso
    """
    for i in range(4):
        while True:
            nD = input(str('Por favor ingrese su número de cédula: '))
            salida = funciones.nuevoDonante(nD)
            if salida == True:
                funciones.recuperadosDonantes.append(nD)
                break
            else:
                print(salida)
                print('Por favor ingrese el dato nuevamente.')
    return 'Donantes registrados satisfactoriamente. '     

def decodificarDonadorES():
    while True:
            entrada = input(str('Por favor ingrese su número de cédula: '))
            salida = funciones.nuevoDonante(entrada)
            if salida == True or salida == 'No puede ingresar un donante ya existente.':
                break
            else:
                print(salida)
                print('Por favor ingrese el dato nuevamente.')
    resultado = funciones.decodificarDonador(entrada)
    return resultado 


def listaRNES():
    """
    Funcionamiento: Muestra una lista de provincias para que el usuario seleccione una y despliega los donantes correspondientes.
    Entradas:
    - Ninguna entrada directa (input dentro de la función)
    Salidas:
    - resultado (str): Información de donadores según la provincia seleccionada
    """
    print('Código   /   Provincia\n' 
    '1            San José\n' 
    '2            Alajuela\n' 
    '3            Cartago\n' 
    '4            Heredia\n' 
    '5            Guanacaste\n' 
    '6            Puntarenas\n' 
    '7            Limón\n' 
    '8            Nacionalizado o naturalizado\n' 
    '9            Partida especial de nacimientos\n' 
    '')
    while True:
        oplistaRN = int(input('Dígite una opción: '))
        if oplistaRN in (1,2,3,4,5,6,7,8,9):
            break
        else:
            print('El dato ingresado es invalido, intente de nuevo.')
    salidaListaRN = funciones.listaRN(oplistaRN)
    if salidaListaRN[1] == 0:
        return 'Aún no hay donadores de esa naturalización. '
    if oplistaRN in (8,9):
        return (f'Los donadores {salidaListaRN[2]}, son {salidaListaRN[1]} con las cédulas: \n'
                f'{salidaListaRN[0]}')

    return (f'Los donadores de la provincia {salidaListaRN[2]}, son {salidaListaRN[1]} con las cédulas: \n'
          f'{salidaListaRN[0]}')

def donadoresTotalesES():
    """
    Funcionamiento: Recorre todas las provincias y muestra los donantes registrados en cada una.
    Entradas:
    - Ninguna entrada directa (uso interno de rango)
    Salidas:
    - Imprime directamente los resultados
    """
    for i in range(1,10):
        salidaListaRN = funciones.listaRN(i)
        if salidaListaRN[1] == 0:
            print(f'{salidaListaRN[2]} aún no reporta donadores. ')
            continue
        if i in (8,9):
            print(f'Los donadores {salidaListaRN[2]}, son {salidaListaRN[1]} con las cédulas: \n'
                f'{salidaListaRN[0]}')
            continue
        print(f'Los donadores de la provincia {salidaListaRN[2]}, son {salidaListaRN[1]} con las cédulas: \n'
          f'{salidaListaRN[0]}')
    return

def donadoresAtipicosES():
    """
    Funcionamiento: Muestra los donadores con cédula 8 y 9.
    Entradas:
    - Ninguna entrada directa (uso interno de rango)
    Salidas:
    - Imprime directamente los resultados
    """
    for i in range(8,10):
        salidaListaRN = funciones.listaRN(i)
        if salidaListaRN[1] == 0:
            print(f'{salidaListaRN[2]} aún no reporta donadores. ')
            continue
        print(f'Los donadores {salidaListaRN[2]}, son {salidaListaRN[1]} con las cédulas: \n'
            f'{salidaListaRN[0]}')
    return
            



'''
Menú
'''
def menu():
    print('¡Suero Convaleciente!, Menú de donadores.\n' 
    '\n' 
    'Dígite la tecla indicada según cada opción. \n' 
    '1. Agregar nuevos donantes. \n' 
    '2. Decodificar donante. \n' 
    '3. Donadores según registro de naturalizaciones. \n' 
    '4. Donadores totales del país. \n' 
    '5. Donadores no típicos. \n' 
    '6. Salir. \n' 
    '')

    while True:
        opcion = int(input('Dígite una opción: '))
        if opcion in (1,2,3,4,5,6):
            break
        else:
            print('El dato ingresado es invalido, intente de nuevo.')

    if opcion == 1:
        print(nuevoDonanteES())
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu()

    if opcion == 2:
        print(decodificarDonadorES())
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu()

    if opcion == 3:
        print(listaRNES())
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu()

    if opcion == 4:
        donadoresTotalesES()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu()

    if opcion == 5:
        donadoresAtipicosES()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        menu()

    if opcion == 6:
        print('Gracias por donar su sangre, ahora fuiste tú, luego espero poder ser yo.')
        input()
        exit()

#Programa Principal
menu()