def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

n = int(input("Ingrese un numero entero positivo: "))
print(factorial(n))

def Suma(n):
    if n < 0:
        return 0
    else:
        return n + Suma(n - 1)

n = int(input("Ingrese un numero entero positivo: "))

if n > 0:
    resultado = Suma(n)
    print(f"La suma de {n}: {resultado}")
else:
    print("Por favor intente de nuevo")

def Fibonacci(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input("Ingrese un numero de Fibonacci entero positivo: "))
if n > 0:
    resultado = Fibonacci(n)
    print(f"La suma de {n}: {resultado}")
else:
   print("Por favor intente de nuevo")

def contar_Palabra(palabras, letras):
    if not palabras:
        return 0
    elif palabras[0] == letras:
        return 1 + contar_Palabra(palabras[1:], letras)
    else:
        return contar_Palabra(palabras[1:], letras)

palabras = input("Ingrese una palabra: ").strip()
letras = input("Ingrese la letras que desea contar: ").strip()

if len(letras) != 1:
    print("Por favor ingrese una sola letra ")
else:
    resultado = contar_Palabra(palabras, letras)
    print(f"La letra '{letras}' aparece {resultado} veces en la palabra '{palabras}'.")

def Cadena_Texto(texto):
    if len(texto) == 0:
        return ""
    else:
        return texto[-1] + Cadena_Texto(texto[:-1])

texto = input("Ingrese una cadena de texto: ")
Invertir = Cadena_Texto(texto)
print(f"Cadena de texto: {Invertir}")


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("ingrese una base: "))
exponente = int(input("ingrese un exponente: "))
print(potencia(base, exponente))