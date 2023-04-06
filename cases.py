# Euclidean algorithm which faster than main.py
import sys
import time


def gcd(a, b):
    if b == 0:
        print("-" * 40)
        return a
    else:
        q = a // b
        r = a % b
        print(a, "=", b, "*", q, "+", r)
        return gcd(b, a % b)


def main():
    a, b = sorted(list(map(int, input("Enter two numbers: ").split())), reverse=True)

    print("-" * 40)
    start = time.time()
    GCD = gcd(a, b)
    end = time.time()
    print("GCD of", a, "and", b, "is", GCD)
    print("=" * 40, end='\n\n')


if __name__ == "__main__":
    if sys.version[:4] != "3.11":  # check python version
        sys.setrecursionlimit(100000)  # set recursion limit
    T = int(input("Enter number of cases: "))
    print("\n\n")
    for _ in range(T):
        main()  # run main function
