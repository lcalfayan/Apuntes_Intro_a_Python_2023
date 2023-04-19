# 4. Trabajando con datos
En esta clase vas a seguir aprendiendo a manipular datos con Python. Vas a escribir un programa que lee un archivo de datos en formato .CSV y realiza un cálculo simple. Vas a aprender a estructurar tu código creando funciones y estructuras de datos un poco más complejas como tuplas, conjuntos y diccionarios.
Vas a aprender a imprimir información con cierto formato, esto tiene un enorme potencial. 

Al final de la clase, vamos a trabajar con datos reales sobre los árboles de la ciudad de Buenos Aires en espacios públicos.



* [4.1 Introducción.](01_Introduccion.md)
* [4.2 Secuencias](02_Secuencias.md)
* [4.3 Contadores del módulo _collections_](03_Contadores.md)
* [4.4 Impresión con formato](04_Formato.md)
* [4.5 Arbolado porteño](05_Arboles1.md)
* [4.6 Cierre de la clase](06_Cierre.md)

# 4.1 Introducción.

En cada sección vas a encontrar un video corto con mayor nivel de detalle sobre los temas específicos. En esta unidad vamos a operar con datos guardados como secuencias de elementos. Veremos como tomar secciones (rebanadas, _slices_) de esas secuencias, como iterar sobre ellas. Veremos, además, que podés iterar sobre conjuntos de datos que _no_ están ordenados, como diccionarios. Visitamos la función `enumerate()` que crea una secuencia auxiliar. Usamos `zip()` para combinar dos secuencias en una y veremos las "tuplas" como estructuras de datos. Por último vamos a trabajar en el análisis de un conjunto de datos de la vida real: los datos públicos sobre el arbolado de la ciudad de Buenos Aires.

# 4.2 Secuencias

En esta sección hablamos de secuencias de datos.

### Tipo de secuencias

Python tiene tres tipos de datos que son *secuencias*.

* String: `'Hello'`. Una cadena es una secuencia de caracteres.
* Lista: `[1, 4, 5]`.
* Tupla: `('Pera', 100, 490.1)`.

Todas las secuencias tienen un orden, indexado por enteros, y tienen una longitud.

```python
a = 'Hello'               # String o cadena
b = [1, 4, 5]             # Lista
c = ('Pera', 100, 490.1)  # Tupla

# Orden indexado
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Longitud de secuencias
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Las secuencias pueden ser replicadas: `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Las secuencias del mismo tipo también pueden ser concatenadas: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```

### Rebanadas (slicing)

Sacar una rebanada es tomar una subsecuencia de una secuencia.
La sintaxis es `s[comienzo:fin]`, donde `comienzo` y `fin` son los índices de la subsecuencia que querés.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

* Los índices `comienzo` y `fin` deben ser enteros.
* Las rebanadas *no* incluyen el valor final. Es como los intervalos semi-abiertos en matemática.
* Si los índices son omitidos toman sus valores por defecto: el principio o el final de la lista.

### Reasigación de rebanadas

En listas, una rebanada puede ser reasignada o eliminada.

```python
# Reasignación
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

*Observación: La rebanada reasignada no tiene que tener necesariamente la misma longitud.*

```python
# Eliminación
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

### Reducciones de secuencias

Hay algunas operaciones usuales que reducen una secuencia a un solo valor.

```python
>>> s = [1, 2, 3, 4]
>>> sum(s)
10
>>> min(s)
1
>>> max(s)
4
>>> t = ['Hello', 'World']
>>> max(t)
'World'
>>>
```

### Iterar sobre una secuencia

Los ciclos `for` iteran sobre los elementos de una secuencia.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

En cada iteración del ciclo obtenés un nuevo elemento para trabajar. La variable iteradora va a tomar este nuevo valor. En el siguiente ejemplo la variable iteradora es `x`:

```python
for x in s:         # `x` es una variable iteradora
    ...instrucciones
```

En cada iteración, el valor previo de la variable (si hubo alguno) es sobreescrito. Luego de terminar el ciclo, la variable retiene su último valor.

### El comando break

Podés usar el comando `break` para romper un ciclo antes de tiempo.

```python
for name in namelist:
    if name == 'Juana':
        break
    ...
    ...
