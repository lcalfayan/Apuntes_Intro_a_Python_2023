# Atrapar y administrar excepciones


numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')


## para atrapar cuando hacen control+c
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:                                     #atrapa todos los errores                                      
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

raise RuntimeError('¡Qué moco!')
