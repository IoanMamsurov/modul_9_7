
def is_prime(func):
    def wrapper(*args):
        summ = sum(args)
        d = 0
        for i in range(2, summ - 1):
            if summ % i == 0:
                d += 1
        if d == 0:
            return f'{func(*args)}\nПростое'
        else:
            return f'{func(*args)}\nСоставное'
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)

