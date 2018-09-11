"""
===============================================================
A soma dos quadrados dos dez primeiros números naturais é,

1^2 + 2^2 + ... + 10^2 = 385
O quadrado da soma dos dez primeiros números naturais é,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Portanto, a diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025 - 385 = 2640.

Encontre a diferença entre a soma dos quadrados dos primeiros cem números naturais e o quadrado da soma.

===============================================================
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def q(y):
  return y*y
sum_q = sum(list(map(q, range(1,101))))
q_sum = ((1+100)*50)**2 #PA Sum, Soma de PA 
print(q_sum - sum_q)

#In Setup = Intel Core i3 530 2.93 GHz
#Less time = 0.032736435 seconds
#Answer = 25164150