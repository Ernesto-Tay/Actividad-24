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
    if val<0:
        print("No se puede sacar un valor de fibonacci negativo")
        return 0
    elif val==0:
        return 0
    elif val==1:
        return 1
    else:
        return fibonacci(val - 1) + fibonacci(val - 2)

def apariciones(palabra, letra):
    if letra not in palabra:
        return 0
    else:
        if palabra == "":
            return 0
        elif palabra[0] == letra:
            return 1 + apariciones(palabra[1:], letra)
        else:
            return apariciones(palabra[1:], letra)

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
                print(f"El factorial de {val} es {factorial(val)}")
            except ValueError:
                print("Debe ingresar un número entero")

        case "2":
            try:
                val = int(input("Ingrese el valor máximo de la suma: "))
                print(f"La suma recursiva de {val} es {suma(val)}")
            except ValueError:
                print("Debe ingresar un número entero")

        case "3":
            try:
                val = int(input("Ingrese el valor de la secuencia de fibonacci que desea encontrar: "))
                print(f"El valor {val} de la secuencia de fibonacci es {fibonacci(val)}")
            except ValueError:
                print("Debe ingresar un número entero")

        case "4":
            try:
                palabra = input("Ingrese una palabra: ")
                letra = input("Ingrese la letra a contar: ")
                print(f"La letra {letra} aparece {apariciones(palabra, letra)} veces en `{palabra}`")
            except Exception as e:
                print("Error inesperado",e)

        case "5":
            try:
                palabra = input("Ingrese una palabra: ")
                print(f"Si invertimos `{palabra}`, sería `{inversa(palabra)}`")
            except Exception as e:
                print("Error inesperado",e)

        case "6":
            try:
                num = int(input("Ingrese un número: "))
                exponente = int(input("Ingrese el exponente: "))
                if exponente <0:
                    print("El exponente debe ser mayor a 0")
                else:
                    print(f"{num} a la {exponente} es: {potencia(num, exponente)}")
            except ValueError:
                print("Ingrese números enteros")

        case "7":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")