#Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo

frase = 'todos somos programadores'
palabras = frase.split()
inclusivas = []
for palabra in palabras:
    if palabra[-1] == 'o':
        inclusiva = palabra[:-1] + 'e'
        inclusivas.append(inclusiva)
    elif palabra[-2] == 'o':
        inclusiva = palabra[:-2] + 'e' + palabra[-1]
        inclusivas.append(inclusiva)
    else:
        inclusivas.append(palabra)

    
frase_t = ' '.join(inclusivas)
print(frase_t)


frase = 'Los hermanos sean unidos porque ésa es la ley primera'
palabras = frase.split()
inclusivas = []
for palabra in palabras:
    if palabra[-1] == 'o':
        inclusiva = palabra[:-1] + 'e'
        inclusivas.append(inclusiva)
    elif palabra[-2] == 'o':
        inclusiva = palabra[:-2] + 'e' + palabra[-1]
        inclusivas.append(inclusiva)
    else:
        inclusivas.append(palabra)

    
frase_t = ' '.join(inclusivas)
print(frase_t) 


frase = '¿cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split()
inclusivas = []
for palabra in palabras:
    if len(palabra) >= 2: 
        if palabra[-1] == 'o':
            inclusiva = palabra[:-1] + 'e'
            inclusivas.append(inclusiva)
        elif palabra[-2] == 'o':
            inclusiva = palabra[:-2] + 'e' + palabra[-1]
            inclusivas.append(inclusiva)
        else:
            inclusivas.append(palabra)
    else:
        inclusivas.append(palabra)

    
frase_t = ' '.join(inclusivas)
print(frase_t) 



frase = 'Todos, tu también'
palabras = frase.split()
palabras                  # el problema es que cuenta la coma despues de Todos.
inclusivas = []
for palabra in palabras:
    if len(palabra) >= 2: 
        if palabra[-1] == 'o':
            inclusiva = palabra[:-1] + 'e'
            inclusivas.append(inclusiva)
        elif palabra[-2] == 'o':
            inclusiva = palabra[:-2] + 'e' + palabra[-1]
            inclusivas.append(inclusiva)
        else:
            inclusivas.append(palabra)
    else:
        inclusivas.append(palabra)

    
frase_t = ' '.join(inclusivas)
print(frase_t) 




