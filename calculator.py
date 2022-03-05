
# taking input numbers
a = input("Input first number: ")
b = input("Input second number: ")

# taking input for operation
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
op = input("Enter the Sl.no of teh operation to be performed: ")

# selection statements and printing results
if op == '1':
    res=int(a)+int(b)
    print("The Sum of 'a' and 'b' is "+str(res))
elif op == '2':
    res=int(a)-int(b)
    print("The Difference between 'a' and 'b' is "+str(res))
elif op == '3':
    res=int(a)*int(b)
    print("The product of 'a' and 'b' is "+str(res))
elif op == '4':
    res=int(a)/int(b)
    print("The Quotient od 'a' and 'b' is "+str(res))
elif op == '5':
    res=int(a)%int(b)
    print("The Remainder of 'a' and 'b' is "+str(res))
else:
    print("Invalid Input")

# end of program
