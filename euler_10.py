"""
====================================================================================================
A soma dos primos abaixo de 10 é 2 + 3 + 5 + 7 = 17.

Encontre a soma de todos os primos abaixo de dois milhões.
====================================================================================================
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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
  if primes[-1] > 2000000: 
    primes.pop()
    break
print(sum(primes))  
  
#In Setup = Intel Core i3 530 2.93 GHz
#Less time = 79.391879968 seconds
#Answer = 142913828922
