"""
2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem qualquer resto.

Qual é o menor número positivo que é divisível por todos os números de 1 a 20?

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
 
lista = [2,3,5,7,11,13,17,19]
lista2 = [n for n in range(1,21)] 
lista_fat = []
mmc, t, k = 1, 0, 0
while True:
  for n in range(20):
    if ((lista2[n] % lista[k]) == 0):
      t = 1;lista2[n] /= lista[k] 
  if t == 0:
    k += 1
  else:
    t = 0
    mmc*= lista[k]
    lista_fat.append(lista[k])
  if sum(lista2) == 20:
    break
    
for g in range(len(lista_fat)):
  if lista_fat[g] == lista_fat[-1]:
    print(lista_fat[g],'=',mmc)
  else:  
    print(lista_fat[g],end=' x ')
if mmc == 232792560:
  print('Test True!')

#In Setup = Intel Core i3 530 2.93 GHz
#Less time = 0.040831211 seconds
#Answer = 232792560