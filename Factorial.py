def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


factorial(5)

# Method 2

def factorial(n):
    f = 1
    for i in range(n-1):
        f = f * (n - i)
    return f