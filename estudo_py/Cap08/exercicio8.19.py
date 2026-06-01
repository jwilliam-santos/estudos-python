#Escreva um generator capaz de gerar a sequência de números primos.
def gerador_primos():
    yield 2
    proxprimo = 3
    
    while True:
        divisor = 3
        while divisor < proxprimo:
            if proxprimo % divisor == 0:
                break 
            divisor += 2
        if divisor == proxprimo:
                yield proxprimo 
        proxprimo += 2
g = gerador_primos()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

