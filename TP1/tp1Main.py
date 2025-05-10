# Elaborado por: Elías Lizano y Joshua Brenes
# Fecha de creación: 22/4/2025 7:00p.m
# Última modificación: 9/52025 11:00p.m
# Versión de python: 3.12.3

'''
Tarea Programada 1, Main: Este es el documento principal de la tarea, el que se ejecuta para iniciar el programa.
Contiene principalmente, la función de menú.
'''

# Importación de librerias/modulos
import funciones
import pickle

'''
Menú
'''
def menu():
    print('Tarea programada 1, Base de datos de estudiantes. \nSeleccione una opción.\n' 
    '\n' 
    'Dígite la tecla indicada según cada opción. \n' 
    '1. Crear base de datos dínamica. \n' 
    '2. Registrar un estudiante. \n' 
    '3. Generar reporte de HTML. \n' 
    '4. Respaldar en XML. \n' 
    '5. Reporte por género. \n' 
    '6. Gestionar curva. \n' 
    '7. Envió de correos de reposición. \n'
    '8. Aplazados en al menos 2 rubros. \n'
    '9. Estadistica por generación. \n'
    '10. Reporte por sede por buen rendimiento. \n'
    '11. Salir. \n' 
    '')

    while True:
        try: #Ciclo que obliga al usuario a ingresar una opción valida.
            opcion = int(input('Dígite una opción: '))
            if opcion in (1,2,3,4,5,6,7,8,9,10,11):
                break
            else:
                print('El dato ingresado es invalido, intente de nuevo.')
        except ValueError:
            print('El dato ingresado es invalido, ingrese unicamente números enteros.')

    if opcion == 1:
        funciones.bdDinamicaES()
        with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
        #print(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 2:
        funciones.registrarEstudianteES()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 3:
        funciones.crearReporte()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 4:
        funciones.respaldoXML()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 5:
        funciones.determinarGeneroyOrdenar()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 6:
        funciones.gestionCurva()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 7:
        print(funciones.determinarReposicion())
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 8:
        funciones.determinarAplazados()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 9:
        funciones.estadisticaGeneracion()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 10:
        funciones.determinarSede()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 11:
        print('Gracias por utilizar nuestro servicio.')
        input()
        exit()
    

#Programa principal    
menu()