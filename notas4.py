### Ciclos en Python###
##Ejemplos##
# 1. Almacenaremos el número más grande actual aquí
numero Mayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
 while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int (input("Introduce un número o escribe -1 para detener:"))

# Imprimir el número más grande
print("El número más grande es:", numeroMayor)

#2. # programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))

# 0 termina la ejecución
while numero != 0:
    # verificar si el número es impar
    if numero % 2 == 1:
        # aumentar el contador de números impares
        numerosImpares += 1
    else:
        # aumentar el contador de números pares
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)

#Laboratorio1
###Escenario###
#Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada númeroSecreto. Quiere que todos los que ejecutan su programa jueguen el juego 
#Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quienes no adivinen el número quedarán atrapados en un ciclo sin fin para siempre! 
#Desafortunadamente, él no sabe cómo completar el código.

#Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

#Pedirá al usuario que ingrese un número entero.
#Utilizará un ciclo while.
#Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto 
#del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi ciclo!"  y se le solicitará que ingrese un número nuevamente. Si el número ingresado por 
#el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras:
# "¡Bien hecho, muggle! Eres libre ahora".

numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numero=int(input("Ingresa el número secreto: "))
while numero != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero=int(input("Ingresa nuevamente el número secreto: "))
print("¡Bien hecho, muggle! Eres libre ahora")

#Potencias de 2
for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)
    
for i in range(1, 1):
    print("El valor de i es actualmente", i) 
    
pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2 

#Laboratorio 2

#Tu tarea es muy simple aquí: escribe un programa que use un ciclo for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, 
#el programa debería imprimir en la pantalla el mensaje final "¡Listo o no, ahí voy!"

import time

for i in range(1,6):
    print(i,"Mississipi")
    i+= 1
    time.sleep(1)
    
print("¡Listo o no, ahí voy!")

#Break y continue

# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

#Otro ejemplo con Break 

numeroMayor = -99999999
contador = 0

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador = 1
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 


#Otro ejemplo con Continue

numeroMayor = -99999999
contador = 0

numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

while numero != -1:
    if numero == -1:
        continue
    contador = 1

    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

if contador:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número")

#Laboratorio 3#
#Escenario
#La instrucción break se usa para salir/terminar un ciclo.

#Diseña un programa que use un ciclo while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra 
#de salida secreta, en cuyo caso el mensaje "¡Has dejado el ciclo con éxito". Debe imprimirse en la pantalla y el ciclo debe terminar.

#No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la declaración break.

palabraSecreta="chupacabra"
palabra=input("Ingrese la palabra secreta: ")

while True:
    if palabra==palabraSecreta:
        break
    palabra=input("Ingrese la palabra secreta: ")
    
print("¡Has dejado el ciclo con éxito!")

#Laboratorio 4

#Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

#-Un ciclo for.
#-El concepto de ejecución condicional (if-elif-else).
#-La declaración continue.

#Tu programa debe:

#Pedir al usuario que ingrese una palabra.
#Utiliza userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
#hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
#Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
#Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.

# Indicar al usuario que ingrese una palabra
palabra=input("Señor usuario, ingrese su palabra: ")
palabra= palabra.upper()


for letra in palabra:
    if letra=="A":
        continue
    elif letra=="E":
        continue
    elif letra=="I":
        continue
    elif letra=="O":
        continue
    elif letra=="U":
        continue
    else:
        print(letra)

#Laboratorio 5

#Basado en el devorador de vocales del programa anterior:
#Tu programa debe:

#Pedir al usuario que ingrese una palabra.
#Utilizar userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y 
#el upper() muy pronto, no te preocupes.
#Usa la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
#Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable en la pantalla.
#Analiza el código en el editor. Hemos creado palabrasinVocal y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python 
#que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de ciclo, y asignarlo a la variable palabrasinVocal.

palabraSinVocal = ""
palabra=input("Señor usuario, ingrese su palabra: ")
palabra= palabra.upper()


for letra in palabra:
    if letra=="A":
        continue
    elif letra=="E":
        continue
    elif letra=="I":
        continue
    elif letra=="O":
        continue
    elif letra=="U":
        continue
    else:
        palabraSinVocal+=letra
        
print(palabraSinVocal)



