numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print("Fizz")

elif numero % 3 == 0 and numero % 5 == 0:
    print("Fizzbuzz")
    
elif numero % 5 == 0:
    print("Buzz")

else:
    print("Esse número não é divísivel por 3 ou 5")