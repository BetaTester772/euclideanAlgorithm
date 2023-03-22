# euclidean algorithm

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
    main()
