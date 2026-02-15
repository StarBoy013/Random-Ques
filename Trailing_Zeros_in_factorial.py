def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def count_trailing_zeros(n):
    fact = factorial(n)
    count = 0
    while True:
        if fact % 10 == 0:
            count = count + 1
            fact = fact // 10
        else:
            break
    return count    




def count_trailing_zeros_efficient(n):
    count = 0
    for i in range(5, n, 5):
        count = count + n // i
        return count
    
print(count_trailing_zeros_efficient(10))