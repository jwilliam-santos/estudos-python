#Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias (objetos), especificando o valor de canal_min e canal_max por nome.
class Televisão:
    def __init__(self, canal_min=2, canal_max=14):
        self.ligada = False
        self.canal = 2
        self.canal_min = canal_min
        self.canal_max = canal_max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1
        else:
            self.canal = self.canal_max
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
        else:
            self.canal = self.canal_min

tv = Televisão(2,10)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
tv1 = Televisão()
print(tv1.canal)
obj1 = Televisão(canal_max=136,canal_min=39)
obj2 = Televisão(canal_min=30,canal_max=90)
print(f"{obj1.canal_min} e  objeto1 ")
print(f"{obj2.canal_max} e  objeto2 ")