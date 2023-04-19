# Ejercicio 2.7: Buscar precios

def buscar_precio(fruta):
    with open('../Data/precios.csv', 'rt') as f:
        precio = 0.0
        for line in f:
            row = line.split(',')
            if fruta in line: 
                costo = float(row[1])
                precio += costo    
        print(f'El precio de {fruta} es {precio}')
        
buscar_precio("Naranja")
buscar_precio("Uva")
buscar_precio("Kiwi")

######################################


def buscar_precio(fruta):
    with open('../Data/precios.csv', 'rt') as f:
        precio = 0.0
        for line in f:
            row = line.split(',')
            nombre = row[0]
            if nombre == fruta: 
                precio = float(row[1])
        return precio

# pruebo para una fruta que sí está
fruta = "Naranja"
precio = buscar_precio(fruta)
if precio > 0: 
        print(f'El precio de {fruta} es {precio}')
else:
    print(f'{fruta} no está en el listado')

# pruebo para una fruta que no está
fruta = "Kiwi"
precio = buscar_precio(fruta)
if precio > 0: 
        print(f'El precio de {fruta} es {precio}')
else:
    print(f'{fruta} no está en el listado')