import math 


def primes(limit):
    avaliable_primes = [True for _ in range(limit+1)]
    prime_candidate = 2
    while prime_candidate < math.sqrt(limit):
        if avaliable_primes[prime_candidate]:
            for j in range(prime_candidate * 2, limit+1, prime_candidate):
                avaliable_primes[j] = False
        prime_candidate += 1
    return [i for i in range(2, limit+1) if avaliable_primes[i]]