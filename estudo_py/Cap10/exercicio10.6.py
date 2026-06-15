#Modifique a classe Televisão de forma que os métodos muda_canal_para_cima e muda_canal_para_baixo retornem o canal após a mudança
class Televisão:
    def __init__(self, canal_min=2, canal_max=14):
        self.ligada = False
        self.canal = 2
        self.canal_min = canal_min
        self.canal_max = canal_max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1
            return self.canal
        else:
            self.canal = self.canal_max
            
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1
            return self.canal
        else:
            self.canal = self.canal_min
            return self.canal

tv = Televisão(2,10)
print(tv.muda_canal_para_baixo())