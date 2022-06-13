# This program finds the Permutation of two given numbers
# This program works according to the formula:
# nPr = n!/(n-1)!
# simply, choice of r things from a set of n.

def main():
    n = int(input("Enter number: "))    # input takes value of n
    r = int(input("Enter second number: "))     # input takes value of r
    fact1 = numerator(n, r)     # value of n and r is passed into numerator function, result returned into fact1.
    fact2 = denominator(n, r)    # value of n and r passed into denominator function, returned into fact2.
    permutation = fact1 // fact2    # final result

    print(f'{n}P{r} = {permutation}')


def numerator(num1, num2):     # denominator function
    if num1 < num2:         # returns 0 if num1 is less than num2, to truncate the result to 0.
        return 0
    else:
        total = 1   # initialize accumulator.
        for i in range(num1):    # iterates i, num times, starting from 0.
            fact = (num1 - i)
            total *= fact   # accumulate and multiply result
        return total


def denominator(a, b):  # denominator function
    total = 1   # initialize accumulator
    diff = a - b
    for j in range(diff):    # iterates j, diff times, starting from 0.
        fact = (diff - j)
        total *= fact   # accumulate and multiply result
    return total


main()