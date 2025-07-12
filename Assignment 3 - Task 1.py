n = int(input("enter a number : "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(n)
print("factorial of " + str(n) + " is " + str(result))