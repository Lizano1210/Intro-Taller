#
#
#
#
import BDdinamica
import reporteHTML
bD = []

'''
Menú
'''
def menu(bD):
    print('Administrados de propiedades. \nSeleccione una opción.\n' 
    '\n' 
    'Dígite la tecla indicada según cada opción. \n' 
    '1. Crear base de datos dínamica. \n' 
    #'2. Modificar renta. \n' 
    '3. Generar reporte de HTML. \n' 
    #'4. Indicar ingreso por alquiler. \n' 
    #'5. Reporte total del edificio. \n' 
    '6. Salir. \n' 
    '')

    while True:
        opcion = int(input('Dígite una opción: '))
        if opcion in (1,2,3,4,5,6):
            break
        else:
            print('El dato ingresado es invalido, intente de nuevo.')

    if opcion == 1:
        bD = BDdinamica.bdDinamicaES()
        print(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu(bD)
    
    if opcion == 3:
        reporteHTML.crearReporte(bD)
        print('') # Espacio utilizado para separar el resultado de el menu desplegandose nuevamente solo porque se ve bonito :)
        return menu(bD)
    

#Programa principal    
menu(bD)