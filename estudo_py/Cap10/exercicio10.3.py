#Modifique a classe Televisão de forma que, se pedirmos para mudar o canal ela vá para o canal máximo.
#Se mudarmos o canal para cima além do canal máximo, que volte ao canal mínimo.
class Televisão:
    def __init__(self, canal_min, canal_max):
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