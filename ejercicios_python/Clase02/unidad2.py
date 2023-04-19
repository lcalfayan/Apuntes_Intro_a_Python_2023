# Clase 2
import os
os.getcwd()
#'/home/datascience/Documentos/Ejercicios/ejercicios_python/Clase02'
os.chdir('/home/datascience/Documentos/Ejercicios/ejercicios_python/Clase02')


#Ejercicio 2.1: Preliminares sobre lectura de archivos

#abrir un archivo csv en formato solo lectura (rt)
with open('camion.csv', 'rt') as f:
        data = f.read()

data
print(data)

#para leer un erchivo linea por linea
#%%
with open('camion.csv', 'rt') as f:
    for line in f:
        print(line, end = '')
#%%

#leer una sola linea de texto (y saltear la primera linea):
f = open('camion.csv', 'rt')
headers = next(f)
headers
#'nombre,cajones,precio\n'
for line in f:
    print(line, end = '')
    
f.close()   

f = open('camion.csv', 'rt')
headers = next(f).split(',')
headers
#['nombre', 'cajones', 'precio\n']
for line in f:
    row = line.split(',')
    print(row)

f.close() 

#Ejericio 2.3: Precio de la naranja
f = open('../Data/precios.csv', 'rt')

for line in f:
    if 'Naranja' in line: 
        row = line.split(',')
        precio = row[1]
        print('El precio de la naranja es:',precio )
f.close()

#Ejercicio 2.4: Archivos comprimidos
import gzip
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')

#%%
# 2.4 FUNCIONES

def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

sumcount(3)
sumcount(20)
1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20

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

# Ejercicio 2.5: Definir una función

def saludar(nombre):
    'Saluda a alguien'
    print('Hola', nombre)

saludar('Juan')
help(saludar)

# Ejercicio 2.6: Transformar un script en una función
##en el archivo costo_camion.py

# Ejercicio 2.7: Buscar precios
## en el archivo buscar_precios.py
