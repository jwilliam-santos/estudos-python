#nome pilhas.py pois foi pedido no Livro
class Pilha:
    def __init__(self, energia=100):
        self.energia = energia

    def consuma(self, consumo):
        if consumo > self.energia:
            consumo = self.energia
        self.energia -= consumo
        return consumo
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
    def __init__(self, televisão, pilha):
        self.televisão = televisão
        self.pilha = pilha

    def liga(self):
        if self.pilha.consuma(1):
            self.televisão.ligada = True

    def desliga(self):
        if self.pilha.consuma(1):
            self.televisão.ligada = False

    def canal_mais(self):
        if self.pilha.consuma(1):
            self.televisão.muda_canal_para_cima()

    def canal_menos(self):
        if self.pilha.consuma(1):
            self.televisão.muda_canal_para_cima()