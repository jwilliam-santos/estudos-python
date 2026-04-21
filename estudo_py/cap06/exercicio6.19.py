#Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida. 
#Verifique se onome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.
#--------------------------------------------------------------------------------------------------
#Programa 6.22
#estoque = {
#    "tomate": [1000, 2.30],
#    "alface": [500, 0.45],
#    "batata": [2001, 1.20],
#    "feijão": [100, 1.50],
#}
#venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
#total = 0
#print("Vendas:\n")
#for operação in venda:
#    produto, quantidade = operação
#    preço = estoque[produto][1]
#    custo = preço * quantidade
#    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
#    estoque[produto][0] -= quantidade
#    total += custo
#print(f" Custo total: {total:21.2f}\n")
#print("Estoque:\n")
#for chave, dados in estoque.items():
#    print("Descrição: ", chave)
#   print("Quantidade: ", dados[0])
#   print(f"Preço: {dados[1]:6.2f}\n")
#Programa começa na proxíma linha (28)
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}
total = 0
while True:
    produto = input('Digite o nome do produto (Digite fim para sair)')
    if produto == 'fim':
        print('Tchau')
        break
    if produto in estoque:
        quantidade = int(input('Qual a quantidade que você deseja?'))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f'{produto}: {quantidade} x {preço} = {custo}')
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print('Quantidade acima do limite')
    else:
        print('Produto inexistente ou não está no estoque ')
print(f'Custo total: {total}')
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")