instrucciones
```

Cuando el comando  `break` se ejecuta, sale del ciclo y se mueve a las siguientes `instrucciones`.  El comando `break` sólo se aplica al ciclo más interno. Si un ciclo está anidado en otro ciclo, el comando no va a romper el ciclo externo.

### El comando continue

Para saltear un elemento y moverse al siguiente, usá el comando `continue`.

```python
for line in lines:
    if line == '\n':    # Salteo las instrucciones que procesan líneas
        continue
    # Instrucciones que procesan líneas
    ...
```

Éste es útil cuando el elemento encontrado no es de interés o es necesario ignorarlo en el procesamiento.

### Ciclos sobre enteros

Para iterar sobre un rango de números enteros, usá `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

La sintaxis es `range([comienzo,] fin [,paso])` (lo que figura entre corchetes es opcional).

```python
for i in range(100):
    # i = 0,1,...,99
    ...codigo
for j in range(10,20):
    # j = 10,11,..., 19
    ...codigo
for k in range(10,50,2):
    # k = 10,12,...,48
    # Observá que va de a dos.
    ...codigo
```

* El valor final nunca es incluido. Es como con las rebanadas.
* `comienzo` es opcional. Por defecto es `0`.
* `paso` es opcional. Por defecto es `1`.
* `range()` calcula los valores a medida que los necesita. No guarda realmente en memoria el rango completo de números.

### La función enumerate()

La función `enumerate` agrega un contador extra a una iteración.

```python
nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
    # i = 0, nombre = 'Edmundo'
    # i = 1, nombre = 'Juana'
    # i = 2, nombre = 'Rosita'
```

La forma general es `enumerate(secuencia [, start = 0])`. `start` es opcional.
Un buen ejemplo de cuándo usar `enumerate()` es para llevar la cuenta del número de línea mientras estás leyendo un archivo:

```python
with open(nombre_archivo) as f:
    for nlinea, line in enumerate(f, start=1):
        ...
```

Al fin de cuentas, `enumerate` es sólo una forma abreviada y simpática de escribir:

```python
i = 0
for x in s:
    instrucciones
    i += 1
```

Al usar `enumerate` tenemos que tipear menos y el programa funciona un poco más rápido.

### Tuplas y ciclos for

Podés iterar con múltiples variables de iteración.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    #   x = 1, y = 4
    #   x = 10, y = 40
    #   x = 23, y = 14
    #   ...
```

Cuando usás múltiples variables, cada tupla es *desempaquetada* en un conjunto de variables de iteración. El número de variables debe coincidir con la cantidad de elementos de cada tupla.

### La función zip()

La función `zip` toma múltiples secuencias y las combina en un iterador.

```python
columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)
# ('nombre','Pera'), ('cajones',100), ('precio',490.1)
```

Para obtener el resultado debés iterar. Podés usar múltiples variables para desempaquetar las tuplas como mostramos antes.

```python
for columna, valor in pares:
    ...
```

Un uso frecuente de `zip` es para crear pares clave/valor y construir diccionarios.

```python
d = dict(zip(columnas, valores))
```

 Como cierre te dejamos una [explicación](https://youtu.be/e_E-2tFcRwQ) para este tema.

## Ejercicios

### Ejercicio 4.1: Contar
Probá algunos ejemplos elementales de conteo:

```python
>>> for n in range(10):            # Contar 0 ... 9
        print(n, end=' ')

0 1 2 3 4 5 6 7 8 9
>>> for n in range(10,0,-1):       # Contar 10 ... 1
        print(n, end=' ')

10 9 8 7 6 5 4 3 2 1
>>> for n in range(0,10,2):        # Contar 0, 2, ... 8
        print(n, end=' ')

0 2 4 6 8
>>>
```

### Ejercicio 4.2: Más operaciones con secuencias
Interactivamente experimentá con algunas operaciones de reducción de secuencias.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

Probá iterar sobre los datos.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

A veces los comandos for, len(), y range() son combinados para recorrer listas:

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

Sin embargo, Python tiene mejores alternativas para esto. Te recomendamos familiarizarte con ellas y usarlas: por su simpleza producen código más legible y reducen la posibilidad de un bug en el código. Simplemente usá un ciclo `for` normal si querés iterar sobre los elementos de la variable `data`.  Y usá `enumerate()` si necesitás tener el índice por algún motivo.

### Ejercicio 4.3: Un ejemplo práctico de enumerate()
Recordá que el archivo  `Data/missing.csv` contiene datos sobre los cajones de un camión, pero tiene algunas filas que faltan. Usando `enumerate()`,
copiá tu programa `costo_camion.py` a la carpeta de la clase actual, y modificalo de forma que imprima un aviso (warning) cada vez que encuentre una fila incorrecta, indicando el número de fila.

```python
>>> cost = costo_camion('../Data/missing.csv')
Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
Fila 7: No pude interpretar: ['Naranja', '', '70.44']
>>>
```

Para hacer esto, vas a tener que cambiar algunas partes de tu código.

```python
...
for n_fila, fila in enumerate(filas, start=1):
    try:
        ...
    except ValueError:
        print(f'Fila {n_fila}: No pude interpretar: {fila}')
