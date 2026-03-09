numero = input("Digite o número a verificar:").strip()
i = 0
f = len(numero) - 1  
while f > i and numero[i] == numero[f]:
    f = f - 1
    i = i + 1
if numero[i] == numero[f]:
    print(f"{numero} é palíndromo")
else:
    print(f"{numero} não é palíndromo")
