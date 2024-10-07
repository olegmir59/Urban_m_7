# Домашнее задание по теме "Декораторы"
# Задание: Декораторы в Python

def is_prime_trial_division(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if is_prime_trial_division(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(n1, n2, n3):
    return n1 + n2 + n3


result = sum_three(2, 3, 6)
print(result)

result = sum_three(1, 3, 6)
print(result)