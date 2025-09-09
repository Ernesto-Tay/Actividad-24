def factorial(val):
    if val ==1:
        return 1
    elif val <1:
        print("El factorial de este número no existe")
        return
    else:
        return val * factorial(val - 1)

def suma(val):
    if val <1:
        print("Debe dar un número mayor a 1")
        return
    elif val == 1:
        return 1
    else:
        return val + suma(val - 1)

def fibonacci(val1, val2 = None):
    if val1 < 1:
        print("No se puede calcular un número de fibonacci negativo")
        return
    elif val1 == 1 or val1 == 2:
        return 1
    else:
        pass #Falta terminar la sencuencia

def apariciones(palabra, letra):
    if letra not in palabra:
        return 0
    else:
        if palabra.count(letra) == 1:
            return 1
        else:
            return 1+ apariciones(palabra, letra)

def inversa(palabra, letra_start = None):
    divisor = palabra.lower.split()
    if not letra_start:
        letra_start = divisor[0]
    if palabra.count(letra_start) == 1:
        pass
    else:
        letra_start = letra_start.capitalize()

def potencia(base, exponente):
    if exponente == 1:
        return base
    elif exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


while True:
    print("\n\n---------------MENÚ---------------\n1. Calcular un factorial\n2. realizar suma recursiva\n3. calcular un número de fibonacci\n4. calcular las apariciones de una letra en una palabra\n5. invertir una cadena de texto\n6. calcular la potencia de un número\n7. Salir")
    select = input("Ingrese una opción: ")
    match select:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")