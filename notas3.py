#Módulo 3
#Laboratorio 1
n=int(input("Escribe un número: "))
print(n>=100)

#Ejemplo 
#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande

#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#Laboratorio 2
#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

#Imprima el enunciado "Si, ¡El Espatifilo es la mejor planta de todos los tiempos!"  en la pantalla si la cadena ingresada es "Espatifilo".
#Imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo".
#Imprima  "¡Espatifilo! ¡No [entrada]!"  de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.


entrada=input()
if entrada=="Espatifilo":
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif entrada=="espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo! ¡No "+entrada+ "!")

#Laboratorio3
#Escenario
#Érase una vez una tierra - una tierra de leche y miel, habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto, su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

#Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).
#Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
#Tu tarea es escribir una calculadora de impuestos.

#Debe aceptar un valor de punto flotante: el ingreso.
#A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti, la encontrarás en el código de esqueleto del editor.
#Nota: Este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.


ingreso = float(input("Ingresa el ingreso anual:"))

if ingreso < 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - 85528) * 0.32 + 14839.02

if impuesto < 0.0:
    impuesto = 0.0

impuesto=round(impuesto, 0)

print("El impuesto es: ", impuesto, "pesos")

#####Laboratorio 4
#Escenario
#Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común . Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

#Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

#Si el número del año no es divisible entre cuatro, es un año común.
#De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
#De lo contrario, si el número del año no es divisible entre 400, es un año común.
#De lo contrario, es un año bisiesto.
#Observa el código en el editor: solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.

#El código debe mostrar uno de los dos mensajes posibles, que son Año bisiesto o Año común, según el valor ingresado.

#Sería bueno verificar si el año ingresado cae en la era gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario gregoriano. Consejo: utiliza los operadores != y %.

año = int(input("Introduzca un año:"))

# Coloca tu código aquí.
if año<1582:
    print("No dentro del período del calendario gregoriano")
elif año%4!=0:
    print("Año común")
elif año%100!=0:
    print("Año bisiesto")
elif año%400!=0:
    print("Año común")
else:
    print("Año bisiesto")

