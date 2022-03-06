# program to calculate the compound interest of a given loan

from math import pow


# compound interest calculator function
def compound(p, t, r):
    p = int(p)
    t = int(t)
    r = int(r)

    intr = p * pow((1 + r), t)
    return intr


# driver code

pr = input("Input the principle amount: ")
ti = input("Input the time period: ")
rate = input("Input the rate of interest: ")

intr = compound(pr, ti, rate)

print("The compound interest formed over",ti,"years for Rs.",pr,"is",intr,".")
