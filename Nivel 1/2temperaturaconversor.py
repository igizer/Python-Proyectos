# Pasar de cualquier unidad a Celsius
def a_celcius(numero, unidad):
    if unidad == "C":
        return numero
    elif unidad == "F":
        return (numero - 32) * 5 / 9
    elif unidad == "K":
        return numero - 273.15

# Pasar de Celsius a cualquier unidad
def desde_celcius(temperatura, deseado):
    if deseado == "C":
        return temperatura
    elif deseado == "F":
        return (temperatura * 9 / 5) + 32
    elif deseado == "K":
        return temperatura + 273.15

# Función principal del programa
def programa():
    print('Conversor de temperaturas (Celsius (°C), Fahrenheit (°F) y Kelvin (K))')
    temperatura = float(input("Escriba la temperatura actual (número): "))
    unidad = input("Unidad actual ('C', 'F', 'K'): ").upper() #UPPER CONVIERTE A MAYUSCULA, POR SI LA ENTRADA ERA UNA MINUSCULA
    deseado = input("Unidad a convertir ('C', 'F', 'K'): ").upper()

    if unidad in ['C', 'F', 'K'] and deseado in ['C', 'F', 'K']:
        temp_celcius = a_celcius(temperatura, unidad)
        respuesta = desde_celcius(temp_celcius, deseado)
        print("La temperatura convertida es:", respuesta, deseado)
    else:
        print('ERROR: ¡Unidad inválida!')

# Bucle principal
while True:
    print()
    programa()
    cerrar= input("¿Desea volver a convertir una temperatura o cerrar programa? (Escriba 1 Para 'Cerrar' o cualquier otra para seguir")
    if cerrar == "1":
        break