#Crear un archivo .py , escribir un Hola mundo que se imprima en consola.
print("Hola mundo")

# Escribir un programa que salude con el nombre de entrada desde teclado
nombre= input("Escribe tu nombre: ")
print("Hola, "+ nombre)

# Escribe un programa que pida tu edad y muestre si es mayor de edad o no lo es.
edad = int(input("Ingresa tu edad: "))  
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Escribe un programa que pida un numero entero y determine si es par o impar 

numero= int(input("Escribe un nuemro entero: "))

if numero%2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
    
#Escribe un programa que que pida un numero entero y calcule la suma de 1 hasta el
# numero ingresado .

#1.-Usando la formula
numero = int(input("Por favor, ingresa un número entero positivo: "))

if numero < 1:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Calcular la suma usando la fórmula
    suma = (numero * (numero + 1)) // 2
    print(f"La suma de los números de 1 hasta {numero} es: {suma}")

#2.-Usando un bucle for

n=100
suma1=0
for i in range(1, n+1):
    suma1+=i
    
print (suma1)




