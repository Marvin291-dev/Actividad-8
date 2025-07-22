while True:
        print("\n🎯 MENÚ DE OPCIONES")
        print("1. Factorial")
        print("2. Suma")
        print("3. Fibonacci")
        print("4. Contar una letra en una palabra")
        print("5. Invertir cadena de texto")
        print("6. Potencia")
        print("7. Salir")
        try:
            opcion = int(input("Selecciona una opción: "))
            match opcion:
                case 1:
                    def factorial(n):
                        if n == 0 or n == 1:
                            return 1
                        else:
                             print(n)
                        return n * factorial(n - 1)

                    n = int(input("Ingrese un numero entero positivo: "))
                    print(factorial(n))

                case 2:
                    def Suma(n):
                        if n == 1:
                            return 1
                        else:
                            return n + Suma(n - 1)
                    try:
                        n = int(input("Ingrese un numero entero positivo: "))
                        if n > 0:
                            result = Suma(n)
                            print(f"El resultado es: {result}")
                        else:
                            print("Por favor ingrese un numero que no sea 0")
                    except ValueError:
                        print("Intente de nuevo")

                case 3:
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

                case 4:
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

                case 5:
                    def Cadena_Texto(texto):
                        if len(texto) == 0:
                            return ""
                        else:
                            return texto[-1] + Cadena_Texto(texto[:-1])

                    texto = input("Ingrese una cadena de texto: ")
                    Invertir = Cadena_Texto(texto)
                    print(f"Cadena de texto: {Invertir}")

                case 6:
                    def potencia(base, exponente):
                        if exponente == 0:
                            return 1
                        else:
                            return base * potencia(base, exponente - 1)


                    base = int(input("ingrese una base: "))
                    exponente = int(input("ingrese un exponente: "))
                    print(potencia(base, exponente))
                case 7:
                    print("¡Hasta luego!")
                    break
                case _:
                    print("Opción fuera de rango. Intenta nuevamente.")
        except ValueError:
                     print("❌ Entrada inválida. Por favor ingresa un número entre 1 y 7.")