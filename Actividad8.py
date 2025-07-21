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

   def contar_Palabra(palabra, letra, n=0):
       if n == len(palabra):
           return 0
       if palabra[n] == letra:
           return n(palabra, letra, n + 1) + 1
       else:
           return contar_Palabra(palabra, letra, n + 1)


   palabra = input("Ingrese una frase: ")
   letra = input("Ingrese una letra para contar: ")
   if len(letra) != 1:
       print("Por favor ingresa una letra: ")
   else:
       cantidad = contar_Palabra(palabra, letra)
       print(f"la letra {letra} aparece {cantidad} veces en la frase: {palabra}.")


