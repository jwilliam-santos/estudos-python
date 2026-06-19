#Escreva um programa que valide a entrada de dados do usuário. 
#Tente achar um número válido de CPF oude CNPJ como definido nos exercícios anteriores. 
#Exiba uma mensagem dizendo se o número é válido ese este é um CNPJ ou um CPF.
import re
verificar_cpf_cnpj = 0
def CHAMAR_CNPJ(CNPJ_CPF):
    global verificar_cpf_cnpj
    cnpjdigitado = re.findall("[0-9]",CNPJ_CPF)
    if len(cnpjdigitado) < 14 or len(cnpjdigitado) > 14:
        print("Não é um CNPJ")
    else:
        print(f" CNPJ :{cnpjdigitado}")
        verificar_cpf_cnpj = 2

def CHAMAR_CPF(CNPJ_CPF):
    global verificar_cpf_cnpj
    
    cpfdigitado = re.findall("[0-9]",CNPJ_CPF)
    if len(cpfdigitado) < 11 or len(cpfdigitado) > 11:
        print("Não é um CPF")
    else:
        print(f" CPF :{cpfdigitado}")
        verificar_cpf_cnpj = 3

CNPJ_CPF = input("Digite os 14 digitos do CNPJ ou os 11 digitos do CPF:").strip()

CHAMAR_CPF(CNPJ_CPF)
CHAMAR_CNPJ(CNPJ_CPF)
if verificar_cpf_cnpj  == 0:
    print("Digite um CPF ou um CNPJ")
elif verificar_cpf_cnpj == 2:
    print("O número digitado foi um CNPJ")
elif verificar_cpf_cnpj == 3:
    print("O número digitado foi um CPF")