#FACTORIAL USING RECURSION
n=int(input("Enter a number: "))
def factorial(n):
    if n < 2:
        return 
    else:
        return n * factorial(n-1)
c=factorial(n)
print("Factorial of",n,"is",c)