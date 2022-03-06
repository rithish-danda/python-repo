# program to find the factorial of a number



# factorial function
def factorial(n):
    n = int(n)
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        f = 1
        while n > 1:
            f = f * n
            n -= 1
        return f

      
      
# Driver Code
num = input("Enter any number: ")
fact = factorial(num)
print("The Factorial of ",num,"is ",fact,".")


