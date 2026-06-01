#Modifique o programa da calculadora que usa partial para suportar mais duas operações:
#raiz para raiz quadrada e potência para exponenciação.
#--------------------------------------------------------------------------------------
#import operator
#from functools import partial
#
#
#def executa(operação, símbolo, operando1, operando2):
#    resultado = operação(float(operando1), float(operando2))
#    print(f"{operando1} {símbolo} {operando2} = {resultado}")
#
#
#operações = {
#    "+": partial(executa, operator.add, "+"),
#    "-": partial(executa, operator.sub, "-"),
#    "*": partial(executa, operator.mul, "×"),
#    "/": partial(executa, operator.truediv, "÷"),
#}
#operando1 = input("Operador 1: ")
#operando2 = input("Operador 2: ")
#operação = input("Operação: ").strip()
#if operação in operações:
#    operações[operação](operando1, operando2)
#else:
#    print("Operação inválida!")
#Programa começa na proxíma linha (27)
import operator
from functools import partial
import math

def executa(operação, símbolo, operando1, operando2):
    resultado = operação(float(operando1), float(operando2))
    print(f"{operando1} {símbolo} {operando2} = {resultado}")


operações = {
    "+": partial(executa, operator.add, "+"),
    "-": partial(executa, operator.sub, "-"),
    "*": partial(executa, operator.mul, "×"),
    "/": partial(executa, operator.truediv, "÷"),
    '**': partial(executa,operator.pow,'Potência' ), #ptt e a potencia
    'raiz': partial(executa,lambda x,y: math.sqrt(x),'Raiz quadrada'), # sqrt é a raiz quadrada
}
operando1 = input("Operador 1: ")
operação = input("Operação: ").strip()
if operação in operações:
    if operação == 'raiz':
        operações[operação](operando1,0)
    else:
        operando2 = input("Operador 2: ")
        operações[operação](operando1, operando2)
else:
    print("Operação inválida!")
