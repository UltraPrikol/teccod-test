def is_prime(num: int):

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def prime_numbers(min_num, max_num):
    prime_list = []

    for num in range(min_num, max_num + 1):
        if is_prime(num):
            prime_list.append(num)

    return prime_list


print(prime_numbers(1, 10))