```

### Ejercicio 4.4: La función zip()
En el archivo `Data/camion.csv`, la primera línea tiene los encabezados de las columnas. En los códigos anteriores la descartamos.

```python
>>> f = open('../Data/camion.csv')
>>> filas = csv.reader(f)
>>> encabezados = next(filas)
>>> encabezados
['nombre', 'cajones', 'precio']
>>>
```

Pero, ¿no puede ser útil conocer los encabezados? Es acá donde la función `zip()` entra en acción. Primero tratá de aparear los encabezados con una fila de datos:

```python
>>> fila = next(filas)
>>> fila
['Lima', '100', '32.20']
>>> list(zip(encabezados, fila))
[ ('nombre', 'Lima'), ('cajones', '100'), ('precio', '32.20') ]
>>>
```

Fijate cómo `zip()` apareó los encabezados de las columnas con los valores de la columna.
Usamos `list()` arriba para devolver el resultado en una lista de forma que lo puedas ver. Normalmente, `zip()` crea un iterador que debe ser consumido en un ciclo for.

Este apareamiento es un paso intermedio para construir un diccionario. Probá lo siguiente:

```python
>>> record = dict(zip(encabezados, fila))
>>> record
{'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}
>>>
```

Esta transformación es un truco sumamente útil cuando tenés que procesar muchos archivos de datos. Por ejemplo, suponé que querés hacer que el programa `costo_camion.py` trabaje con diferentes archivos de entrada, pero que no le importe la posición exacta de la columna que tiene la cantidad de cajones o el precio. Es decir, que entienda que la columna tiene el precio por su encabezado y no por su posición dentro del archivo.

Modificá la función  `costo_camion()` en el archivo `costo_camion.py` para que se vea así:

```python
# costo_camion.py

def costo_camion(nombre_archivo):
    ...
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        ...
```

Ahora, probá tu función con un archivo completamente diferente `Data/fecha_camion.csv` que se ve así:

```csv
nombre,fecha,hora,cajones,precio
"Lima","6/11/2007","9:50am",100,32.20
"Naranja","5/13/2007","4:20pm",50,91.10
"Caqui","9/23/2006","1:30pm",150,83.44
"Mandarina","5/17/2007","10:30am",200,51.23
"Durazno","2/1/2006","10:45am",95,40.37
"Mandarina","10/31/2006","12:05pm",50,65.10
"Naranja","7/9/2006","3:15pm",100,70.44
```

```python
>>> costo_camion('../Data/fecha_camion.csv')
47671.15
>>>
```

Si lo hiciste bien, vas a descubrir que tu programa aún funciona a pesar de que le pasaste un archivo con un formato de columnas completamente diferente al de antes. ¡Y eso está muy bueno!

El cambio que hicimos acá es sutil, pero importante. En lugar de tener *hardcodeado* un formato fijo, la nueva versión de la función `costo_camion()` puede sacar la información de interés de cualquier archivo CSV. En la medida en que el archivo tenga las columnas requeridas, el código va a funcionar.

Copiá el programa `informe.py` que escribiste antes (ver [Ejercicio 3.4](../03_Contenedores_y_Errores/02_Contenedores.md#ejercicio-34-balances)) a la carpeta de ejercicios de la clase actual, y modificalo para que use esta técnica para elegir las columnas a partir de sus encabezados.

Probá correr el programa `informe.py` sobre el archivo  `Data/fecha_camion.csv`
y fijate si da la misma salida que antes.

### Ejercicio 4.5: Invertir un diccionario
Un diccionario es una función que mapea claves en valores. Por ejemplo, un diccionario de precios de cajones de frutas.

```python
>>> precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }
>>>
```

Si usás el método `items()`, obtenés pares `(clave,valor)`:

```python
>>> precios.items()
dict_items([('Pera', 490.1), ('Lima', 23.45), ('Naranja', 91.1), ('Mandarina', 34.23)])
>>>
```

Sin embargo, si lo que querés son pares `(valor, clave)`, ¿cómo lo hacés?
*Ayuda: usá `zip()`.*

```python
>>> lista_precios = list(zip(precios.values(),precios.keys()))
>>> lista_precios
[(490.1, 'Pera'), (23.45, 'Lima'), (91.1, 'Naranja'), (34.23, 'Mandarina')]
>>>
```

¿Por qué haría algo así? Por un lado porque te permite realizar cierto tipo de procesamiento de datos sobre la información del diccionario.

```python
>>> min(lista_precios)
(23.45, 'Lima')
>>> max(lista_precios)
(490.1, 'Pera')
>>> sorted(lista_precios)
[(23.45, 'Lima'), (34.23, 'Mandarina'), (91.1, 'Naranja'), (490.1, 'Pera')]
>>>
```

Esto también ilustra un atributo importante de las tuplas. Cuando son usadas en una comparación, las tuplas son comparadas elemento-a-elemento comenzando con el primero. Es similar a la lógica subyacente al orden lexicográfico o alfabético en las cadenas.

La función `zip()` se usa frecuentemente en este tipo de situaciones donde necesitás aparear datos provenientes de diferentes lugares. Por ejemplo, para aparear los nombres de las columnas con los valores para hacer un diccionario de valores con nombres.

Observá que `zip()` no está limitada a pares. Podés usarla con cualquier número de listas de entrada:

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

También, tené en cuenta que `zip()` se detiene cuando la más corta de las entradas se agota.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```

