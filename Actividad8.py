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

   def Palabra(n):

