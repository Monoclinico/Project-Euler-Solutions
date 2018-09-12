"""
Um trigêmeo pitagórico é um conjunto de três números naturais, um < b < c , para o qual,

a^2 + b^2 = c^2
Por exemplo, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Existe exatamente um tripleto pitagórico para o qual a + b + c = 1000. 
Encontre o produto abc.
============================================================================================================
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

li_a = li_b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
abc = 0
for a in li_a:
  for b in li_b:
    c =(((a**2) + (b**2))**(1/2))
    if c.is_integer() and b > a:
      n = 1000/ (a+b+c)
      a *= n; b *= n; c *= n
      if a.is_integer() and b.is_integer() and c.is_integer():
        abc = a * b * c
        break
  if abc != 0:
    break
print(abc)
#In Setup = Intel Core i3 530 2.93 GHz
#Less time = 0.043 seconds
#Answer = 31875000