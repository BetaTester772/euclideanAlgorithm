# euclidean algorithm
import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        print(a, "%", b, "=", a % b)
        return gcd(b, a % b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("GCD of", a, "and", b, "is", gcd(a, b))


if __name__ == "__main__":
    if sys.version[:4] != "3.11":
        sys.setrecursionlimit(100000)
    main()
