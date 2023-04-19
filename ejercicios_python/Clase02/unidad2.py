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

