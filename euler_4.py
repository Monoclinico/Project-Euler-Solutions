"""
Um número palíndromo lê os dois lados da mesma maneira. O maior palíndromo feito a partir do produto de dois números de 2 dígitos é 9009 = 91 × 99.

Encontre o maior palíndromo feito com o produto de dois números de 3 dígitos.

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palin(p):
  if str(p) == str(p)[::-1]: return True
  else: return False 
value = 0
for v in range(9,1,-1):
  ini, fi = ((v*100)+99),v *100
  for n in range(ini,fi,-1):
    for l in range(ini,fi,-1):
      prod = n*l
      if palin(prod):
        if prod > value:
          value = prod
          n1, n2 = n, l
          break
    if value: break
  if value: break
print(f'{n1} x {n2} = {value}')

#In Setup = Intel Core i3 530 2.93 GHz
#Less time = 0.039223571 seconds
#answer = 906609
#resposta = 906609

