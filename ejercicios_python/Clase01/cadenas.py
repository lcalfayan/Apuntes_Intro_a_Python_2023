#Ejercicio 1.14: Extraer caracteres individuales y subcadenas
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
a= frutas[0]
print(a) #M
a1= frutas[1]
print(a1) #a
a2=frutas[2]
print(a2) #n
a3=frutas[-1]        # Último caracter
print(a3) #i
a4=frutas[-2]        # Índices negativos se cuentan desde el final
print(a4) #w


frutas[0] = 'm' #los strings son sólo de lectura, no permiten asignacion de items
frutas = frutas + 'Pera'
frutas = frutas + ',' + 'Pera'
frutas = 'Melon' + ',' + frutas

#Ejercicio 1.16: Testeo de pertenencia (test de subcadena)
'Naranja' in frutas 
#True
'nana' in frutas
#True
'Lima' in frutas
#False
'wik' in frutas
#False , parece que no lee al reves
'Lima' not in frutas
#True

#Ejercicio 1.17: Iteración sobre cadenas
cadena = "Ejemplo con for"
for c in cadena:
    print('caracter:', c)

cadena = "Ejemplo con for"
cant_o = 0
for c in cadena:            #c es una nueva variable, que va cambiando de asignacion en cada ciclo for
    print('caracter:', c)
    if c == "o":
        cant_o = cant_o + 1

#Ejercicio 1.18: geringoso --> en otro archivo

#Ejercicio 1.19: Métodos de cadenas
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

frutas.lower()
#'manzana,naranja,mandarina,banana,kiwi'
frutas #no pisa el objeto frutas que genere primero

frutas.upper()
#'MANZANA,NARANJA,MANDARINA,BANANA,KIWI'

frutas.find('Mandarina')
#16 : en el caracter 16, incluida las comas, empieza la palabra Mandarina
frutas[13:17]
#'ja,M'
frutas[16:25]
#'Mandarina'

frutas = frutas.replace('Kiwi','Melón')
frutas  #reeamplazo la palabra Kiwi por Melón

nombre = '   Naranja   \n'
nombre
nombre = nombre.strip()    # remueve espacios antes y despues de la cadena
nombre

prueba = '  esp  acio  '
prueba = prueba.strip()
prueba #no remueve espacios en el medio

#Ejercicio 1.20: f-strings
nombre = 'Naranja'
cajones = 100
precio = 91.1
f'{cajones} cajones de {nombre} a ${precio:0.2f}'
#'100 cajones de Naranja a $91.10'

#Ejercicio 1.21: Expresiones regulares
texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020.'

# Encontrar las apariciones de una fecha en el texto
import re      #"re" es un módulo que ayuda a hacer operaciones mas complejas con cadenas
re.findall(r'\d+/\d+/\d+', texto)
#['6/8/2020', '7/8/2020']

# Reemplazá esas apariciones, cambiando el formato
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto)
#'Hoy es 2020-8-6. Mañana será 2020-8-7.'

#Comentario
#para averiguar qué operaciones puedo hacer con un objeto
s = 'hello world'
#s.<tecla tab> (en la consola)
dir(s)
help(str)
help(s.upper)
