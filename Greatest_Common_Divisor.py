def gcd(a, b):
    c = a if a > b else b
    for i in range(c, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

gcd(10,2)


# Euclidean's algorithm for GCD

def gcd_euclidean(a, b):
    while a != b:
        if a> b:
            a = a - b
        else:
            b = b - a
    return a

print(gcd_euclidean(10, 20))

# More efficient version of Euclidean's algorithm for GCD

def gcd_euclidean_efficient(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclidean_efficient(b, a % b)
    
print(gcd_euclidean_efficient(10, 20))