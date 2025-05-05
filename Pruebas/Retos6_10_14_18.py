
"""
Elaborado por: Moisés López, Joshua Brenes, Elías Lizano, Thanisha Chaves, Patrick Gätjens 
Hora de inicio: 8/4/2025 1:12p.m.
Última Edición: 8/4/2025 3:51p.m.
"""

def acumularSuma(L1):
    SUMA=0
    for i in range(0,len(L1)):
        SUMA+=L1[i]
        L1[i]=SUMA
        i=i+1
    print(L1)
    return
#Reto----------------------------10
def contarRepeticionesL(L1,L2):
    conta=0
    for a in L1:
        if a==L2[0]:
            conta += 1
        
    if conta==0:
        print("No se encuentra")
    else:
        print(conta)
    return

# Reto 14 

def eliminarDuplicado(lista):
    listaAux = []
    
    for i in lista:
        if str(i) not in listaAux:
            listaAux += str(i)
        
    return listaAux
        
# Reto 18

def eliminarEspacios(frase):
    listaAux = []
    fraseAux = ""
    contador = 0
    
    for i in range(len(frase)):
        if frase[i] != " ":
            fraseAux += frase[i]
        else:
            contador +=1
            
    listaAux += [fraseAux]
    listaAux += [contador]
    
    return listaAux


#Programa Principal
print("Reto 6")
l1=[1,2,3]
acumularSuma(l1)
l1=[1,4,8,2]
acumularSuma(l1)
print("Reto 10")
l1=[8,0,6,5,0,3]
l2=[4]
contarRepeticionesL(l1,l2)
l1=[8,2,6,8,4]
l2=[8]
contarRepeticionesL(l1,l2)
l1=[2,3,4,5,7]
l2=[5]
contarRepeticionesL(l1,l2)
print("Reto 14")
print(eliminarDuplicado([1,2,3,2,5]))
print(eliminarDuplicado(["a","b","c"]))
print(eliminarDuplicado([1,2,3,2,5,3,4,3]))
print("Reto 18")
print(eliminarEspacios("Hoy es un buen día para ser feliz."))
