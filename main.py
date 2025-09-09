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

def fibonacci(val):
    if val<=0:
        return 0
    elif val==1:
        return 1
    else:
        return fibonacci(val - 1) + fibonacci(val - 2)

def apariciones(palabra, letra):
    if letra not in palabra:
        return 0
    else:
        if palabra.count(letra) == 1:
            return 1
        else:
            return 1+ apariciones(palabra, letra)

def inversa(palabra, dic_start=None, dic_end=None, lista = False):
    if not lista:
        palabra = list(palabra)
    if dic_start is None and dic_end is None:
        dic_start = 0
        dic_end = len(palabra)-1

    if dic_start >= dic_end:
        return "".join(palabra)

    a = palabra[dic_start]
    b = palabra[dic_end]
    palabra[dic_start] = b
    palabra[dic_end] = a
    return inversa(palabra, dic_start + 1, dic_end - 1, True)

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
            try:
                val = int(input("Ingrese un valor: "))
                if factorial(val).isdigit():
                    print(f"El factorial de {val} es {factorial(val)}")
            except ValueError:
                print("Debe ingresar un número")

        case "2":
            try:
                val = int(input("Ingrese el valor máximo de la suma: "))
                if suma(val).isdigit():
                    print(f"La suma recursiva de {val} es {suma(val)}")
            except ValueError:
                print("Debe ingresar un número")

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