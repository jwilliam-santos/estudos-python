#Atualmente a classe Televisão  inicializa com o canal 2.
#Modifique  a classe Televisão de forma a receber o canal inicial em seu construtor como parâmetro opicional
class Televisão:
    def __init__(self, canal_min, canal_max,canal_inic):
        self.ligada = False
        self.canal = canal_inic
        self.canal_min = canal_min
        self.canal_max = canal_max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_max:
            self.canal += 1


tv = Televisão(1, 99,13)
for x in range(0, 120,14):
    tv.muda_canal_para_cima()
print(tv.canal)
for x in range(0, 120,5):
    tv.muda_canal_para_baixo()
print(tv.canal)