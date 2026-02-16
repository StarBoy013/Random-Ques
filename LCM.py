def lcm(a, b):
    c = a if a > b else b
    while True:
        if c % a == 0 and c % b == 0:
            return c
        c += 1
        
print(lcm(13, 7))

# a*b = gcd(a, b) * lcm(a, b)