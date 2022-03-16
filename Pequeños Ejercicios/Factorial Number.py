number = int(input("Ingresen un número: "))
factorialNumber = 1

if number < 0:
    print("Lo siento. No se puede hacer la factoría de un numero negativo.")
elif number == 0:
    print("La factoría de cero es igual a 1.")
else:
    for value in range(1, number + 1):
        factorialNumber = factorialNumber * value
    print(factorialNumber)

