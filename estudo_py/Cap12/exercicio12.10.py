#Escreva uma função que aceite preços em reais. O programa deve ignorar espaços em branco e aceitarvalores prefixados com R$ ou não (com r ou R). O usuário deve entrar valores corretamente formatados com o ponto separando os milhares e a vírgula, os centavos. Se o usuário digitar centavos, estes devem ter
#dois dígitos.
#Valores válidos:
# R$500
#     R$500
#R$500,10
#R$7.312,10
#A função deve retornar o valor digitado convertido para float ou gerar uma exceção do tipo ValueError caso o valor entrado seja inválido.
import re
def aceitar_preço():
    dinheiro = input("Digite os valores em reais").lower()
    dinheirodigitado = re.match(r"\s*(?:r\$)?\s*\d+(?:\.\d{3})*(?:,\d{2})?$", dinheiro)
    try:
        if dinheirodigitado:
            print(dinheirodigitado.group())
        else:
            raise ValueError("Valor incorreto")
    except Exception as e:
        print(f"o erro foi {e}")

aceitar_preço()
        
