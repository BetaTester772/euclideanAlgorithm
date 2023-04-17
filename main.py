# Euclidean algorithm
import sys
import time


def division(a, b):
    q = 0
    while True:
        q += 1
        a -= b
        if a < b:
            r = a
            return q, r


def gcd(a, b):
    if b == 0:
        print("=" * 40)
        return a
    else:
        q, r = division(a, b)
        print(a, "=", b, "*", q, "+", r)
        return gcd(b, a % b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("=" * 40)
    start = time.time()
    GCD = gcd(a, b)
    end = time.time()
    print("GCD of", a, "and", b, "is", GCD)
    print("Time: ", end - start)


if __name__ == "__main__":
    if sys.version[:4] != "3.11":  # check python version
        sys.setrecursionlimit(100000)  # set recursion limit
    main()  # run main function
