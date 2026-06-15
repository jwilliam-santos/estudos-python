#Adicione os atributos tamanho e marca à classe Televisão.
#Crie os objetos Televisão e atribua tamanhos e marcas diferentes.
#Depois, imprima o  valor desses atributos de forma a confirmar a independência dos valores de cada instância (objeto)
class Televisão:
    def _init_(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = "42''"
        self.marca = "LG"
tv1 = Televisão()
tv1.ligada = True
tv1.canal = 39
tv1.tamanho = "50''"
tv1.marca = "Samsung"
tv2 = Televisão()
tv2.ligada = True
tv2.canal = 136
tv2.tamanho = "30''"
tv2.marca = "Philico"
print(f"A primeira tv tem caracteristicas {tv1.ligada,tv1.canal,tv1.tamanho,tv1.marca}")
print(f"A segunda tv tem caracteristicas {tv2.ligada,tv2.canal,tv2.tamanho,tv2.marca}")