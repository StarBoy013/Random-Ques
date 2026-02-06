def count_digits(n):
    if n < 0:
        n = -n
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1
        
    return count

print(count_digits(-12345))


print(299 // 10)