pruebas= int(input("Escriba la cantidad de Pruebas: "))
prueba1= int(input("Nota de la prueba 1: "))
prueba2= int(input("Nota de la prueba 2: "))
prueba3= int(input("Nota de la prueba 3: "))

sumapromedio= prueba1+prueba2+prueba3
promedio= sumapromedio/3

print ("El promedio obtenido es: ",promedio)
if promedio<=60:
    print ("El estudiante esta reprobado")
elif promedio<=70 and promedio>60:
    print("EL estudiante tiene derecho a ampliación")
else:
    print("El estudiante esta Aprobado")