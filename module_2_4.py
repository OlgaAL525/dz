

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [False]
not_primes = [False]
for i in numbers:
    is_prime = True
    for j in range(i):
        j += 1
        if j != 1 and j != i and i % j ==0:
            is_prime = False
            break
    if  is_prime == True  and i != 1:
        primes.append(i)
        not_primes.append(False)
    elif is_prime == False  and i != 1:
        primes.append(False)
        not_primes.append(i)
primes_1 = list(set(primes))
primes_1.remove(False)
print('Primes', primes_1)
not_primes_1 = list(set(not_primes))
not_primes_1.remove(False)
print('Not Primes', not_primes_1)


