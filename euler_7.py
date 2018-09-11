"""
====================================================================================================
Listando os seis primeiros números primos: 2, 3, 5, 7, 11 e 13, podemos ver que o sexto primo é 13.

Qual é o 10 001º número primo?
====================================================================================================
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes, n  = [2], 3
q = met = t = 0
while True:
  met = n ** (1/2)
  for d in primes:
    if n % d == 0: q += 1
    if d > met: t += 1
    if t == 2: break
  if q == 0: primes.append(n)
  q = t = 0
  n += 2
  if len(primes) == 10001: break
print(primes[-1])    
#In Setup = Intel Core i3 530 2.93 GHz
#Less time = 2.018032216 seconds
#Answer = 104743