def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        print('Простое' if count == 2 else 'Составное')
        return n
        pass

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

#  без анотации
# result2 = is_prime(sum_three)
# result3 = result2(2, 3, 6)
# print(result3)
