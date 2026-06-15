#Esse Programa reune a classe Televisão e a classe controle remoto, foi nomeado como pedido no livro
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
class ControleRemoto:
    def __init__(self, televisão):
        self.televisão = televisão

    def liga(self):
        self.televisão.ligada = True

    def desliga(self):
        self.televisão.ligada = False

    def canal_mais(self):
        self.televisão.muda_canal_para_cima()

    def canal_menos(self):
        self.televisão.muda_canal_para_cima()