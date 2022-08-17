def factorial (n):
    print(n)
    if n==1:
        return 1

    return n * factorial(n-1)

n = int(input("escribe un entero: "))
print (factorial(n))