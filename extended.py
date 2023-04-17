# Extended euclidean algorithm
#            Sn-2, Sn-1, qn-1
j = int(input())

S = []
T = []

def extended_gcd(a, b, c, n=j):
    if b == 0:
        return 0
    else:
        q = a // b
        r = a % b

        print(a, "=", b, "*", q, "+", r)
        return extended_gcd(b, a % b)
