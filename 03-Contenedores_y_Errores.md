# 3. Contenedores y Errores
En esta clase vemos que las listas, diccionarios y conjuntos pueden ser útiles como *contenedores* y discutimos brevemente porqué es importante elegir el contenedor más cómodo.

Discutimos los tipos de errores (bugs) que pueden aparecer en un programa e introducimos algunas técnicas primitivas para buscarlos.

Por último, vemos como se puede invocar un programa en Python desde la línea de comandos y, un poco a vuelo de pájaro, cómo pasarle parámetros para especificar qué debe hacer.


* [3.1 Introducción](01_Introduccion.md)
* [3.2 Contenedores](02_Contenedores.md)
* [3.3 Errores](03_Bugs.md)
* [3.4 Llamados desde consola](04_Llamados_desde_cmd.md)
* [3.5 Cierre de la clase](05_Cierre.md)


# 3.1 Introducción

Estructuras de datos, algoritmos, y las relaciones entre ellos.

Cuando estés diseñando algoritmos de procesamiento de datos vas a encontrarte con algo muy interesante: un algoritmo en particular funciona eficientemente sólo si los datos están almacenados de cierta forma, y otro algoritmo que resuelva el mismo problema puede requerir que almacenes los datos en otra estructura completamente diferente.

Los algoritmos imponen restricciones sobre la forma de almacenar los datos. Como contracara, muchas veces una forma particular de almacenar los datos sugiere de por sí un algoritmo de procesamiento. 

Los algoritmos y las estructuras de datos pueden ser conceptos independientes pero están íntimamente relacionadas al funcionar, e influyen drásticamente en la eficiencia de los programas que las usan. 

Un caso clásico es el de los algoritmos de búsqueda:

Si queremos saber si un número particular está presente en una lista de números, el hecho de tener esa lista de números ordenada permite usar métodos de búsqueda que son mucho más eficientes que si dicha lista estuviera desordenada.

Supongamos que nuestra lista de números es 
Numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

Y estamos usando el siguiente algoritmo:

```code
	Avanzar una posición
	Es el numero que busco ?
		Si --> terminar (existe)
		No --> Loop
	Terminar (no existe)	
```

Si buscamos el `30`, el algoritmo visitaría las posiciones con: 10, 20, 30, y daría una respuesta (el número existe en la lista).

Si la lista estuviera desordenada, 
Numeros = [10, 90, 20, 80, 30, 70, 40, 60, 50]

El algoritmo visitaría: 10, 90, 20, 80, 30 y tardaría casi el doble en encontrar el número buscado. 

El hecho de _saber_ que la estructura de datos mantiene los datos ordenados, nos permite optimizar el algoritmo para ahorrar algunos pasos. Podemos decidir que el número _no_ está si encontramos un número mayor que el buscado:

```
	Avanzar una posición
	Es el numero que busco ?
		Si -- > Terminar (existe)
		No -- > Es mayor que el buscado ?
					Si --> Terminar (no existe)
					No --> Loop
```

Analizá qué posiciones visitaría el algoritmo si buscáramos p.ej. `33`.


El ejemplo muestra que una característica de la estructura de datos que usamos permite hacer más eficientes los algoritmos que trabajan con esa estructura. Es importante notar que sobre una lista desordenada esta optimzacion no se podría hacer, y sería necesario recorrer toda la lista hasta el final antes de poder decidir si un elemento existe o no.

En esta clase vamos a ver las tres estructuras de datos principales de Python, y algunos ejemplos de su uso.

# 3.2 Contenedores

En esta sección trataremos listas, diccionarios y conjuntos.

### Panorama