# 4.3 Contadores del módulo _collections_

El módulo `collections` ofrece objetos útiles para manejar datos. En esta sección (y en este [video](https://youtu.be/DoRHWjU3Ews)) introducimos brevemente los contadores, que son solo una de las clases incluidas en este módulo.

### Ejemplo: Contar cosas

Digamos que querés hacer una tabla con el total de cajones de cada fruta.

```python
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
```

Hay dos entradas de `Naranja` y dos de `Pera` en esta lista. Estos cajones deben ser combinados juntos de alguna forma.

### Contadores

Solución: Usá un  `Counter` (contador).

```python
from collections import Counter
total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

total_cajones['Naranja']     # 150
```

## Ejercicios

En este ejercicio vas a probar contadores en un par de ejemplos simples. Cargá tu programa `informe.py` y ejecutalo en el interprete de forma de tener los datos del camión con cajones cargado en modo interactivo.

Podés usar el interprete desde la línea de comandos ejecutando:
```bash
bash % python3 -i informe.py
```
O podés cargarlo en el Spyder y correrlo.


### Ejercicio 4.6: Contadores
Vamos a usar un contador (objeto `Counter`) para contar cajones de frutas. Probalo:

```python
>>> camion = leer_camion('../Data/camion.csv')
>>> from collections import Counter
>>> tenencias = Counter()
>>> for s in camion:
        tenencias[s['nombre']] += s['cajones']

>>> tenencias
Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150})
>>>
```

Observá que la entradas múltiples como `Mandarina`  y `Naranja` en `camion` se combinan en una sola entrada.

Podés usar el contador como un diccionario para recuperar valores individuales:

```python
>>> tenencias['Naranja']
150
>>> tenencias['Mandarina']
250
>>>
```

Podés listar las tres frutas con mayores tenencias:

```python
>>> # Las 3 frutas con más cajones
>>> tenencias.most_common(3)
[('Mandarina', 250), ('Naranja', 150), ('Caqui', 150)]
>>>
```

Carguemos los datos de otro camión con cajones de fruta en un nuevo contador:

```python
>>> camion2 = leer_camion('../Data/camion2.csv')
>>> tenencias2 = Counter()
>>> for s in camion2:
          tenencias2[s['nombre']] += s['cajones']

>>> tenencias2
Counter({'Durazno': 125, 'Frambuesa': 250, 'Lima': 50, 'Mandarina': 25})
>>>
```

Y finalmente combinemos las tenencias de ambos camiones con una operación simple:

```python
>>> tenencias
Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150})
>>> tenencias2
Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})
>>> combinada = tenencias + tenencias2
>>> combinada
Counter({'Caqui': 150, 'Durazno': 220, 'Frambuesa': 250, 'Lima': 150, 'Mandarina': 275, 'Naranja': 150})
>>>
```

Esto es solo una pequeña muestra de lo que se puede hacer con contadores. El módulo  `collections` es muy poderoso pero meterse a ver sus detalles sería una distracción ahora. Sigamos con nuestro curso...

# 4.4 Impresión con formato

En esta sección se ven detalles técnicos sobre cómo hacer que la salida por pantalla sea más amena para el usuario. Podés complementar la lectura con un [video](https://youtu.be/_Mlj6FcJZ9Y).

Cuando trabajás con datos es usual que quieras imprimir salidas estructuradas (tablas, etc.). Por ejemplo:

```code
  Nombre      Cajones     Precio
----------  ----------  -----------
 Lima           100        32.20
 Naranja         50        91.10
 Caqui          150       103.44
 Mandarina      200        51.23
 Durazno         95        40.37
 Mandarina       50        65.10
 Naranja        100        70.44
```

### Formato de cadenas

Una excelente manera de darle formato a una cadena en Python (a partir de la versión 3.6) es usando `f-strings`.

```python
>>> nombre = 'Naranja'
>>> cajones = 100
>>> precio = 91.1
>>> f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}'
'       Naranja        100      91.10'
>>>
```

La parte `{expresion:formato}` va a ser reemplazada. Usualmente los `f-strings` se usan con `print`.

```python
print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}')
```

### Códigos de formato

Lo códigos de formato (lo que va luego de `:` dentro de `{}`) son similares a los que se usan en el `printf()` del lenguaje C. Los más comunes son:

```code
d       Entero decimal
b       Entero binario
x       Entero hexadecimal
f       Flotante como [-]m.dddddd
e       Flotante como [-]m.dddddde+-xx
g       Flotante, pero con uso selectivo de la notación exponencial E.
s       Cadenas
c       Caracter (a partir de un entero, su código)
```

Los modificadores permiten ajustar el ancho a imprimir o la precisión decimal (cantidad de dígitos luego del punto). Ésta es una lista parcial:

```code
:>10d   Entero alineado a la derecha en un campo de 10 caracteres
:<10d   Entero alineado a la izquierda en un campo de 10 caracteres
:^10d   Entero centrado en un campo de 10 caracteres
:0.2f   Flotante con dos dígitos de precisión
```

### Formato a diccionarios

Podés usar el método `format_map()` para aplicarle un formato a los valores de un diccionario:

```python
>>> s = {
    'nombre': 'Naranja',
    'cajones': 100,
    'precio': 91.1
}
>>> '{nombre:>10s} {cajones:10d} {precio:10.2f}'.format_map(s)
'       Naranja        100      91.10'
>>>
```

Usa los mismos códigos que los `f-strings` pero toma los valores que provee el diccionario.

### El método format()

Existe un método  `format()` que permite aplicar formato a argumentos.

```python
>>> '{nombre:>10s} {cajones:10d} {precio:10.2f}'.format(nombre='Naranja', cajones=100, precio=91.1)
'       Naranja        100      91.10'
>>> '{:10s} {:10d} {:10.2f}'.format('Naranja', 100, 91.1)
'       Naranja        100      91.10'
>>>
```

La verdad es que `format()` nos resulta un poco extenso y preferimos usar `f-strings`.

### Formato estilo C

También podés usar el operador  `%`.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

Esto requiere un solo ítem, o una tupla a la derecha. Los códigos están también inspirados en el `printf()` de C. Tiene la dificultad de que hay que contar posiciones y todas las variables van juntas al final.

## Ejercicios

### Ejercicio 4.7: Formato de números
Un problema usual cuando queremos imprimir números es especificar el número de dígitos decimales. Los f-strings nos permiten hacerlo. Probá los siguientes ejemplos:

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```


La documentación completa sobre los códigos de formato usados en f-strings puede consultarse [acá](https://docs.python.org/3/library/string.html#format-specification-mini-language). El formato puede aplicarse también usando el operador `%` de cadenas.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

La documentación sobre códigos usados con `%` puede encontrarse [acá](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

A pesar de que suelen usarse dentro de un `print`, el formato de cadenas no está necesariamente ligado a la impresión. Por ejemplo, podés simplemente asignarlo a una variable.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```

### Ejercicio 4.8: Recolectar datos
En el [Ejercicio 4.4](../04_Datos/02_Secuencias.md#ejercicio-44-la-funcion-zip), modificaste tu programa `informe.py` que calcula las ganancias o pérdidas de un camión que compra a productores y vende en el mercado. Copiá su contenido en un nuevo archivo `tabla_informe.py` y guarda éste también en la carpeta de ejercicios de esta clase. Ahora dejá el archivo `informe.py`, y trabajá sobre `tabla_informe.py`. Lo vas a ir modificando durante los próximos ejercicios hasta producir una tabla como ésta:

```
 Nombre     Cajones     Precio     Cambio
---------- ---------- ---------- ----------
 Lima          100        32.2       8.02
 Naranja        50        91.1      15.18
 Caqui         150      103.44       2.02
 Mandarina     200       51.23      29.66
 Durazno        95       40.37      33.11
 Mandarina      50        65.1      15.79
 Naranja       100       70.44      35.84
```

En este informe, el "Precio" es el precio en el mercado y el "Cambio" es la variación respecto al precio cobrado por el productor.

Para generar un informe como el de arriba, primero tenés que recolectar todos los datos de la tabla. Escribí una función `hacer_informe()`
que recibe una lista de cajones y un diccionario con precios como input y devuelve una lista de tuplas conteniendo la información mostrada en la tabla anterior.

Agregá esta función a tu archivo `tabla_informe.py`. Debería funcionar como se muestra en el siguiente ejemplo:

```python
>>> camion = leer_camion('../Data/camion.csv')
>>> precios = leer_precios('../Data/precios.csv')
>>> informe = hacer_informe(camion, precios)
>>> for r in informe:
        print(r)

('Lima', 100, 32.2, 8.019999999999996)
('Naranja', 50, 91.1, 15.180000000000007)
('Caqui', 150, 103.44, 2.019999999999996)
('Mandarina', 200, 51.23, 29.660000000000004)
('Durazno', 95, 40.37, 33.11000000000001)
('Mandarina', 50, 65.1, 15.790000000000006)
('Naranja', 100, 70.44, 35.84)
...
>>>
```

### Ejercicio 4.9: Imprimir una tabla con formato
Volvé a hacer el ciclo `for` del ejercicio anterior pero cambiando la forma de imprimir como sigue:

```python
>>> for r in informe:
        print('%10s %10d %10.2f %10.2f' % r)

      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
...
>>>
```

O directamente usando  f-strings. Por ejemplo:

```python
>>> for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
...
>>>
```

Agregá estos últimos comandos a tu programa `tabla_informe.py`. Hacé que el programa tome la salida de la función `hacer_informe()` e imprima una tabla bien formateada.

### Ejercicio 4.10: Agregar encabezados
Suponete que tenés una tupla con nombres de encabezado como ésta:

```python
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
```

Agregá el código necesario a tu programa para que tome una tupla de encabezados como la de arriba y cree una cadena donde cada nombre de encabezado esté alineado a la derecha en un campo de 10 caracteres de ancho y separados por un solo espacio.

```python
'    Nombre    Cajones     Precio     Cambio'
```

Escribí el código que recibe los encabezados y crea una cadena de separación entre los encabezados y los datos que siguen. Esta cadena es simplemente una tira de caracteres "-" bajo cada nombre de campo. Por ejemplo:

```python
'---------- ---------- ---------- ----------'
```

Cuando esté listo, tu programa debería producir una tabla como esta:

```
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
```

### Ejercicio 4.11: Un desafío de formato
Por último, modificá tu código para que el precio mostrado incluya un símbolo de pesos ($) y la salida se vea como esta tabla:

```
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84
```

Guardá estos cambios en el archivo `tabla_informe.py` que más adelante los vas a necesitar.

### Ejercicio 4.12: Tablas de multiplicar
Escribí un programa `tablamult.py` que imprima de forma prolija las tablas de
multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.

```python
       0   1   2   3   4   5   6   7   8   9
---------------------------------------------
 0:    0   0   0   0   0   0   0   0   0   0
 1:    0   1   2   3   4   5   6   7   8   9
 2:    0   2   4   6   8  10  12  14  16  18
 3:    0   3   6   9  12  15  18  21  24  27
 4:    0   4   8  12  16  20  24  28  32  36
 5:    0   5  10  15  20  25  30  35  40  45
 6:    0   6  12  18  24  30  36  42  48  54
 7:    0   7  14  21  28  35  42  49  56  63
 8:    0   8  16  24  32  40  48  56  64  72
 9:    0   9  18  27  36  45  54  63  72  81
```


# 4.5 Arbolado porteño

El tema de esta sección está brevemente presentado en este [video](https://youtu.be/jIMVkyBxuv0).

En esta sección haremos algunos ejercicios que integran los conceptos aprendidos en las clases anteriores. Vamos a manejar archivos, diccionarios, listas, contadores y el comando `zip`, entre otras cosas. Entregá lo que puedas hacer. 

## Ejercicios

Vamos a repasar las herramientas que vimos en esta clase aplicándolas a una base de datos sobre árboles en parques de la Ciudad de Buenos Aires. Para empezar, descargá el archivo CSV de "[Arbolado en espacios verdes](https://data.buenosaires.gob.ar/dataset/arbolado-espacios-verdes)" en tu carpeta `Data`. Vamos a estudiar esta base de datos y responder algunas preguntas. Guardá los ejercicios de esta sección en un archivo `arboles.py`.

![Arbolado porteño](arboles.jpg)

### Descripción de la base



|Título de la columna|Tipo de dato|Descripción|
|:-------------:|:-------------:| ----- |
|long            | Número flotante (float) |Coordenadas para geolocalización |
|lat             | Número flotante (float) |Coordenadas para geolocalización |
|id_arbol            | Número entero (integer) |Identificador único del árbol |
|altura_tot          | Número entero (integer) |Altura del árbol (m)|
|diametro            | Número entero (integer) |Diámetro del árbol (cm) |
|inclinacio          | Número entero (integer) |Inclinación del árbol (grados) |
|id_especie          | Número entero (integer) |Identificador de la especie |
|nombre_com          | Texto (string) |Nombre común del árbol |
|nombre_cie          | Texto (string) |Nombre científico del árbol |
|tipo_folla          | Texto (string) |Tipo de follaje del árbol |
|espacio_ve          | Texto (string) |Nombre del espacio verde |
|ubicacion           | Texto (string) |Dirección del espacio verde |
|nombre_fam          | Texto (string) |Nombre de la familia del árbol |
|nombre_gen          | Texto (string) |Nombre del género del árbol |
|origen              | Texto (string) |Origen del árbol |
|coord_x             | Número flotante (float) |Coordenadas para localización |
|coord_y             | Número flotante (float) |Coordenadas para localización |


### Ejercicio 4.13: Lectura de los árboles de un parque
Definí una función `leer_parque(nombre_archivo, parque)` que abra el archivo indicado y devuelva una **lista de diccionarios** con la información del parque especificado. La lista debe tener un diccionario por cada árbol del parque elegido. Dicho diccionario debe tener los datos correspondientes a un árbol (recordá que cada fila del csv corresponde a un árbol).

_Sugerencia: basate en la función `leer_camion()` y usá también el comando `zip` como hiciste en el_ [Ejercicio 4.4](../04_Datos/02_Secuencias.md#ejercicio-44-la-funcion-zip) _para combinar el encabezado del archivo con los datos de cada fila. Inicialmente no te preocupes por los tipos de datos de cada columna, pero cuando empieces a operar con una columna modificá esta función para que ese dato sea del tipo adecuado para operar._

_Observación: La columna que indica el nombre del parque en el que se encuentra el árbol se llama `'espacio_ve'` en el archivo CSV._

Probá con el parque "GENERAL PAZ" para tener un ejemplo de trabajo, debería darte una lista con 690 árboles.

### Ejercicio 4.14: Determinar las especies en un parque
Escribí una función `especies(lista_arboles)` que tome una lista de árboles como la generada en el ejercicio anterior y devuelva el conjunto de especies (la columna `'nombre_com'` del archivo) que figuran en la lista.

_Sugerencia: Usá el comando `set` como en la [Sección 3.2](../03_Contenedores_y_Errores/02_Contenedores.md#conjuntos)._

### Ejercicio 4.15: Contar ejemplares por especie
Usando un diccionario contador (Counter) del módulo `collections` como en el [Ejercicio 4.6](../04_Datos/03_Contadores.md#ejercicio-46-contadores), escribí una función `contar_ejemplares(lista_arboles)` que, dada una lista como la generada con `leer_parque()`, devuelva un diccionario contador en el que las especies (recordá, es la columna `'nombre_com'` del archivo) sean las claves y tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada.

Luego, combiná esta función con `leer_parque()` y con el método `most_common()` para informar las cinco especies más frecuentes en cada uno de los siguientes parques:

- 'GENERAL PAZ'
- 'ANDES, LOS'
- 'CENTENARIO'

**Resultados** de cantidad por especie en tres parques:

General Paz | Los Andes | Centenario
-------------------------|-----------|--------------
Casuarina: 97 |Jacarandá: 117|Plátano: 137
Tipa blanca: 54|Tipa blanca: 28|Jacarandá: 45
Eucalipto: 49|Ciprés: 21|Tipa blanca: 42
Palo borracho rosado: 44 |Palo borracho rosado: 18|Palo borracho rosado: 41
Fenix: 40|Lapacho: 12|Fresno americano: 38


### Ejercicio 4.16: Alturas de una especie en una lista
Escribí una función `obtener_alturas(lista_arboles, especie)` que, dada una lista de árboles como la anterior y una especie de árbol (un valor de la columna `'nombre_com'` del archivo), devuelva una lista con las alturas (columna `'altura_tot'`) de los ejemplares de esa especie en la lista.

_Observación: Acá sí, fijate de devolver las alturas como números (de punto flotante) y no como cadenas de caracteres. Podés hacer esto modificando `leer_parque`_.

Usala para calcular la altura promedio y altura máxima de los 'Jacarandá' en los tres parques mencionados.

**Resultados** de alturas de Jacarandás en tres parques:

Medida | General Paz | Los Andes | Centenario
-------|------------------|-----------|--------------
max  |16.0 |25.0  | 18.0
prom |10.2 |10.54 | 8.96

### Ejercicio 4.17: Inclinaciones por especie de una lista
Escribí una función `obtener_inclinaciones(lista_arboles, especie)` que, dada una especie de árbol y una lista de árboles como la anterior, devuelva una lista con las inclinaciones (columna `'inclinacio'`) de los ejemplares de esa especie.

### Ejercicio 4.18: Especie con el ejemplar más inclinado
Combinando la función `especies()` con `obtener_inclinaciones()` escribí una función `especimen_mas_inclinado(lista_arboles)` que, dada una lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su inclinación.

Correlo para los tres parques mencionados anteriormente.

**Resultados.** Deberías obtener, por ejemplo, que en el Parque Centenario hay un _Falso Guayabo_ inclinado 80 grados.


### Ejercicio 4.19: Especie más inclinada en promedio
Volvé a combinar las funciones anteriores para escribir la función `especie_promedio_mas_inclinada(lista_arboles)` que, dada una lista de árboles devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado.

**Resultados.** Deberías obtener, por ejemplo, que los _Álamos Plateados_ del Parque Los Andes tiene un promedio de inclinación de 25 grados.


**Preguntas extras:** ¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado de toda la ciudad y no solo de un parque? ¿Podrías dar la latitud y longitud de ese ejemplar? ¿Y dónde se encuentra (lat,lon) el ejemplar más alto? ¿De qué especie es?


# 4.6 Cierre de la clase

Te recordamos que leas el [código de honor](../Codigo.md) del curso en el que hablamos de las reglas que rigen en este curso para evitar el plagio así como otros aspectos importantes sobre qué se puede compartir y qué no. Al enviar tus archivos entendemos que leíste y estas de acuerdo con este texto. En caso contrario no envíes tus archivos y contactate con los docentes.

Tené en cuenta que quizás algunos ejercicios sean corregidos automáticamente: es importante que respetes los nombres de las funciones, el orden de los parámetros y lo que devuelven esas funciones de manera que al correrlas den _exactamente_ lo que pide el enunciado.

* Para cerrar esta clase te pedimos que recopiles las soluciones de los siguientes ejercicios:
    1. El archivo `costo_camion.py` del [Ejercicio 4.4](../04_Datos/02_Secuencias.md#ejercicio-44-la-funcion-zip).
    2. El archivo `tabla_informe.py` del [Ejercicio 4.11](../04_Datos/04_Formato.md#ejercicio-411-un-desafio-de-formato).
    3. El archivo `tablamult.py` del [Ejercicio 4.12](../04_Datos/04_Formato.md#ejercicio-412-tablas-de-multiplicar).
    4. El archivo `arboles.py` con los ejercicios [Ejercicio 4.13](../04_Datos/05_Arboles1.md#ejercicio-413-lectura-de-los-arboles-de-un-parque) al [Ejercicio 4.19](../04_Datos/05_Arboles1.md#ejercicio-419-especie-mas-inclinada-en-promedio).


```python

```
