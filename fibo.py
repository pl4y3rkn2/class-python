def fibonachi(n):
    if n==0 or n==1:
        return 1
    return fibonachi(n-1)+fibonachi(n-2)

n=int(input("coloca un numero: "))

print(fibonachi(n))