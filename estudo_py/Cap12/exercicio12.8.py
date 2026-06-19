#Escreva um programa que valide a entrada de dados do usuário. 
#O programa deve aceitar números de CNPJ no seguinte formato: 99.999.999/9999-99, em que cada 9 representa um dígito. 
#Exija os pontos e o traço no final, verificando a correta quantidade de dígitos.
import re
CNPJ = input("Digite os 14 digitos do CNPJ:").strip()
cnpjdigitado = re.findall("[0-9]",CNPJ)
if len(cnpjdigitado) < 14 or len(cnpjdigitado) > 14:
    print("Digite a quantidade correta de digitos")
else:
    print(f" CNPJ :{cnpjdigitado}")