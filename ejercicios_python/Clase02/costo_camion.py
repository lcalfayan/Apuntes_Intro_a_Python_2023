#Ejercicio 2.2: Lectura de un archivo de datos

#%%
f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',') #le saco los encabezados a f

costo_total = 0

for line in f:
    row = line.split(',')
    cantidad = int(row[1])
    costo = float(row[2])
    costo_total += cantidad*costo
print('El costo total es:', costo_total)

f.close() 

#%%
#Ejercicio 2.6: Transformar un script en una función
def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    headers = next(f).split(',') #le saco los encabezados a f

    costo_total = 0

    for line in f:
        row = line.split(',')
        cantidad = int(row[1])
        costo = float(row[2])
        costo_total += cantidad*costo
    return(costo_total)
    f.close()


costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
