#Ejercicio 1
print("\"Estoy\"")
print('"""aprendiendo"""')
print("\"\"\"Python\"\"\"")


#Operadores aritméticos: Dvisión entera

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

#Ejerciico 3 
juan=3
maria=5
adan=6
print(juan,maria, adan)
total_manzanas= juan+maria+adan
print("Número total de manzanas: " ,total_manzanas)

#Ejerecicio4

kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas*1.61###
kilometros_a_millas = kilometros/1.61###

print(millas, " millas son ", round(millas_a_kilometros, 7), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 4), " millas ")

#Ejercicio 5

x = 0
x = float(x)


y= (3*(x**3))- (2*(x**2))+(3*x)-1
print("y =", y)

x = 1
x = float(x)
y =  (3*(x**3))- (2*(x**2))+(3*x)-1
print("y =", y)

x = -1
x = float(x)
y =  (3*(x**3))- (2*(x**2))+(3*x)-1
print("y =", y)

# Esta programa calcula la hipotenusa (c)
# a y b son las longitudes de los catetos
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5 # se utiliza ** en lugar de la raíz cuadrada
print("c =", c)

#Concatebar cadenas 2.1.6.6
x= "Hola, amigo, "
y= "¿cómo estàs?"
z=x+y
print(z)

nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

#Rectángulo
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Laboratorio. Entradas y salidas simples
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))

print("La suma de los dos números es: "+str(a+b)) 
# muestra el resultado de la resta aquí
print("La resta de los dos números es: "+str(a-b))
# muestra el resultado de la multiplicación aquí
print("La multiplicación de los dos números es: "+str(a*b))
# muestra el resultado de la división aquí
print("El resultado de la división entre los dos números es: "+str(a//b))

print("\n¡Eso es todo, amigos!")

#Laboratorio.Operadores y expresiones

x = float(input("Ingresa el valor para x: "))

# coloca tu código aquí
y=(1/(x+(1/(x+(1/(x+(1/x)))))))

print("y =", y)

#Laboratorio2. Operadores y expresiones
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
min = min + dura # encuentra el total de minutos
hora = hora + min // 60 # encuentra el número de horas ocultos en los minutos y actualiza las horas
min = min % 60 # corrige los minutos para que estén en un rango de (0..59)
hora = hora % 24 # corrige las horas para que estén en un rango de (0..23)
print(hora, ":", min, sep='')
