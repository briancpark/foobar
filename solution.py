def solution(i):
    # Your code here
    result = produce_prime_string(i)
    return result[i : i + 5]


def produce_prime_string(n):
    string = ""
    for i in range(n + 100):
        if is_prime(i):
            string = string + str(i)
    return string


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
