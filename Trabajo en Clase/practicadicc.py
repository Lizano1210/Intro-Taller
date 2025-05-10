#
#
#
#

#Definición de variables globales.
autorizados = {'Juan': 17,'Mario': 21,'Oscar': 23,'Julia': 18}


def autorizadosConcierto():
    menores = 0
    mayores = 0
    puedenAsistir = []
    for i in autorizados:
        if autorizados[i] < 18:
            menores += 1
        else:
            mayores += 1
            puedenAsistir.append(i)
    if puedenAsistir == []:
        puedenAsistir = 'Ninguno.'
    print(f'Menores a 18 años: {menores}. \n'
          f'Mayores a 18 años: {mayores}. \n'
          f'Pueden asistir al concierto: \n'
          f'{puedenAsistir}')
    
autorizadosConcierto()
    

    
