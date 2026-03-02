#escreva um programa para controlar uma pequena maquina registradora,
# Você deve solicitar ao usuario que deve solicitar
#  ao usuario que digite o codigo do produto e a quantidade comprada.
# Utilize a tabela de codigo a seguir de preços a cada produto
# codigo  / preço
#   1     / 0.50
#   2     /   1.00
#   3     /  4.00
#   5     / 7.00
#   9      /  8.00
#seu programa deve exibir o total de compras depois que o usuario digitar 0,
#  Qualquer outro codigo deve gerar a mensagem de erro 'Código inválido'.
print('olhe a tabela a seguir e digite separadamente o seu produto e a quantidade de cada um deles')
print(' codigo  / preço') 
print('    1    /   0.50 ')
print('    2    /   1.00 ')
print('    3    /   4.00 ')
print('    5    /   7.00' )
print('    9    /    8.00')
codigo_produto = input('Digite o codigo so seu produto de acordo com a ultima tabela')
quantidade = int(input('digite a quantida do seu produto que vc deseja comprar'))
if codigo_produto == '1' and quantidade >= 1:
    preço =  quantidade * 0.50
    print(f'o preço final so seu produto deu: {preço}')
elif codigo_produto == '2' and quantidade >= 1:
    preço = quantidade * 1
    print(f' o preço final da sua compra deu {preço}')
elif codigo_produto == '3' and quantidade >= 1:
    preço = quantidade * 4
    print(f'o preço do produto da sua compra deu {preço}')
elif codigo_produto =='5'and quantidade >= 1:
    preço = quantidade * 7 
    print(f'O preço final da sua conta deu: {preço}')
elif codigo_produto == '9' and quantidade >=1:
    preço = quantidade * 8
    print(f'o preço final de sua compra deu {preço}')
else:
    print('codigo invalido!!!!')