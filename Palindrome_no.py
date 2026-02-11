# def palindrome_no(n):
#     r = int(str(n)[::-1])
#     if n == r:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
    
# print(palindrome_no(8))

def palindrome_no(n):
    c = n
    r = 0
    for i in range(len(str(n))):
        a = n % 10
        r = r * 10 + a
        n = n // 10
    if c == r:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
print(palindrome_no(8))