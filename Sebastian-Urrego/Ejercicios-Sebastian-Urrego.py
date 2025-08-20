# Nombre: Sebastian Urrego Ochoa
# Descripción: Ejercicios de Condicionales, ciclos y colecciones en Python


# Condicionales
print ("---Ejercicios de Condicionales---")

#Ejercicio 1 numeros positivos o negativos

num = int (input("Ingresa un numero: "))
if num > 0:
    print("Es positivo")
elif num < 0:
    print ("Es negativo")
else:
    print("Es cero")
    

#Ejercicio 2 Mayor de edad

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Ejercicio 3 Numero par o impar
num = int(input("Ingresa un numero: "))
if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#Ejercicio : Clasificacion de notas
nota = int(input("Ingresa tu nota (0-100): "))
if nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")

#Ejercicio 5 Menor de tres nnmeros
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))
c = int(input("Tercer numero: "))
if a <= b and a <= c:
    print("El menor es:", a)
elif b <= a and b <= c:
    print("El menor es:", b)
else:
    print("El menor es:", c)


#Ciclos For
print("\n=== Ejercicios de Ciclos For ===")

#Ejercicio 1 Imprimir del 1 al 10
for i in range(1, 11):
    print(i)

#Ejercicio 2 Tabla de multiplicar
num = int(input("Numero: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#Ejercicio 3 Suma de los primeros 5 numeros
suma = 0
for i in range(1, 6):
    suma += i
print("La suma es:", suma)

#Ejercicio 4 Contar vocales en una palabra
palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print("Cantidad de vocales:", contador)

#Ejercicio 5 Imprimir una lista
frutas = ["manzana", "pera", "uva", "plátano"]
for fruta in frutas:
    print(fruta)


#Ciclos While 
print("\n=== Ejercicios de Ciclos While ===")

#Ejercicio 1 Contar hasta 10
i = 1
while i <= 10:
    print(i)
    i += 1

#Ejercicio 2 Contraseña correcta
password = ""
while password != "python123":
    password = input("Ingresa la contraseña: ")
print("¡Acceso concedido!")

#Ejercicio 3 Suma acumulada
suma = 0
num = int(input("Ingresa un numero (0 para salir): "))
while num != 0:
    suma += num
    num = int(input("Ingresa otro numero (0 para salir): "))
print("La suma total es:", suma)

#Ejercicio 4 Adivina el numero
secreto = 7
num = int(input("Adivina el numero (1-10): "))
while num != secreto:
    print("Incorrecto, intenta otra vez.")
    num = int(input("Adivina el numero (1-10): "))
print("¡Correcto! El numero era", secreto)

#Ejercicio 5 Cuenta regresiva
num = int(input("Ingresa un numero: "))
while num >= 0:
    print(num)
    num -= 1