def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    return primes

while True:
    n = int(input())
    if n == 0:
        break
    
    primes = sieve_of_eratosthenes(2 * n)
    count = sum(1 for prime in primes[n + 1:2 * n + 1] if prime)
    print(count)