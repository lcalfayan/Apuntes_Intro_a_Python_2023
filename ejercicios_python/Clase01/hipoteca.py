# Ejercicio 1.7: La hipoteca de David
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))


#Ejercicio 1.8: Adelantos
saldo = 500000.0
tasa = 0.05
total_pagado = 0.0
mes=1

while saldo > 0: 
    if mes <= 12:
        pago_mensual =3684.11
        total_pagado = round(total_pagado + pago_mensual, 2)
        print(mes, round(saldo,2), pago_mensual, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual
        mes=mes+1
        
    else:
        pago_mensual = 2684.11
        total_pagado = round(total_pagado + pago_mensual, 2)
        print(mes, round(saldo,2), pago_mensual, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual
        mes=mes+1   

print('Total pagado', round(total_pagado, 2))
print('Cant. meses requeridos', mes-1)


#Ejercicio 1.9: Calculadora de adelantos
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=1

pago_extra_mes_comienzo = 61 #comienzo del 6to año
pago_extra_mes_fin = 108     #fin del 9no año
pago_extra = 1000

while saldo > 0: 
    if mes <= 12:
        pago_mensual12 = pago_mensual + pago_extra
        total_pagado = round(total_pagado + pago_mensual12, 2)
        print(mes, round(saldo,2), pago_mensual12, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual12
        mes=mes+1
    elif (mes >= pago_extra_mes_comienzo) and (mes <=pago_extra_mes_fin):
        pago_mensual_6_9 = pago_mensual + pago_extra
        total_pagado = round(total_pagado + pago_mensual_6_9, 2)
        print(mes, round(saldo,2), pago_mensual_6_9, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual_6_9
        mes=mes+1
        
    else:
        pago_mensual = pago_mensual
        total_pagado = round(total_pagado + pago_mensual, 2)
        print(mes, round(saldo,2), pago_mensual, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual
        mes=mes+1   

print('Total pagado', round(total_pagado, 2))
print('Cant. meses requeridos', mes-1)
total_pagado_exacto= total_pagado - saldo

#Ejercicio 1.11: Hipoteca ajustado
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=1

pago_extra_mes_comienzo = 61 #comienzo del 6to año
pago_extra_mes_fin = 108     #fin del 9no año
pago_extra = 1000

while saldo > 0: 
    if mes <= 12:
        pago_mensual12 = pago_mensual + pago_extra
        total_pagado = round(total_pagado + pago_mensual12, 2)
        print(mes, round(saldo,2), pago_mensual12, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual12
        mes=mes+1
    elif (mes >= pago_extra_mes_comienzo) and (mes <=pago_extra_mes_fin):
        pago_mensual_6_9 = pago_mensual + pago_extra
        total_pagado = round(total_pagado + pago_mensual_6_9, 2)
        print(mes, round(saldo,2), pago_mensual_6_9, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual_6_9
        mes=mes+1
        
    else:
        pago_mensual = pago_mensual
        total_pagado = round(total_pagado + pago_mensual, 2)
        print(mes, round(saldo,2), pago_mensual, total_pagado)
        saldo = saldo * (1+tasa/12) - pago_mensual
        mes=mes+1   

print('Total pagado', round(total_pagado, 2))
print('Cant. meses requeridos', mes-1)
total_pagado_exacto= total_pagado - pago_mensual + saldo
print('total pagado exacto', round(total_pagado_exacto,2))

exacto = round(total_pagado_exacto,2)
mes = mes-1

f'David pagó ${exacto} en {mes} meses'