Para dar soluciones útiles, los programas suelen trabajar con una diversidad de objetos. Muchas veces éstos son representaciones de objetos en la vida real. Por ejemplo, en la clase pasada, el programa del camión de frutas [Ejercicio 2.9](../02_Estructuras_y_Funciones/04_Funciones.md#ejercicio-29-funciones-de-la-biblioteca) maneja listas que representan el contenido de un camión, y maneja un archivo .csv con una lista de precios del mercado. 

* Un camión con cajones de fruta
* Una tabla de precios de cajones de fruta

Si elegimos bien la forma en que representamos los objetos de la vida real dentro de un programa, podemos encontrar muy fácil programar las soluciones que buscamos (y viceversa). 

En Python hay tres opciones principales para elegir contenedores de datos.

* Listas - Secuencias ordenadas de datos.
* Diccionarios - Datos no ordenados.
* Conjuntos - Colección no ordenada de elementos únicos.

### Listas como contenedores

Usá listas cuando el orden de los datos importe. Acordate de que las listas pueden contener cualquier tipo de objeto.
Por ejemplo, una lista de tuplas.

```python
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]

camion[0]            # ('Pera', 100, 490.1)
camion[2]            # ('Limon', 150, 83.44)
```

#### Construcción de una lista

Cómo armar una lista desde cero.

```python
registros = []  # Empezamos con una lista vacía

# Usamos el .append() para agregar elementos
registros.append(('Pera', 100, 490.10))
registros.append(('Naranja', 50, 91.3))
...
```

Un ejemplo de cómo cargar registros desde un archivo.

```python
registros = []  # Empezamos con una lista vacía

with open('../Data/camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
```

### Diccionarios como contenedores

Los diccionarios son útiles si vamos a querer buscar rápidamente (por claves).
Por ejemplo, un diccionario de precios de cajones.

```python
precios = {
   'Pera': 513.25,
   'Limon': 87.22,
   'Naranja': 93.37,
   'Mandarina': 44.12
}
```

Así podemos buscar datos:

```python
>>> precios['Naranja']
93.37
>>> precios['Pera']
513.25
>>>
```

### Construcción de diccionarios

Ejemplo de armado de un diccionario desde cero.

```python
precios = {} # Empezamos con un diccionario vacío

# Agregamos elementos
precios['Pera'] = 513.25
precios['Limon'] = 87.22
precios['Naranja'] = 93.37
```

Un ejemplo de cómo armar un diccionario a partir del contenido de un archivo.

```python
precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])
```

Nota: Si probás estos comandos en el archivo `../Data/precios.csv`, vas a ver que casi anda. Pero hay una línea en blanco al final que genera un error. Usando lo que ya vimos, más adelante (en el [Ejercicio 3.3](../03_Contenedores_y_Errores/02_Contenedores.md#ejercicio-33-diccionarios-como-contenedores)) vas a tener que modificar el código para resolver el problema.

### Búsquedas en un diccionario

Podés verificar si una clave existe:

```python
if key in d:
    # YES
else:
    # NO
```

### Claves compuestas

Casi cualquier valor puede usarse como clave en un diccionario de Python. La principal restricción es que una clave debe ser de tipo inmutable.
Por ejemplo, tuplas:

```python
feriados = {
  (1, 1) : 'Año nuevo',
  (1, 5) : 'Día del trabajador',
  (13, 9) : "Día del programador",
}
```

Luego, podemos acceder al diccionario así:

```python
>>> feriados[(1, 5)]
'Día del trabajador'
>>>
```

*Las listas, los conjuntos y los diccionarios no pueden ser usados como claves de diccionarios, porque son mutables.*

### Conjuntos

Un conjunto es una colección de elementos únicos sin orden y sin repetición.


```python
citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
citricos = set(['Naranja', 'Limon', 'Mandarina'])
```

Los conjuntos son útiles para evaluar pertenencia.

```python
>>> citricos
set(['Naranja', 'Limon', 'Mandarina'])
>>> 'Naranja' in citricos
True
>>> 'Manzana' in citricos
False
>>>
```

Los conjuntos también son útiles para eliminar duplicados.

```python
nombres = ['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana']

unicos = set(nombres)
# unicos = {'Manzana', 'Banana', 'Naranja', 'Pera'}
```

Más operaciones en conjuntos:

```python
citricos.add('Banana')        # Agregar un elemento
citricos.remove('Limon')    # Eliminar un elemento

A | B                 # Unión de conjuntos A y B
A & B                 # Intersección de conjuntos
A - B                 # Diferencia de conjuntos
```

![Operaciones de conjuntos](Set_UID.png)

## Ejercicios

En estos ejercicios, vas a empezar a construir un programa más largo. Trabajá en el archivo `ejercicios_python/Clase02/informe.py`.

### Ejercicio 3.1: Lista de tuplas
El archivo `../Data/camion.csv` contiene la lista de cajones cargados en un camión.  En el [Ejercicio 2.9](../02_Estructuras_y_Funciones/04_Funciones.md#ejercicio-29-funciones-de-la-biblioteca) escribiste una función `costo_camion(nombre_archivo)` que leía el archivo y realizaba un cálculo.

La función debería verse parecida a ésta:

```python
# fragmento de costo_camion.py
import csv
...

def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                ncajones = int(row[1])
                precio = float(row[2])
                total += ncajones * precio
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return total

...
```


Usando este código como guía, creá un nuevo archivo `informe.py`. En este archivo, definí una función `leer_camion(nombre_archivo)` que abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas. Para hacerlo vas a tener que hacer algunas modificaciones menores al código de arriba.

Primero, en vez de definir `total = 0`, tenés que empezar con una variable que empieza siendo una lista vacía Por ejemplo:

```python
camion = []
```

Segundo, en vez de sumar el costo, tenés que pasar cada fila a una tupla igual a como lo hiciste en el último ejercicio, y agregarla a la lista. Por ejemplo:

```python
for row in rows:
    lote = (row[0], int(row[1]), float(row[2]))
    camion.append(lote)
```

Por último, la función debe devolver la lista `camion`.

Experimentá con tu función interactivamente (acordate de que primero tenés que correr el programa `informe.py` en el intérprete):

*Ayuda: Usá `-i` para ejecutar un archivo en la terminal y quedar en el intérprete*

```python
>>> camion = leer_camion('../Data/camion.csv')
>>> camion
[('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Limon', 150, 83.44), ('Mandarina', 200, 51.23),('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]
>>>
>>> camion[0]
('Lima', 100, 32.2)
>>> camion[1]
('Naranja', 50, 91.1)
>>> camion[1][1]
50
>>> total = 0.0
>>> for s in camion:
        total += s[1] * s[2]

>>> print(total)
47671.15
>>>
```

Esta lista de tuplas que creaste es muy similar a un array o matriz bidimensional. Por ejemplo, podés acceder a una fila específica y columna específica usando una búsqueda como `camion[fila][columna]` donde `fila` y `columna` son números enteros.

También podés reescribir el último ciclo for usando un comando como éste:

```python
>>> total = 0.0
>>> for nombre, cajones, precio in camion:
            total += cajones*precio

>>> print(total)
47671.15
>>>
```

*Observación: la instrucción `+=` es una abreviación. Poner `a += b` es equivalente a poner `a = a + b`*

### Ejercicio 3.2: Lista de diccionarios
Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para representar las diferentes columnas del archivo de entrada.

Experimentá con esta función nueva igual que en el ejercicio anterior.

```python
>>> camion = leer_camion('../Data/camion.csv')
>>> camion
[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Limon', 'cajones': 150, 'precio': 83.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]
>>> camion[0]
{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}
>>> camion[1]
{'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}
>>> camion[1]['cajones']
50
>>> total = 0.0
>>> for s in camion:
        total += s['cajones']*s['precio']

>>> print(total)
47671.15
>>>
```

Fijate que acá los distintos campos para cada entrada se acceden a través de claves en vez de la posición en la lista. Muchas veces preferimos esto porque el código resulta más fácil de leer. Tanto para otres como para nosotres en el futuro.

Mirar diccionarios y listas muy grandes puede ser un lío. Para limpiar el output para debuguear, probá la función `pprint` (Pretty-print) que le da un formato más sencillo de interpretar.

```python
>>> from pprint import pprint
>>> pprint(camion)
[{'nombre': 'Lima', 'precio': 32.2, 'cajones': 100},
    {'nombre': 'Naranja', 'precio': 91.1, 'cajones': 50},
    {'nombre': 'Limon', 'precio': 83.44, 'cajones': 150},
    {'nombre': 'Mandarina', 'precio': 51.23, 'cajones': 200},
    {'nombre': 'Durazno', 'precio': 40.37, 'cajones': 95},
    {'nombre': 'Mandarina', 'precio': 65.1, 'cajones': 50},
    {'nombre': 'Naranja', 'precio': 70.44, 'cajones': 100}]
>>>
```

### Ejercicio 3.3: Diccionarios como contenedores
Los diccionarios son útiles si querés buscar elementos usando índices que no sean números enteros. En la terminal de Python, jugá con un diccionario:

```python
>>> precios = {}
>>> precios['Naranja'] = 92.45
>>> precios['Mandarina'] = 45.12
>>> precios
... mirá el resultado ...
>>> precios['Naranja']
92.45
>>> precios['Manzana']
... mirá el resultado ...
>>> 'Manzana' in precios
False
>>>
```

En el [Ejercicio 2.7](../02_Estructuras_y_Funciones/04_Funciones.md#ejercicio-27-buscar-precios) escribiste una función que busca el precio de una determinada fruta o verdura en el archivo `../Data/precios.csv`. Esto es útil para saber sobre un producto en particular, pero si necesitás tener los precios de toda la mercadería, no resulta práctico abrir y cerrar el archivo para consultar cada precio. Por eso ahora te proponemos generar un diccionario que contenga todos los precios. En este diccionario, podés consultar luego los precios de cada producto.

Escribí una función `leer_precios(nombre_archivo)` que a partir de un conjunto de precios como éste arme un diccionario donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.

Para hacerlo, empezá con un diccionario vacío y andá agregándole valores igual a como hiciste antes, pero ahora esos valores los vas leyendo del archivo.

Vamos a usar esta estructura de datos para buscar rápidamente los precios de las frutas y verduras.

Un par de consejos:
Usá el módulo `csv` igual que antes.

```python
>>> import csv
>>> f = open('../Data/precios.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['Lima', '40.22']
['Uva', '24.85']
...
[]
>>>
```

El archivo `Data/precios.csv` puede tener líneas en blanco, esto te puede traer complicaciones.
Observá que arriba figura una lista vacía (la última), porque la última línea del archivo no tenía datos.

Puede suceder que esto haga que tu programa termine con una excepción. Usá los comandos `try` y `except` para evitar el problema.
Para pensar: ¿sería mejor prevenir estos problemas con el comando `if` en vez de `try` y `except`?

Una vez que hayas escrito tu función `leer_precios()`, testeala interactivamente para asegurarte de que funciona bien:

```python
>>> precios = leer_precios('../Data/precios.csv')
>>> precios['Naranja']
106.28
>>> precios['Mandarina']
80.89
>>>
```

### Ejercicio 3.4: Balances
Supongamos que los precios en `camion.csv` son los precios pagados al productor de frutas mientras que los precios en `precios.csv` son los precios de venta en el lugar de descarga del camión.

Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa `informe.py` (usando las funciones `leer_camion()` y `leer_precios()`) y completá el programa para que con los precios del camión ([Ejercicio 3.2](../03_Contenedores_y_Errores/02_Contenedores.md#ejercicio-32-lista-de-diccionarios)) y los de venta en el negocio ([Ejercicio 3.3](../03_Contenedores_y_Errores/02_Contenedores.md#ejercicio-33-diccionarios-como-contenedores)) calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

Ayuda: hubo una ganancia de algo más de quince mil pesos.

# 3.3 Errores

En esta sección hablamos sobre errores. Acá hay un [video](https://youtu.be/1nTWUPopXrI) sobre este tema.

## Tres tipos de errores:

Programando nos podemos encontrar con tres tipos de errores.

Los *errores sintácticos* son los que se dan cuando escribimos incorrectamente. Por ejemplo si queremos escribir `x = (a + b) * c` pero en vez de eso escribimos `x = (a + b] * c`, el programa no va a correr.

Un segundo tipo de error lo forman los errores *en tiempo de ejecución*, que se dan cuando el programa empieza a ejecutarse pero se produce un error durante su ejecución. Por ejemplo si le pedimos al usuarie que ingrese su edad esperando un número entero e ingresa "veintiséis años", es probable que el programa dé un error. Si leemos un archivo CSV y una fila tiene datos faltantes, el programa puede dar un error. Este tipo de errores en Python generan _excepciones_ que, como veremos más adelante, pueden atraparse administrarse adecuadamente.

El tercer tipo de error es el más difícil de encontrar y de entender. Son los *errores semánticos*, que se dan cuando el programa no hace lo que está diseñado para hacer. Tienen que ver con el sentido de las instrucciones. En estos casos el programa se ejecuta pero da un resultado incorrecto o inesperado. En general, la mejor forma de encontrar estos errores es correr paso a paso el código que genera un resultado inesperado, tratando de entender dónde está la falla, usando el debugger. Veremos cómo usar el debugger la clase que viene, por ahora trabajaremos de forma un poco más primitiva.

## Debuggear a mano

Los errores (o bugs) son difíciles de rastrear y resolver. Especialmente aquellos errores que no resultan en un mensaje de error por parte del intérprete, sino que resultan en que el programa no pueda continuar o dé un resultado inesperado. Si tu programa corre, pero no da el resultado que esperás, o _se cuelga_ y no entendés por qué, existen herramientas concretas que te ayudan a buscar el origen del problema. A continuación veremos algunas metodologías específicas (aunque un poco primitivas) que permiten rastrear el origen del problema.

### ¿Qué dice un traceback?
Si el intérprete te da un mensaje de error, estás en el caso más fácil. Lo primero que podés hacer es intentar entender la causa del error usando como punto de partida el "traceback":

```bash
python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", line 4, in spam
    x.append(3)
AttributeError: 'int' object has no attribute 'append'
```
La última línea dice algo así como "el objeto `int` no tiene un atributo `append` "- lo cual es obvio, pero ¿cómo llegamos ahí?

La última línea es el motivo concreto del error.

Las líneas anteriores te dicen el camino que siguió el programa hasta llegar al error. En este caso: el error ocurrió en `x.append(3)` en la línea 4, dentro de la función `spam` del módulo `"blah.py"`, que fue llamado por la función `bar` en la línea 7 del mismo archivo, que fue llamada por... y así siguiendo. 
En este caso en particular, la pregunta es: es  `x` efectivamente un objeto que implementa el método `.append()` ?  Hay que revisar el programa.

Sin embargo a veces el traceback no proporciona suficiente información (por ejemplo, no sabemos el valor de cada parámetro usado en las llamadas).

Una posibilidad que a veces da resultado es copiar el traceback en Google. Si estás usando una biblioteca de funciones que mucha gente usa (como `numpy` o `math`) es muy probable que alguien se haya encontrado antes con el mismo problema que vos, y alguien más le haya explicado qué lo causa, o cómo evitarlo. Podés aprender mucho con esas búsquedas, y en muchos casos tu programa está cometiendo el mismo error.

### Usá el modo [REPL](https://es.wikipedia.org/wiki/REPL) de Python

Si usás Python desde la línea de comandos, podés usarlo pasándole un `-i` como parámetro antes del script a ejecutar. Cuando el intérprete de Python termine de ejecutar el script se va a quedar en modo interactivo (en lugar de volver al sistema operativo). Podés averiguar en qué estado quedó el sistema. 

```bash
python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", line 4, in spam
    x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>     print( repr(x) )
```

Este *parámetro* (el `-i`, que ya usamos antes) preserva el estado del intérprete al finalizar el script y te permite interrogarlo sobre el estado de las variables y obtener información que de otro modo perderías. En el ejemplo de recién interesa saber qué es `x` y cómo llegó a ese estado. Si estás usando un IDE esta posibilidad de interacción suele ocurrir naturalmente.

### Debuggear con `print`

`print()` es una forma rápida y sencilla de permitir que el programa se ejecute (casi) normalmente mientras te da información del estado de las variables. Si elegís bien las variables que mostrar, es probable que digas "¡¡Ajá!!".

*Sugerencia: es conveniente usar `repr()` para imprimir las variables*

```python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()` te muestra una representación técnicamente más precisa del valor de una variable, y no la representación *bonita* que solemos ver.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# SIN `repr`
>>> print(x)
3.4
# CON `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```

### Debuggear con lápiz y papel

Muchas veces unx *asume* que el intérprete está haciendo algo. Si agarrás un lápiz y un papel y _hacés de intérprete_ anotando el estado de cada variable y siguiendo las instrucciones del programa paso a paso, es posible que entiendas que las cosas no son como creías.

Estas alternativas son útiles pero un poco primitivas. La mejor forma de debuggear un programa en Python es usar el debugger.

### Disenar casos de prueba

Es mas común cometer errores en ciertas estructuras de un programa que en otras: referirse posiciones de una lista que no existen, pedir elementos de un diccionario usando una clave equivocada y devolver el resultado de una función en un tipo de datos equivocado son errores relativamente comunes.

Algunos de estos errores _no_ resultan en excepciones, ni mensajes de error por parte del intérprete sino simplemente en resultados no esperados reportados por tu script.

Un método útil para detectar errores de este tipo es diseñar "casos de prueba": conjuntos de datos de entrada cuya salida es conocida, que podés usar para tratar de poner en evidencia errores de escritura. *Cuidado:* pasar airosamente un caso de prueba no verifica que tu programa funcione bien. Sólo dice que no pudiste detectar un error en su lógica. El diseño de casos de prueba es un arte en sí mismo. Ejercitar en esa técnica desde temprano puede serte muy útil.

Verás algunos ejemplos de casos de prueba más abajo, en los ejercicios.

## Ejercicios:

En los siguientes ejercicios te proponemos que uses las técnicas que mencionamos arriba para resolver los problemas que aparecen a continuación.
Determiná los errores de los siguientes códigos y corregilos en un archivo `solucion_de_errores.py` comentando brevemente los errores. ¿Qué tipo de errores tiene cada uno?

En el archivo `solucion_de_errores.py` separá las correcciones de los distintos códigos con una línea que contenga solamente los símbolos `#%%` seguido de una o varias líneas comentadas indicando el ejercicio y el problema que tenía. Al terminar, debería verse así tu archivo:

```python
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
#    Lo corregí cambiando esto por aquello.
#    A continuación va el código corregido
...
...

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...
...
```


### Ejercicio 3.5: Semántica
¿Anda bien en todos los casos de prueba?
```python
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
```

### Ejercicio 3.6: Sintaxis
¿Anda bien en todos los casos de prueba?
```python
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
```

### Ejercicio 3.7: Tipos
¿Anda bien en todos los casos de prueba?
```python
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
```

### Ejercicio 3.8: Alcances
La siguiente suma no da lo que debería:
```python
def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
```

### Ejercicio 3.9: Pisando memoria
El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, ¿podés determinar por qué y explicarlo brevemente en la versión corregida?

Te dejamos un [video](https://youtu.be/xb3IG44SP08) sobre este ejemplo.

```python
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
```

_Ayuda: Primero tratá de pensarlo, pero si este último se te hace muy difícil, podés mirar un poco de la teoría relacionada con esto un par de secciones más adelante ([Sección 5.4](../05_Listas/04_Objetos.md#ejemplo-de-asignación))._

# 3.4 Llamados desde consola

Ya vimos que el Python se puede correr desde la consola. También podemos correr programas escritos en pythons desde la consola. Esto nos permite usarlos de manera muy práctica

## Llamados desde consola:

Se relaciona con la [Sección 1.5](../01_Intro_a_Python/05_Lineas_de_Comandos.md#la-línea-de-comandos).

Ya vimos en la [Sección 1.5](../01_Intro_a_Python/05_Lineas_de_Comandos.md#la-línea-de-comandos) que Python se puede correr desde la consola. También podemos pasarle como parámetro, al invocarlo, el nombre de un script que queremos que ejecute. Esto nos permite usarlo de manera muy práctica. Abrí una ventana terminal y probá esto:

```code
PS ...\Clase03> py ../Clase01/rebotes.py
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
```

Fijate que estamos en la carpeta de la clase 3 (`\Clase03>`) y le estamos pidiendo a Python que ejecute el script `rebotes.py` que hiciste en la clase 1, y que está en ese directorio (`../Clase01/rebotes.py`). La salida es el resultado de esa ejecución.

Ahora vamos a darle un poco más de flexibilidad a `rebotes.py`.

Escribí el siguiente código y guardalo con el nombre `parametros.py`

```python
import sys

print (sys.argv)
```

Ahora ejecutalo desde la línea de comandos con

```
PS ...\Clase03> py parametros.py
['parametros.py']
```

Y ahora probá:
```
PS ...\Clase03> py parametros.py uno dos tres
['parametros.py', 'uno', 'dos', 'tres']
```

Sin entrar en detalles, lo que hace el script es imprimir una variable (`sys.argv` del módulo `sys`). Esa variable es una lista (por eso los corchetes en la salida `['parametros.py']`) y esa lista contiene los parámetros que le dimos a Python al invocarlo (`
['parametros.py', 'uno', 'dos', 'tres']`). Notá que el primer parámetro en la lista (con índice `0`) es el nombre del script a ejecutar.

Esto es interesante porque implica que un script puede acceder a los parámatros que hayas escrito en la línea de comandos, incluso a su propio nombre. 

Cambiemos este pequeño script para que haga un cálculo con los parámetros que le pases:

```python
import sys

param1 = int(sys.argv[1])
param2 = int(sys.argv[2])

print (param1 * param2)
```

Y volvé a probarlo como antes.

No funciona, verdad ? Porqué ? Que dice el Traceback ? (probálo!). Dice que hubo una excepción de tipo `ValueError` porque la función `int()` no puede interpretar la cadena `uno` y por lo tanto el script se detiene.

Podríamos evitar que esta excepción detenga el programa, pero por ahora no compliquemos el script, y pasémosle parámetros que pueda usar:

```
...\Clase03> py parametros.py 4 3
12
```

## Ejercicios:
Usando estas ideas, modificá `rebotes.py` para que la altura inicial de la pelota no sea ya 100 metros, sino que la puedas especificar al invocar el script, de modo de obtener este comportamiento:

```code
...\Clase03> py rebotes.py 300
1 180.0
2 108.0
3 64.8
4 38.88
5 23.328
6 13.9968
7 8.3981
8 5.0389
9 3.0233
10 1.814
```

Atención a la forma de invocar el script ! 
Qué acaba de pasar acá ? Hemos "exportado" una función escrita en Python y ahora la podemos invocar desde la línea de comandos pasándole los parámetros necesarios. Poderoso!


Esta modificación para recibir parámetros desde la línea de comandos tiene una ventaja y una desventaja. La ventaja esta clara. La desventaja tal vez también: ahora _es obligatorio_ pasarle parámetros por línea de comandos. 

En general, los programas tienen cierto comportamiento si uno les pide que hagan algo en particular, y otro comportamiento si uno no les pide nada (por ejemplo, en el caso de `zip` que usamos en la clase 1, si no le pedimos que haga nada en particular nos dá una ayuda)

Podemos lograr este comportamiento midiendo la longitud de la lista `sys.argv`, o checkeando que cumpla ciertas características.

### Ejercicio 3.10: Parámetros por omisión
Antes de asignar un valor a la altura inicial de la pelota, medí la longitud de la lista de parámetros. Si _omitimos_ pasarle el parámetro para la altura inicial, que use el valor por omisión de 100 metros. Si le pasamos una altura, entonces que use ésa. 

### Ejercicio 3.11: Ejecución desde la línea de comandos con parámetros
En el programa `costo_camion.py` del ejercicio [Ejercicio 2.9](../02_Estructuras_y_Funciones/04_Funciones.md#ejercicio-29-funciones-de-la-biblioteca), el nombre del archivo de entrada `'../Data/camion.csv'` fue escrito en el código.

```python
# costo_camion.py
import csv

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
```

Esto está bien para ejercitar, pero en un programa real probablemente no harías eso ya que querrías una mayor flexibilidad. Una posibilidad es pasarle al programa el nombre del archivo que querés procesar como un parámetro cuando lo llamás desde la línea de comandos.

Copiá el contenido de `costo_camion.py` a un nuevo archivo llamado `camion_commandline.py` que incorpore la lectura de parámetros por línea de comando según la sugerencia del siguiente ejemplo:

```python
# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
```

Como vimos antes, `sys.argv` es una lista que contiene los argumentos que le pasamos al script al momento de llamarlo desde la línea de comandos (si es que le pasamos alguno). Por ejemplo, desde una terminal de Unix (en Windows es similar), para correr nuestro programa y que procese el mismo archivo podríamos escribir:

```bash
bash $ python3 camion_commandline.py ../Data/camion.csv
Costo total: 47671.15
bash $
```

O con el archivo `missing.csv`:
```bash
bash $ python3 camion_commandline.py ../Data/missing.csv
...
Costo total: 30381.15
bash $
```
Si no le pasamos ningún archivo, va a mostrar el resultado para `camion.csv` porque lo indicamos con la línea `nombre_archivo = '../Data/camion.csv'`.

Guardá tu programa en el archivo `camion_commandline.py` para entregar al final de la clase.


Te dejamos un [video](https://youtu.be/D4WI4qsuwrQ) explicando cómo funciona el pasaje de parámetros por línea de comandos en Python. 


# 3.5 Cierre de la clase

Como todas las semanas, te vamos a pedir que envies tus ejercicios resueltos por mail. Recordá usar siempre la misma dirección de mail y poner como *subject* del correo **[Unidad 3]**. Los ejercicios de esta unidad los podés enviar hasta el día viernes 26 de agosto inclusive. *Recordá:* Si cursás en el turno de los miércoles, mandá tus ejercicios a python@unsam.edu.ar, si cursás en el turno de los jueves mandalos a pythonunsam@gmail.com.

* Los ejercicios a enviar esta semana son:
    1. El archivo `informe.py` del [Ejercicio 3.4](../03_Contenedores_y_Errores/02_Contenedores.md#ejercicio-34-balances).
    2. El archivo `solucion_de_errores.py` con los ejercicios [Ejercicio 3.5](../03_Contenedores_y_Errores/03_Bugs.md#ejercicio-35-semantica) al [Ejercicio 3.9](../03_Contenedores_y_Errores/03_Bugs.md#ejercicio-39-pisando-memoria).
    3. El archivo `camion_commandline.py` del [Ejercicio 3.11](../03_Contenedores_y_Errores/04_Llamados_desde_cmd.md#ejercicio-311-ejecucion-desde-la-linea-de-comandos-con-parametros).
    
¡Nos vemos pronto!




```python

```
