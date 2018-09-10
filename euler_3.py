"""
Os fatores primos de 13195 são 5, 7, 13 e 29.

Qual o maior fator primo do número 600851475143?

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
#!!!Problema resolvido com um código especifico para o número 600851475143!!!
def primo(p):
  a = 0
  for b in range(1,p):
    if p%b == 0:
      a+=1
  if a == 1:
    return True
  else:
    return False

lista = []
n = 600851475143
u = 600851475143
for h in range(1000,5000,1000):
  for i in range(h-999,h,1):
    if n%i == 0:
      if primo(i):
        lista.append(i)
  n /= lista[-1]
mult = 1
for o in lista:
  mult *= o 
print(u/mult)

#In Setup = Intel Core i3 530 2.93 GHz
#Less time = 0.038233453 seconds
#answer = 6857