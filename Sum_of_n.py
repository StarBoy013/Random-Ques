def sum_of_n_numbers(n):
    total = 0
    if n <= 0:
        return "Should be positive"
    else:
        for i in range(n+1):
            total = total + i
        return total
    
    
sum_of_n_numbers(100)
