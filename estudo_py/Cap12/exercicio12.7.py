#Escreva um programa que valide a entrada de dados do usuário.
#O programa deve aceitar números de CPF no seguinte formato: 999.999.999-99, em que cada 9 representa um dígito.
#Exija os pontos e o traço no final, verificando a correta quantidade de dígitos.
import re
CPF = input("Digite os 11 digitos do cpf:").strip()
cpfdigitado = re.findall("[0-9]",CPF)
if len(cpfdigitado) < 11 or len(cpfdigitado) > 11:
    print("Digite a quantidade correta de digitos")
else:
    print(f" CPF :{cpfdigitado}")