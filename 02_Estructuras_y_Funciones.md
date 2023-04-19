# 2. Estructuras y funciones
Esta clase comenzamos a utilizar un entorno de desarrollo integrado (IDE). 

Para escribir programas útiles, necesitamos aprender a trabajar con algunas estructuras de datos un poco más complejas. En esta clase introducimos las estructuras de datos elementales de Python que nos faltan: tuplas, conjuntos y diccionarios y profundizamos un poco más en las listas y sus usos. También comenzamos a ver cómo estructurar el código usando funciones y a leer archivos.



* [2.1 Introducción y repaso.](01_Introduccion_y_repaso.md)
* [2.2 Entorno de desarrollo integrado](02_IDE.md)
* [2.3 Manejo de archivos](03_Archivos.md)
* [2.4 Funciones](04_Funciones.md)
* [2.5 Tipos y estructuras de datos](05_TiposDatos.md)
* [2.6 Cierre de la clase](06_Cierre.md)


# 2.1 Introducción y repaso.

En este [video](https://youtu.be/xHTMgN2l4_g) damos una breve introducción a los temas de la clase. Luego vas a encontrar también algunos videos con mayor nivel de detalle sobre los temas de las secciones.


Te dejamos acá además un [video](https://youtu.be/sFt_1z9L4J8) con un repaso del [Ejercicio 1.11](../01_Intro_a_Python/04_Numeros.md#ejercicio-111-hipoteca-ajustado) de la hipoteca de David.

¡Que disfrutes la clase!


# 2.2 Entorno de desarrollo integrado

A partir de aquí te vamos a proponer trabajar principalmente dentro de un entorno de desarrollo integrado (IDE, por sus siglas en inglés). 

En particular, sugerimos trabajar con el [Spyder](https://www.spyder-ide.org/) que es un entorno de desarrollo de Python diseñado para científicos, ingenieros y analistas de datos. El Spyder puede descargarse solo o como parte de la distribución de [Anaconda](https://www.anaconda.com/products/individual) que trae, además de Python y del Spyder, una serie de bibliotecas con módulos muy útiles para desarrollos relacionados a la ciencia de datos.

En este [breve video](https://youtu.be/fHMnZ1gYOew) mostramos el spyder.

Esta es una imagen de una captura de pantalla del Spyder:
![Ventana de Spyder](Spyder.png)


En la captura se puede ver que por defecto el Spyder viene estructurado con tres ventanas. Un editor de código ocupa la mitad izquierda de la ventana, mientras que la mitad derecha se divide en una terminal (o consola) interactiva de Python en la mitad inferior y un inspector de variables en la mitad superior. El Spyder nos permite correr línea por línea el código del editor (tecla `F9`) y ver el estado de las variables en el inspector de variables, o ejecutarlo completo (tecla `F5`). También nos permite debuguear el código con facilidad (botones azules de la barra superior).

Les recomendamos que le dediquen un tiempo a probar sus últimos ejercicios en este entorno. Verán que es muy cómodo. Pueden mirar un [breve tutorial](https://www.youtube.com/watch?v=0fxURPC1YFs) donde no sólo les enseñan el uso de la tecla `F5`, sino también una introducción al uso del debugger (le dice depurador) que veremos más adelante en este curso.


# 2.3 Manejo de archivos

La mayoría de los programas usa alguna fuente de datos. En esta sección discutimos el acceso a archivos, tema que introducimos en este [video](https://youtu.be/KTCS13-Z8bI). Te dejamos también el [código](./arboles.py) y el [archivo](./arboles.csv) que usamos en el video.

### Archivos de entrada y salida

Con estos comandos podés abrir dos archivos, una para lectura y otro para escritura:

```python
f = open('foo.txt', 'rt')     # Abrir para lectura ('r' de read, 't' de text)
g = open('bar.txt', 'wt')     # Abrir para escritura ('w' de write, 't' de text)
```

_Observación: los nombres [foo, bar, foobar](https://es.wikipedia.org/wiki/Foo) son genéricos que se usan usualmente para aludir a un nombre que se ignora, son los análogos informáticos a fulano, mengano y zutano._

Para leer el archivo completo, o una parte:

```python
data = f.read()

# Leer 'maxbytes' bytes
data = f.read([maxbytes])
```

Para escribir un texto en el archivo:

```python
g.write('un texto')
```

Finalmente, hay que cerrar los archivos cuando terminamos de usarlos.

```python
f.close()
g.close()
```

Es importante cerrar adecuadamente los archivos y es bastante fácil olvidarse (puede que el programa termine y no se termine de guardar bien). Por eso, preferimos abrir los archivos con el comando `with` de la siguiente forma.

```python
with open(nombre_archivo, 'rt') as file:
    # Usá el archivo `file`
    ...comandos que usan el archivo
    # No hace falta cerrarlo explícitamente
...comandos que no usan el archivo
```

Esto cierra automáticamente el archivo cuando se termina de ejecutar el bloque indentado.

_Observación: En algunos sistemas operativos es probable que le tengas que especificar el_ encoding _agregando `encoding='utf8'` como parámetro al comando `open`. Algo tipo `open('foo.txt', 'rt', encoding='utf8')`._

### Comandos usuales para leer un archivo

Para leer un archivo entero, todo de una, como cadena:

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` es una cadena con *todo* el texto en `foo.txt`
```

Para leer línea por línea iterativamente:

```python
with open(nombre_archivo, 'rt') as file:
    for line in file:
        # Procesar la línea
```

### Comandos usuales para escribir un archivo

Para escribir cadenas:

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
```

También podés simplemente redireccionar la salida del print (de la pantalla a un archivo).

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...
```

## Ejercicios

Estos ejercicios usan el archivo `../Data/camion.csv`.  El archivo contiene una lista de líneas con información sobre los cajones de fruta cargados en un camión. Suponemos que estás trabajando en el directorio `ejercicios_python/Clase02` del curso. Si no estás segure, podés pedirle al Python que te diga dónde está trabajando con este comando:

```python
>>> import os
>>> os.getcwd()
'/Users/profe/Desktop/ejercicios_python/Clase02/' # La salida va a cambiar
>>>
```

### Ejercicio 2.1: Preliminares sobre lectura de archivos
Primero, tratá de leer el archivo entero de una en una larga cadena:

```python
>>> with open('../Data/camion.csv', 'rt') as f:
        data = f.read()

>>> data
'nombre,cajones,precio\n"Lima",100,32.20\n"Naranja",50,91.10\n"Caqui",150,83.44\n"Mandarina",200,51.23\n"Durazno",95,40.37\n"Mandarina",50,65.10\n"Naranja",100,70.44\n'
>>> print(data)
nombre,cajones,precio
"Lima",100,32.20
"Naranja",50,91.10
"Caqui",150,83.44
"Mandarina",200,51.23
"Durazno",95,40.37
"Mandarina",50,65.10
"Naranja",100,70.44
>>>
```

En el ejemplo de arriba podrás observar que Python tiene dos modos de salida. En el primero escribiste `data` en el intérprete y Python mostró la representación *cruda* de la cadena, incluyendo comillas y códigos de escape. Cuando escribiste `print(data)`, en cambio, obtuviste la salida formateada de la cadena.

Leer un archivo entero y cargarlo en memoria todo de una vez parece simple, pero sólo tiene ventajas si el archivo es pequeño. Si estás trabajando con archivos enormes es mejor procesar las líneas de tu archivo una a una.

Para leer un archivo línea por línea, usá un ciclo for como este:

```python
>>> with open('../Data/camion.csv', 'rt') as f:
        for line in f:
            print(line, end = '')

nombre,cajones,precio
"Lima",100,32.2
"Naranja",50,91.1
...
>>>
```

En ese código, las líneas son leídas una por una hasta el final del archivo, cuando el ciclo se termina.

En ciertas ocasiones, puede pasar que quieras leer una sola línea de texto (por ejemplo, querés saltearte la primera línea del archivo que contiene los nombres de las columnas).

```python
>>> f = open('../Data/camion.csv', 'rt')
>>> headers = next(f)
>>> headers
'nombre,cajones,precio\n'
>>> for line in f:
        print(line, end = '')

"Lima",100,32.20
"Naranja",50,91.10
...
>>> f.close()
>>>
```

El comando `next()` devuelve la siguiente línea de texto en el archivo. Sin embargo, sólo para que sepas, los ciclos `for` usan el método `next()` para obtener sus datos. Por lo tanto, típicamente no forzás un llamado extra a `next()` salvo que explícitamente quieras saltear o leer una línea particular como en nuestro caso de acá abajo.

Una vez que estés leyendo un archivo línea a línea, podés hacer otras operaciones, como separar los datos dentro de una línea con el método `split()`. Por ejemplo, probá esto:

```python
>>> f = open('../Data/camion.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['nombre', 'cajones', 'precio\n']
>>> for line in f:
        row = line.split(',')
        print(row)

['"Lima"', '100', '32.20\n']
['"Naranja"', '50', '91.10\n']
...
>>> f.close()
```

*Observación: En estos ejemplos tuvimos que llamar  a `f.close()` explícitamente porque no estamos trabajando con el comando `with`.*

*Otra observación: usamos `../Data` para acceder a la carpeta "Data" porque ésta se encuentra dentro de la carpeta "ejercicios_python", al igual que la carpeta actual de trabajo, que es "Clase02". Con los dos puntos del inicio del path nos referimos a la carpeta "madre", es decir, a la carpeta que contiene a la actual.*

### Ejercicio 2.2: Lectura de un archivo de datos
Ahora que sabés leer un archivo, escribamos un programa que haga un cálculo simple con los datos leídos.

Las columnas en `camion.csv` corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado `costo_camion.py`  que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

*Ayuda: para interpretar un string `s` como un número entero, usá `int(s)`. Para leerlo como punto flotante, usá `float(s)`.*

Tu programa debería imprimir una salida como la siguiente:

```bash
Costo total 47671.15
```

Acordate de guardar tu archivo en el directorio `Clase02`; vamos a volver a trabajar sobre él.

### Ejercicio 2.3: Precio de la naranja
El archivo `../Data/precios.csv` contiene una serie de líneas con precios de venta de cajones en el mercado al que va el camión. El archivo se ve así:

```csv
"Lima",40.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
"Frutilla",53.72
...
```

Escribí un código que abra el archivo `../Data/precios.csv`, busque el precio de la naranja y lo imprima en pantalla.

```python
>>> f = open('../Data/precios.csv', 'rt')
...
>>> f.close()

El precio de la naranja es:  106.28
```

### Ejercicio 2.4: Archivos comprimidos
¿Qué pasaría si quisiéramos leer un archivo comprimido con gzip, por ejemplo? La función primitiva de Python  `open()` no hace esa tarea. Pero hay un módulo de la biblioteca de Python llamado `gzip` que lee archivos comprimidos.

Probalo:

```python
>>> import gzip
>>> with gzip.open('../Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')

... mirá la salida ...
>>>
```

*Observación: La inclusión del modo  `'rt'` es crítica acá. Si te lo olvidás, vas a estar leyendo cadenas de bytes en lugar de cadenas de caracteres.*

### Comentario: ¿No deberíamos estar usando Pandas para esto?

Es frecuente que les estudiantes que conocen un poco más de Python rápidamente señalen que hay módulos como [Pandas](https://pandas.pydata.org) que tienen, entre muchas otras funcionalidades, la posibilidad de leer archivos CSV en una sola instrucción. Es verdad, y funcionan muy bien. Sin embargo, este no es un curso sobre Pandas. Si bien más adelante veremos algo de esta biblioteca, lo que nos interesa en este momento es aprender a manejar archivos directamente. Estamos trabajando con archivos CSV porque es un formato sencillo que es muy útil conocer, pero es principalmente una excusa para mostrar cómo Python maneja archivos de texto. En resumen, cuando tengas que trabajar con datos, definitivamente usá Pandas. Pero para aprender a manejar archivos vamos a seguir usando las funciones básicas de Python.

# 2.4 Funciones

A medida que tus programas se vuelven más largos y complejos, vas a necesitar organizarte. En esta sección vamos a introducir brevemente funciones y módulos de la biblioteca así como también la administración de errores y excepciones. 
Acá hay un [video introductorio](https://youtu.be/5OOqvYhf65A) al tema de funciones, y acá [hay otro](https://youtu.be/THUdN87afwg) sobre el manejo de errores y excepciones.

### Funciones a medida

Usá funciones para encapsular código que quieras reutilizar. El siguiente ejemplo muestra una definición de una función:

```python
def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

Para llamar a una función:

```python
a = sumcount(100)
```

Una función es una serie de instrucciones que realiza una tarea y devuelve un resultado. La palabra  `return` es necesaria para explicitar el valor de retorno de la función.

### Funciones de la biblioteca

Python trae una gran biblioteca estándar.
Los módulos de esta biblioteca se cargan usando `import`.
Por ejemplo:

```python
import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
```

Vamos a estudiar bibliotecas y módulos en detalle más adelante.

### Errores y excepciones

Las funciones informan los errores como excepciones. Dado que una excepción interrumpe la ejecución de una función, la misma puede generar que todo el programa se detenga si no es administrada adecuadamente.

Probá por ejemplo lo siguiente en tu intérprete:

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <módulo>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

Para poder entender qué pasó (debuguear), el mensaje describe cuál fue el problema, dónde ocurrió y un poco de la historia (traceback) de los llamados que terminaron en este error.

### Atrapar y administrar excepciones

Las excepciones pueden ser atrapadas y administradas.
Para atrapar una excepción, se usan los comandos `try - except`. Podés probar el siguiente fragmento de código pegándolo en un archivo [foo.py](https://es.wikipedia.org/wiki/Foo) :

```python
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
```

Si en este ejemplo le usuarie ingresa por ejemplo una letra, el comando `n = int(a)` genera una excepción de tipo `ValueError`: el comando `numero_valido = True` no se ejecuta, la excepción es atrapada por el `except ValueError` y el ciclo se repite. Probalo ingresando letras, números con decimales y números enteros. Probá también qué ocurre si querés salir sin ingresar nada generando una excepción presionando las teclas `Ctrl+C`. Leé el mensaje que describe lo ocurrido:  `Ctrl+C` genera una excepción de tipo `KeyboardInterrupt` que no es atrapada.

Si no especificamos el tipo de excepción que queremos atrapar, vamos a terminar atrapando todas la excepciones. Probá lo mismo que antes pero con este código.

```python
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
```

Deberías observar una diferencia: al presionar las teclas `Ctrl+C` la excepción `KeyboardInterrupt` sí es atrapada y no se termina el ciclo hasta no ingresar un número entero.

En general es difícil saber exactamente qué tipo de errores pueden ocurrir por adelantado. Para bien o para mal, la administración de excepciones suele ir creciendo a medida que un programa va generando errores inesperados (al mejor estilo: "Uh! Me olvidé de que podía pasar esto. Deberíamos preverlo y administrarlo adecuadamente para la próxima").

### Generar excepciones

Para generar una excepción (también diremos *levantar* una excepción, porque es más cercano al término inglés "raise"), se usa el comando `raise`. Por ejemplo, si tenemos el siguiente código en el archivo `foo.py`:

```python
raise RuntimeError('¡Qué moco!')
```

Al correrlo va a detener la ejecución y permite rastrear la excepción leyendo el mensaje de error que imprime.

```bash
bash $ python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <módulo>
    raise RuntimeError("¡Qué moco!")
RuntimeError: ¡Qué moco!
```

Alternativamente, esa excepción puede ser atrapada por un bloque `try-except`, pudiendo de esta forma evitar que el programa termine. Te dejamos un [video](https://youtu.be/9kUzd2Sk8WE) que repasa estos ejemplos.

## Ejercicios

### Ejercicio 2.5: Definir una función
Probá primero definir una función simple:

```python
>>> def saludar(nombre):
        'Saluda a alguien'
        print('Hola', nombre)

>>> saludar('Guido')
Hola Guido
>>> saludar('Paula')
Hola Paula
>>>
```

Si la primera instrucción de una función es una cadena, sirve como documentación de la función. Probalo escribiendo `help(saludar)` para ver cómo la muestra.

### Ejercicio 2.6: Transformar un script en una función
Transformá el programa `costo_camion.py`  (que escribiste en el [Ejercicio 2.2](../02_Estructuras_y_Funciones/03_Archivos.md#ejercicio-22-lectura-de-un-archivo-de-datos) de la sección anterior) en una función `costo_camion(nombre_archivo)`.  Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante.

Para usar tu función, cambiá el programa de forma que se parezca a esto:

```python
def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
```

Cuando ejecutás tu programa, deberías ver la misma salida impresa que antes. Una vez que lo hayas corrido, podés llamar interactivamente a la función escribiendo esto:

```bash
bash $ python3 -i costo_camion.py
```

Esto va a ejecutar el código en el programa y dejar abierto el intérprete interactivo.

```python
>>> costo_camion('../Data/camion.csv')
47671.15
>>>
```

Es útil para testear y debuguear poder interactuar interactivamente con tu código.


### Ejercicio 2.7: Buscar precios
A partir de lo que hiciste en el [Ejercicio 2.3](../02_Estructuras_y_Funciones/03_Archivos.md#ejercicio-23-precio-de-la-naranja), escribí una función `buscar_precio(fruta)` que busque en archivo `../Data/precios.csv` el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.


```python
>>> buscar_precio('Frambuesa')
El precio de un cajón de Frambuesa es: 34.35
>>> buscar_precio('Kale')
Kale no figura en el listado de precios.
```

Guardá este código en un archivo `buscar_precios.py` para entregar al final de la clase.

Acá te dejamos un [video](https://youtu.be/urLFDsfXsug) en el que resolvemos un ejercicio similar al [Ejercicio 2.7](../02_Estructuras_y_Funciones/04_Funciones.md#ejercicio-27-buscar-precios) de diferentes formas, usando for y usando while.

### Ejercicio 2.8: Administración de errores
Este ejercicio introduce el tema de administración de errores. Es un tema un poco avanzado. No te inquietes si no entendés aún en profundidad estos conceptos, los vamos a retomar más adelante y en otras materias. Simplemente nos parece que está bueno empezar desde temprano a hablar de estos temas.

Probá correr la siguiente función ingresando tu edad real, una edad escrita con letras (como "ocho") y una edad negativa (-3):

```python
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad
```

Ahora probá este ejemplo que atrapa la excepción generada con `raise` y continúa la ejecución con la siguiente persona.

```python
for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')
```

Vamos a usar estas ideas aplicadas al procesamiento de un archivo CSV. ¿Qué pasa si intentás usar la función `costo_camion()` con un archivo que tiene datos faltantes?

```python
>>> costo_camion('../Data/missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <módulo>
    File "costo_camion.py", line 11, in costo_camion
    ncajones = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

El programa termina con un error. A esta altura tenés que tomar una decisión. Para que el programa funcione podés editar el archivo CSV de entrada de manera de corregirlo (borrando líneas o adecuando la información) o podés modificar el código para que maneje las líneas *incorrectas* de  alguna manera.

Modificá el programa `costo_camion.py` para que atrape la excepción con un bloque `try - except`, imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.

Vamos a retomar el tema de administración de errores en las próximas clases. Es normal que te quede una sensación de que no se entiende del todo. Nos faltan varias piezas para armar el rompecabezas.

### Ejercicio 2.9: Funciones de la biblioteca
Python viene con una gran biblioteca estándar de funciones útiles. En este caso el módulo `csv` podría venirnos muy bien. Podés usarlo cada vez que tengas que leer archivos CSV. Acá va un ejemplo de cómo funciona.

```python
>>> import csv
>>> f = open('../Data/camion.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['nombre', 'cajones', 'precio']
>>> for row in rows:
        print(row)

['Lima', '100', '32.2']
['Naranja', '50', '91.1']
['Caqui', '150', '103.44']
['Mandarina', '200', '51.23']
['Durazno', '95', '40.37']
['Mandarina', '50', '65.1']
['Naranja', '100', '70.44']
>>> f.close()
>>>
```

Una cosa buena que tiene el módulo `csv` es que maneja solo una gran variedad de detalles de bajo nivel como el problema de las comillas, o la separación con comas de los datos. En la salida del último ejemplo podés ver que el lector ya sacó las comillas dobles de los nombres de las frutas de la primera columna.


Modificá tu programa `costo_camion.py` para que use el módulo `csv` para leer los archivos CSV y probalo en un par de los ejemplos anteriores.

Ahora que viste funciones, te dejamos un [video](https://youtu.be/3QNtSWBqQwk) en el que repasamos el [Ejercicio 1.29](../01_Intro_a_Python/07_Listas.md#ejercicio-129-traductor-rustico-al-lenguaje-inclusivo) de lenguaje inclusivo usando una función.


# 2.5 Tipos y estructuras de datos

Esta sección introduce dos estructuras de datos elementales: las tuplas y los diccionarios.

### Tipos de datos primitivos

Python tiene pocos tipos primitivos de datos.

* Números enteros
* Números de punto flotante
* Cadenas de texto

Algo ya sabemos sobre estos tipos de datos por la clase anterior.

### Tipo None

```python
email_address = None
```

`None` suele utilizarse como un comodín para reservar el lugar para un valor opcional o faltante. En los condicionales, evalúa como `False`.

```python
if email_address:
    send_email(email_address, msg)
```

### Estructuras de datos

Los programas reales tienen datos más complejos que los que podemos almacenar en los tipos primitivos. Por ejemplo, información sobre un pedido de frutas:

```code
100 cajones de Manzanas a $490.10 cada uno
```

Podemos ver esto como un "objeto" con tres partes:

* Nombre de la mercancía ("Manzanas", una cadena)
* Número o cantidad (100, un entero)
* Precio (490.10, un flotante)

### Tuplas

Una tupla es una colección con valores agrupados juntos.

Ejemplo:

```python
s = ('Manzanas', 100, 490.1)
```

Las tuplas suelen usarse para representar registros o estructuras *simples*.
Típicamente, una tupla representa un solo *objeto* con múltiples partes. Una analogía posible es la siguiente: *Una tupla es como una fila de una base de datos*.

Los contenidos de una tupla están ordenados (como en una lista).

```python
s = ('Manzana', 100, 490.1)
nombre = s[0]                   # 'Manzana'
cantidad = s[1]                 # 100
precio = s[2]                   # 490.1
```

El contenido de las tuplas no puede ser modificado.

```python
>>> s[1] = 75
TypeError: object does not support item assignment
```

Podés, sin embargo, hacer una nueva tupla basada en el contenido de otra, que no es lo mismo que modificar el contenido.

```python
s = (s[0], 75, s[2])
```

#### Empaquetar tuplas

Las tuplas suelen usarse para empaquetar información relacionada en una sola *entidad*.

```python
s = ('Manzanas', 100, 490.1)
```

Una tupla puede ser pasada de un lugar a otro de un programa como un solo objeto.

#### Desempaquetar tuplas

Para usar una tupla en otro lado, debemos desempaquetar su contenido en diferentes variables.

```python
fruta, cajones, precio = s
print('Costo:', cajones * precio)
```

El número de variables a la izquierda debe ser consistente con la estructura de la tupla.

```python
nombre, cajones = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```

### Tuplas vs. Listas

Las tuplas parecieran ser listas de solo-lectura. Sin embargo, las tuplas suelen usarse para un solo ítem que consiste de múltiples partes mientras que las listas suelen usarse para una colección de diferentes elementos, típicamente del mismo tipo.

```python
record = ('Manzanas', 100, 490.1)                # Una tupla representando un registro dentro de un pedido de frutas

symbols = [ 'Manzanas', 'Peras', 'Mandarinas' ]  # Una lista representando tres frutas diferentes.
```

### Diccionarios

Un diccionario es una función que manda *claves* en *valores*. Las claves sirven como índices para acceder a los valores.

```python
s = {
    'fruta': 'Manzana',
    'cajones': 100,
    'precio': 490.1
}
```

#### Operaciones usuales

Para obtener el valor almacenado en un diccionario usamos las claves.

```python
>>> print(s['fruta'], s['cajones'])
Manzanas 100
>>> s['precio']
490.10
>>>
```

Para agregar o modificar valores, simplemente asignamos usando la clave.

```python
>>> s['cajones'] = 75
>>> s['fecha'] = '6/8/2020'
>>>
```

para borrar un valor, usamos el comando `del`.

```python
>>> del s['fecha']
>>>
```

#### ¿Por qué diccionarios?

Los diccionarios son útiles cuando hay *muchos* valores diferentes y esos valores pueden ser modificados o manipulados. Dado que el acceso a los elementos se hace por *clave*, no es necesario recordar una posición para cierto dato, lo que muchas veces cumple un objetivo fundamental: hacer que el código sea más legible (y con esto menos propenso a errores).

```python
s['precio'] # diccionario
# vs
s[2] # lista
```

## Ejercicios

Anteriormente escribiste un programa que leía el archivo
`camion.csv` usando el módulo `csv` para leer el archivo fila por fila.

```python
>>> import csv
>>> f = open('../Data/camion.csv')
>>> filas = csv.reader(f)
>>> next(filas)
['nombre', 'cajones', 'precio']
>>> fila = next(filas)
>>> fila
['Lima', '100', '32.2']
>>>
```

A veces, además de leerlo, queremos hacer otras cosas con el archivo CSV, como por ejemplo usar los datos que contiene para hacer un cálculo. Lamentablemente una fila de datos en crudo no es suficiente para operar aritméticamente. Vamos a querer interpretar los elementos de la fila de datos de alguna manera particular, convirtiéndolos a otro tipo de datos que resulte más adecuado para trabajar. Es frecuente además de convertir los elementos de las filas, transformar las filas enteras en tuplas o diccionarios.

### Ejercicio 2.10: Tuplas
En el intérprete interactivo, creá la siguiente tupla que representa la fila de antes, pero con las columnas numéricas pasadas a formatos adecuados:

```python
>>> t = (fila[0], int(fila[1]), float(fila[2]))
>>> t
('Lima', 100, 32.2)
>>>
```

A partir de esta tupla, ahora podés calcular el costo total multiplicando cajones por precio:

```python
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

¿Qué pasó? ¿Qué hace ese 5 al final?

Este error no es un problema de Python, sino de la forma en la que la máquina representa los números de punto flotante. Así como en base 10 no podemos escribir un tercio de manera exacta, en base 2 escribir un quinto requiere infinitos dígitos. Al usar una representación finita (una cantidad acotada de dígitos) la máquina redondea los números. La aritmética de punto flotante no es exacta.

Esto pasa en todos los lenguajes de programación que usan punto flotante, pero en muchos casos estos pequeños errores quedan ocultos al imprimir. Por ejemplo:

```python
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Las tuplas son de sólo lectura. Verificalo tratando de cambiar el número de cajones a 75.

```python
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Aunque no podés cambiar al tupla, sí podés reemplazar la tupla por una nueva.

```python
>>> t = (t[0], 75, t[2])
>>> t
('Lima', 75, 32.2)
>>>
```

Siempre que reasignes una variable como recién lo hiciste con `t`, el valor anterior de la variable se pierde. Aunque la asignación de arriba pueda parecer como que estás modificando la tupla, en realidad estás creando una nueva tupla y tirando la vieja.

Las tuplas muchas veces se usan para empaquetar y desempaquetar valores dentro de variables. Probá esto:

```python
>>> nombre, cajones, precio = t
>>> nombre
'Lima'
>>> cajones
75
>>> precio
32.2
>>>
```

Tomá las variables de arriba y empaquetalas en una tupla.

```python
>>> t = (nombre, 2*cajones, precio)
>>> t
('Lima', 150, 32.2)
>>>
```

### Ejercicio 2.11: Diccionarios como estructuras de datos
Una alternativa a la tupla es un diccionario.

```python
>>> d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }
>>> d
{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2 }
>>>
```

Calculá el costo total de este lote:

```python
>>> cost = d['cajones'] * d['precio']
>>> cost
3220.0000000000005
>>>
```

Compará este ejemplo con el mismo cálculo hecho con tuplas más arriba. Cambiá el número de cajones a 75.

```python
>>> d['cajones'] = 75
>>> d
{'nombre': 'Lima', 'cajones': 75, 'precio': 32.2 }
>>>
```

A diferencia de las tuplas, los diccionarios se pueden modificar libremente. Agregá algunos atributos:

```python
>>> d['fecha'] = (14, 8, 2020)
>>> d['cuenta'] = 12345
>>> d
{'nombre': 'Lima', 'cajones': 75, 'precio':32.2, 'fecha': (14, 8, 2020), 'cuenta': 12345}
>>>
```

### Ejercicio 2.12: Más operaciones con diccionarios
Si usás el comando `for` para iterar sobre el diccionario, obtenés las claves:

```python
>>> for k in d:
        print('k =', k)

k = nombre
k = cajones
k = precio
k = fecha
k = cuenta
>>>
```

Probá esta variante:

```python
>>> for k in d:
        print(k, '=', d[k])

nombre = 'Lima'
cajones = 75
precio = 32.2
fecha = (14, 8, 2020)
cuenta = 12345
>>>
```

Una manera más elegante de trabajar con claves y valores simultáneamente es usar el método `items()`. Esto te devuelve una lista de tuplas de la forma `(clave,valor)` sobre la que podés iterar.

```python
>>> items = d.items()
>>> items
dict_items([('nombre', 'Lima'), ('cajones', 75), ('precio', 32.2), ('fecha', (14, 8, 2020))])
>>> for k, v in d.items():
        print(k, '=', v)

nombre = Lima
cajones = 75
precio = 32.2
fecha = (14, 8, 2020)
>>>
```

Si pasás un diccionario a una lista, obtenés sus claves.

```python
>>> list(d)
['nombre', 'cajones', 'precio', 'fecha', 'cuenta']
>>>
```

También podés obtener todas las claves del diccionario usando el método `keys()`:

```python
>>> claves = d.keys()
>>> claves
dict_keys(['nombre', 'cajones', 'precio', 'fecha', 'cuenta'])
>>>
```

Si tenés tuplas como en `items` podés crear un diccionario usando la función `dict()`. Probá esto:

```python
>>> nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
>>> nuevos_items
[('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
>>> d = dict(nuevos_items)
>>> d
{'nombre': 'Manzanas', 'cajones': 100, 'precio': 490.1, 'fecha': (13, 8, 2020)}
```


### Ejercicio 2.13: Diccionario geringoso.
Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso (como en el [Ejercicio 1.18](../01_Intro_a_Python/06_Strings.md#ejercicio-118-geringoso-rustico)). 
Probá tu función para la lista `['banana', 'manzana', 'mandarina']`.
Guardá este ejercicio en un archivo `diccionario_geringoso.py` para entregar al final de la clase.

# 2.6 Cierre de la clase

En esta clase comenzamos a trabajar con funciones y estructuras de datos.

Te recordamos que leas el [código de honor](../Codigo.md) del curso en el que hablamos de las reglas que rigen en este curso para evitar el plagio así como otros aspectos importantes sobre qué se puede compartir y qué no. Como todas las semanas, te vamos a pedir que envies tus ejercicios resueltos por mail. Recordá usar siempre la misma dirección de mail y poner como *subject* del correo **[Unidad 2]**. 

Recordá: Si cursás en el turno de los miércoles, mandá tus ejercicios a python@unsam.edu.ar, si cursás en el turno de los jueves mandalos a pythonunsam@gmail.com.


* Los ejercicios a enviar esta semana son:
    1. El archivo `buscar_precios.py` del [Ejercicio 2.7](../02_Estructuras_y_Funciones/04_Funciones.md#ejercicio-27-buscar-precios).
    2. El archivo `costo_camion.py` del [Ejercicio 2.9](../02_Estructuras_y_Funciones/04_Funciones.md#ejercicio-29-funciones-de-la-biblioteca).
    3. El archivo `diccionario_geringoso.py` del [Ejercicio 2.13](../02_Estructuras_y_Funciones/05_TiposDatos.md#ejercicio-213-diccionario-geringoso).
    

Observación: Si el enunciado de un ejercicio te pide que lo corras con un input particular, por favor poné la salida que obtuviste como comentario en tu código. 



