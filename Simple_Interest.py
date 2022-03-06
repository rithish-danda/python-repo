# program to find simple interest from given details

# Simple Interest calculation function
def simple( p, t, r):
    p = int(p)
    t = int(t)
    r = int(r)
    intr = (p * t * r) / 100
    return intr

# Driver Code

pr = input("Input the value of principle amount: ")
# principle amount in INR
ti = input("Input the time period of the loan: ")
# time period taken in years
rate = input("Input the rate of interest: ")
# rate of interest taken in %

intr = simple(pr, ti, rate)
print("The simple interest for the principle amount",pr,"over",ti,"years is",intr,".")
