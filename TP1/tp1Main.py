#
#
#
# 

'''
Tarea Programada 1, Main: Este es el documento principal de la tarea, el que se ejecuta para iniciar el programa.
Contiene principalmente, la función de menú.
'''
import BDdinamica
import reporteHTML
import respaldoXML
import gestCurva

# Definición de variables

bD = [] # Lista que futuramente contendra la base de datos dinamica con los estudiantes. 
annos = () # Tupla que contendra el rango de años dado por el usuario.

'''
Menú
'''
def menu(bD,annos):
    print('Administrados de propiedades. \nSeleccione una opción.\n' 
    '\n' 
    'Dígite la tecla indicada según cada opción. \n' 
    '1. Crear base de datos dínamica. \n' 
    #'2. Modificar renta. \n' 
    '3. Generar reporte de HTML. \n' 
    '4. Respaldar en XML. \n' 
    #'5. Reporte total del edificio. \n' 
    '6. Gestionar curva. \n' 
    '7. Salir. \n' 
    '')

    while True:
        opcion = int(input('Dígite una opción: '))
        if opcion in (1,2,3,4,5,6):
            break
        else:
            print('El dato ingresado es invalido, intente de nuevo.')

    if opcion == 1:
        bD = BDdinamica.bdDinamicaES()
        annos = bD[1] #Se optiene la tupla con el rango de años dado por el usuario.
        bD = bD[0] #bD se modifica para eliminar la tupla de años y que quede solamente la matriz con estudiantes.
        print(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu(bD,annos)
    
    if opcion == 3:
        reporteHTML.crearReporte(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu(bD,annos)
    
    if opcion == 4:
        respaldoXML.respaldoXML(bD,annos)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu(bD,annos)
    
    if opcion == 6:
        gestCurva.gestionCurva(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu(bD,annos)
    

#Programa principal    
menu(bD,annos)