#
#
#
# Caldo de pollo
import BDdinamica
import reporteHTML
import respaldoXML
bD = []
annos = ()

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
        annos = bD[1]
        bD = bD[0]
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
    

#Programa principal    
menu(bD,annos)