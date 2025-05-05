###############################################################
#Elaborado por: Patrick Gatjens Gomez y Thanisha chaves solera#
#Fecha de creación: 19/04/2025 06:55 p.m.                     #
#Ultima modificación: 20/04/2025 11:00 p.m.                   #
#Versión de Python: 3.13.2                                    #
###############################################################
#Librerias importadas:
import names
import random
import math
import pickle #aun no se para que se usa (investigalo)
""" 
Que falta?
-hacer la parte que genera carnet, correo, y notas, con sus respectivas caracteristicas
-revisar por olores de software
-buscar como se puede optimizar aun mas el codigo
-modificiar la funcion solicitarDatos() para que tanto el porcentaje como el numero para la fuente 1, salgan por igual
"""
##########
#fuente 1#
##########

def generadorDeNombres(cantidad):
    """
    Funcionamiento:
    Entradas:
    Salidas:
    """
    #archivo = open('Lista de prueba.txt','w') #estas tres lineas de codigo que dicen archivo, es por si uno ddesea que la lista se guarde en uno, solo hay que quitarles el #
    estudiantesF1 = [] #esta pequeña lista (por ahora pequeña) sera donde iremos insertando los nombres generados de los estudiantes, asi convirtiendola en una matriz
    for i in range(cantidad):
        monedaHF = random.choice([True, False])#con un randomizador entre true(hombre) false(mujer) decida en una chance de 50/50 que sale
        if monedaHF == True:
            #nombre = names.get_full_name(gender='male') #esto no funciona porque en un par de pruebas, me salieron nombre sin dos apellidos, entonces, aqui SOLO se debe generar el nombre, y luego generar los dos apellidos, con un ciclo que se encargue de que no salgan iguales, a no ser que queramos estudiantes nacidos del incesto
            nombre = names.get_first_name(gender='male')
        else:
            nombre = names.get_first_name(gender='Female')
        apellido1 = names.get_last_name() #con estas dos variables de apellidos aseguramos al 100% que lo que salgan sean 2 apellidos, porque con "get_full_name" existia la posibilidad de uno solo 
        apellido2 = names.get_last_name()
        while apellido1 == apellido2: #este es el ciclo que se encarga de evitar la pulga mencionada anteriormente, asi evitamos que los apellidos salgan repetidos
            apellido2 = names.get_last_name()
        nombreCompleto = [(nombre, apellido1, apellido2), monedaHF] #esto tambien funcionaria si se hiciera con: "nombreCompleto = [(nombre, apellido1, apellido2), genero == "Hombre"]" pero, no es correcto, porque cuando genera la lista, salen con los generos erroneos, por eso se debe asignar la 'monedaHF' a una variable, porque ahi si esta guardado el genero
        estudiantesF1.append(nombreCompleto) #lo añade a la lista de nombres que creamos al inicio      
        #archivo.write(nombreCompleto)
    #archivo.close()
    print(f'se genero {cantidad} estudiantes') #este print es para avisar en la Terminal que si funciono y el archivo se creo, por si no aparece en la carpeta que deberia, al menos saber que si se creo
    #HAZ UNA VARIABLES QUE LEA LA MATRIZ Y TE DIGA CUANTOS EN REALIDAD SE GENERARON
    print(estudiantesF1) #esto es temporal, es para ver si los nombres si se crean, y se ven en la terminal
    return estudiantesF1

##########
#fuente 2#
##########

def leerArchivo(porcentaje):
    """
    Funcionamiento:
    Entradas:
    Salidas:
    """
    archivo = open('estudiantes.txt', 'r')
    contenido = archivo.readlines()
    archivo.close()
    nombres = len(contenido) #len en este caso lee linea por linea el documento, entonces se puede decir que lee cuantos estudiantes hay
    cantidad = math.ceil(porcentaje / nombres) #una vez len leyo los nombres, le aplica el porcentaje a los mismos
    estudiantesF2 = [] #es donde se almacenan los nombres de la Fuente 2 (o sea esta funcion, valga la redondancia)
    nombresElegidos = random.sample(contenido, cantidad) ##### creo que aqui puede estar uno de los errores
    for linea in nombresElegidos:
        linea = linea.strip() #esto se coloca para que a la hora de imprimir la lista con los nombres, no salga el \n ###########revisa si strip se puede usar#################
        nombre, apellido1, apellido2, genero = linea.split(',') #lo que hace esta linea es separar todo con comas luego de quitar los espacios
        estudiantesF2.append([(nombre, apellido1, apellido2), genero])
    print(estudiantesF2) #esto es temporal
    return estudiantesF2

def solicitarDatos(): #Falta colocar la variable del porcentaje de los nombres que desea, y si no, en tal caso, hacer un randomizador, entre el 1 y el 100, y el resutado dividirlo entre 100, algo asi: ''porcentaje = random.randint(1, 100)'' y ese resultado, multiplicarlo por "cantidadX"
    """
    Funcionamiento:
    Entradas:
    Salidas:
    """
    cantidadX = int(input('ingrese la cantidad de estudiantes de la cual desea la lista: '))
    porcentaje = int(input('ingrese el porcentaje que desea aplicar a la cantidad: '))
    porcentaje = porcentaje / 100 #se pasa el pocentaje a decimal para que la multiplicacion funcione
    cantidad = int(cantidadX * porcentaje) #esto esta bien, pero el redondeo no lo hace para arriba, para eso uso la siguiente linea en ves de esta
    cantidad = math.ceil(cantidadX * porcentaje) #el .ceil lo que hace es asegurarse que el redondeo sea positivo, y si no, de todas formas el "cantidad = int(cantidadX * porcentaje)" hace lo mismo, solo que esto se encarga de hacerlo con mas exactitud
    print(f'Cantidad calculada de estudiantes: {cantidad}') #esto es para verificar que el porcentaje este bien #temporal
    estudiantesGenerados = generadorDeNombres(cantidad) #estas dos variables las hago para que al llamarlas en return, se llamen bien, intente usar un and, pero no funcionaba y se me ocurrio hacerlo por variables en las que de una vez, tienen los parametros y todo / esta variable llama al generador de nombres
    estudiantesLeidos = leerArchivo(porcentaje)  # Lee los estudiantes desde el archivo
    return estudiantesGenerados, estudiantesLeidos #aqui estan las variables que mencione antes
solicitarDatos() #esto es para hacer las pruebas, pero en realidad esta parte va en el menu el cual se hara mas adelante,

    
######################
    
     #menu de BD
     
######################
   