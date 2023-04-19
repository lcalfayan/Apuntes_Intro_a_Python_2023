# Ejercicio 1.5: La pelota que rebota
i=0        #cantidad de rebotes de la pelota
altura=100 # altura en metros

while altura >=0.1:
	print(i, altura)
	i=i+1
	altura=round(3/5*altura,2)
	
print("Finalización")
print("n rebotes:",i)
print("altura (m):", altura)	
	

