#Ejercicio 1.18: Geringoso rústico
cadena = "Geringoso"
capadepenapa = ''
for c in cadena:
        if c in 'aeiou':
            capadepenapa += c + 'p' + c
        else:
            capadepenapa +=  c

print(capadepenapa)

cadena2 = "GERINGOSO"
capadepenapa2 = ''
for c in cadena2:
        if c in 'aeiouAEIOU':
            capadepenapa2 += c + 'p' + c
        else:
            capadepenapa2 +=  c

print(capadepenapa2)
