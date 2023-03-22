# euclidean algorithm
import sys


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
        return a
    else:
        q, r = division(a, b)
        print(a, "=", b, "*", q, "+", r)
        return gcd(b, a % b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("GCD of", a, "and", b, "is", gcd(a, b))


if __name__ == "__main__":
    if sys.version[:4] != "3.11":  # check python version
        sys.setrecursionlimit(100000)  # set recursion limit
    main()  # run main function
