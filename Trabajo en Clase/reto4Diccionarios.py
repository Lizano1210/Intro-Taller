# Elaborado por: Elías Lizano, Daniel Liao, Gabriel Pérez, Natalie Arias, Sara Funes
# Fecha de creación: 8/5/2025, 2:30p.m.
# Última modificación: 8/5/2025, 2:47p.m.
# Versión de Python: 3.12.3

# Se inicializan variables globales.
tupla1 = ('calor', 'ayer', 'el', 'mañana')
tupla2 = ('ayer hizo bastante calor', 'en el laboratorio hace calor')

def contarPalabrasAux(tupla1, tupla2):
    """
    Funcionamiento: Valida que las entradas sean tuplas y, si lo son, llama a la función principal 
    que realiza el conteo de palabras. Si alguna entrada no es una tupla, devuelve un mensaje de error.
    Entradas:
    - tupla1 (tuple): Tupla de palabras a buscar.
    - tupla2 (tuple): Tupla de frases donde se realizará la búsqueda.
    Salidas:
    - dict | str: Diccionario con las palabras de tupla1 como claves y su cantidad de apariciones en 
      las frases de tupla2 como valores, o un mensaje de error si las entradas no son válidas.
    """
    if type(tupla1) != tuple or type(tupla2) != tuple:
        return 'Ambos valores ingresados deben ser tuplas. '  
    return contarPalabras(tupla1, tupla2)


def contarPalabras(tupla1, tupla2):
    """
    Funcionamiento: Cuenta cuántas veces aparece cada palabra de la tupla1 dentro de las frases de 
    la tupla2. Solo se conservan las palabras que aparecen al menos una vez.
    Entradas:
    - tupla1 (tuple): Tupla de palabras a buscar.
    - tupla2 (tuple): Tupla de frases (str) donde se buscarán las palabras.
    Salidas:
    - dicc (dict): Diccionario con las palabras encontradas y su número de apariciones.
    """
    dicc = {}
    for i in tupla1:
        dicc[i] = 0
        for frase in tupla2:
            palabras = frase.split(' ')
            for palabra in palabras:
                if i == palabra:
                    dicc[i] += 1
    repetidos = []
    for key in dicc:
        if dicc[key] == 0:
            repetidos.append(key)
    for repetido in repetidos:
        del dicc[repetido]
    print(dicc)

# Programa principal
print(contarPalabrasAux(tupla1, tupla2))



            
