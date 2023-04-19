#Ejercicio 2.2: Lectura de un archivo de datos

f = open('camion.csv', 'rt')
headers = next(f).split(',') #le saco los encabezados a f

costo_total = 0

for line in f:
    row = line.split(',')
    cantidad = int(row[1])
    costo = float(row[2])
    costo_total += cantidad*costo
print('El costo total es:', costo_total)

f.close() 
