#1.7 LISTAS

nombres = [ 'Rosita', 'Manuel', 'Luciana' ]
nombres.insert(2, 'Iratxe') # Lo inserta en la posición 2. 
nombres.insert(0, 'Iratxe') # Lo inserta como primer elemento. 


#Iteradores de listas y búsqueda
for nombre in nombres:
    print(nombre)
    
# Ejercicios

#string de frutas, guardado dentro del objeto "frutas"
frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

# con el comando split() transformo el string en una lista
lista_frutas = frutas.split(',')
lista_frutas

#Ejercicio 1.22: Extracción y reasignación de elementos.
## Extraer elemento
lista_frutas[0]
# 'Frambueza'
lista_frutas[1]
# 'Manzana'
lista_frutas[-1]
# 'Pera'
lista_frutas[-7]
# Frambueza

## Reasignar elemento
lista_frutas[2] = 'Granada'
lista_frutas

# extraer un slice
lista_frutas[0:3]
#['Frambuesa', 'Manzana', 'Granada']
lista_frutas[-2:]
#['Sandía', 'Pera']

#Creá una lista vacía y agregale un elemento:
compra = []
compra.append('Pera')
compra
#['Pera']

#reasignar una lista a una porción de otra lista:
lista_frutas[-2:] = compra
lista_frutas
#['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Pera']
# reemplazó [Sandía, Pera] solo con la [Pera]

#Ejercicio 1.23: Ciclos sobre listas
for s in lista_frutas:
        print('s =', s)
        
#Ejercicio 1.24: Test de pertenencia
'Granada' in lista_frutas
#True
'Lima' in lista_frutas
# False
'Lima' not in lista_frutas
# True

# Ejercicio 1.25: Adjuntar, insertar y borrar elementos
lista_frutas.append('Mango')
lista_frutas
# ['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Pera', 'Mango']
lista_frutas.insert(1, 'Lima')
lista_frutas
#['Frambuesa', 'Lima', 'Manzana', 'Granada', 'Mandarina', 'Pera', 'Mango']
lista_frutas.remove('Mandarina')
lista_frutas
#['Frambuesa', 'Lima', 'Manzana', 'Granada', 'Pera', 'Mango']
lista_frutas.append('Frambuesa')
lista_frutas
#['Frambuesa', 'Lima', 'Manzana', 'Granada', 'Pera', 'Mango', 'Frambuesa']
lista_frutas.index('Frambuesa')
#muestra solo la primera aparicion de Frambuesa
lista_frutas[0]
lista_frutas[6]

lista_frutas.count('Banana')
lista_frutas.count('Frambuesa')

del lista_frutas[0]
lista_frutas
# ['Lima', 'Manzana', 'Granada', 'Pera', 'Mango', 'Frambuesa']

#Ejercicio 1.26: Sorting, ordenar elementos
lista_frutas.sort()
lista_frutas

lista_frutas.sort(reverse=True)
lista_frutas

#Usá sorted() si querés generar una nueva lista ordenada en lugar de ordenar la misma:

nueva_lista_frutas = sorted(lista_frutas)   # lista_futas  queda igual, la nueva lista guarda los valores ordenados
nueva_lista_frutas


#Ejercicio 1.27: Juntar múltiples cadenas
lista_frutas = ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
a = ','.join(lista_frutas)
a
#'Banana,Mango,Frambuesa,Pera,Granada,Manzana,Lima'
b = ':'.join(lista_frutas)
b
#'Banana:Mango:Frambuesa:Pera:Granada:Manzana:Lima'
c = ''.join(lista_frutas)
c
#'BananaMangoFrambuesaPeraGranadaManzanaLima'
lista_frutas

#Ejercicio 1.28: Listas de cualquier cosa
nums = [101, 102, 103]
items = ['spam', lista_frutas, nums]
items

items[0] #'spam'
items[0][0] #'s'
items[1] #['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
items[1][1] #'Mango
items[1][1][2] #'n'
items[2] #[101, 102, 103]
items[2][1] #102

#Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo
# en otro archivo: inclusive.py
