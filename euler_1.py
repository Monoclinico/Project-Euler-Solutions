"""
Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. 
    A soma desses múltiplos é 23. Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.    
"""
print(sum(list(filter(lambda x: x%3 == 0 or x%5 == 0,range(1000)))))

#time = 0.036709102s
#answer = 233168
#resposta = 233168