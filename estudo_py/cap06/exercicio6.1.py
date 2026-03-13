#modfique o programa 6.2 para ler 7 notas em vez de 5.
# notas = [0,0,0,0,0,]
# soma = 0
# x = 0
#while x < 5
#   notas[x] = float(input(f' nota {x}:'))
#    soma += notas[x]
#   x += 1
# x = 0
#while x < 5:
#   print(f'nota {x}: {notas[x]:6.2f}')
#   x +- 1
#print(f'media: {soma/ x:5.2f})
#exercicio 6.1 começa na proxima linha (15);
notas = [0]* 7
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f'nota {x}:'))
    soma += notas[x]
    x += 1
while x >= 8 :
    print(f' nota{x}: {notas[x]:6.2f}')
    x +- 1
print(f'sua média e {soma/x:5.2f}')