#modifique o programa anterior de forma a ler um número n.
#imprima os n primeiros números primos
quantidades_n = int(input('Digite a quantidades de numeros primos a ser gerada'))
if quantidades_n < 0:
    print('Digite so números positivos')
else:
    if quantidades_n >= 1:
        print('2')
    primonum = 1
    proxprimo = 3
    while primonum < quantidades_n:
        divisor = 3
        while divisor < proxprimo:
            if proxprimo % divisor == 0:
                break
            divisor += 2
        if divisor == proxprimo:
            print(proxprimo)
        primonum += 1
        proxprimo += 2