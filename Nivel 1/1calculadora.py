# Calculadora básica (suma, resta, multiplicación, división).

print('Calculadora Básica')

def mostrarmenu():
    print('1-suma')
    print('2-resta')
    print('3-multiplicación')
    print('4-división')
    print('5-salir')

def suma(a,b):
    resultado = a+b
    print(resultado)

def resta(a,b):
    resultado = a-b
    print(resultado)

def multiplicacion(a,b):
    resultado = a*b
    print(resultado)

def division(a,b):
    resultado = a/b
    print(resultado)

while True:
    mostrarmenu()
    opcion = input('Digite operación a realizar')

    if opcion in ['1', '2', '3', '4', '5']:

        if opcion == '5':
            print('Calculadora finalizada con éxito!')
            break

        num1 = float(input('digite el primer número a operar'))
        num2 = float(input('digite el segundo numero a operar'))

        if opcion == '1':
            suma(num1, num2)

        elif opcion == '2':
            resta(num1, num2)
        
        elif opcion == '3':
            multiplicacion(num1, num2)
        
        elif opcion == '4':
            division(num1, num2)

    else:

        print('opción invalida')
        print()



























"""
def mostrar_menu():
    print("=== CALCULADORA BÁSICA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elegí una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingresá el primer número: "))
        num2 = float(input("Ingresá el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)
        elif opcion == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)
        elif opcion == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado:", resultado)
            else:
                print("Error: no se puede dividir por cero.")
    else:
        print("Opción no válida. Probá de nuevo.")
    
    print()  # Salto de línea para mejor visualización
✅ ¿Qué hace este programa?
Muestra un menú de opciones al usuario.

Lee la opción elegida por teclado.

Si elige una operación válida, pide dos números reales (float).

Ejecuta la operación correspondiente y muestra el resultado.

Si elige salir (opción 5), termina el programa.

🧠 ¿Por qué está hecho así?
while True: crea un bucle infinito que solo se detiene con break (cuando el usuario elige salir).

input() toma texto del usuario, y lo convertimos a número con float().

Condiciones con if, elif, else controlan qué operación se hace.

Se valida la división por cero para evitar errores.

¿Querés que le agreguemos algo, como repetir operaciones sin reiniciar o usar funciones para modularizarlo más?
"""