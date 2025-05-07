#
#
#
# 

'''
Tarea Programada 1, Main: Este es el documento principal de la tarea, el que se ejecuta para iniciar el programa.
Contiene principalmente, la función de menú.
'''

# Importación de librerias/modulos
import BDdinamica
import registrarEstudiante
import reporteHTML
import respaldoXML
import gestCurva
#import apalazados2
import pickle

# Definición de variables


'''
Menú
'''
def menu():
    print('Administrados de propiedades. \nSeleccione una opción.\n' 
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

    while True: #Ciclo que obliga al usuario a ingresar una opción valida.
        opcion = int(input('Dígite una opción: '))
        if opcion in (1,2,3,4,5,6,7,8,9,10,11):
            break
        else:
            print('El dato ingresado es invalido, intente de nuevo.')

    if opcion == 1:
        BDdinamica.bdDinamicaES()
        with open('baseDatosDinamica.pkl', 'rb') as archivobD:
            bD = pickle.load(archivobD)
        print(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 2:
        registrarEstudiante.registrarEstudianteES()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 3:
        reporteHTML.crearReporte()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 4:
        respaldoXML.respaldoXML()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 6:
        gestCurva.gestionCurva()
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 8:
        #apalazados2.determinarAplazados2oMas(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu()
    
    if opcion == 11:
        print('Gracias por utilizar nuestro servicio.')
        input()
        exit()
    

#Programa principal    
menu()