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