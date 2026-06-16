#Crie classes para representar estados e cidades.
#Cada estado tem um nome, sigla e cidades.
#Cada cidade tem nome e População.
#Escreva um programa de testes que crie três estados com algumas cidades em cada um.
#Exiba a População de cada estado como a soma da população de suas cidades.
class Cidade: #COMPLETO
    def __init__(self,nomecdd,populaçãocdd):
        self.nomecdd = nomecdd
        self.população = populaçãocdd
    
class Estado:
    def __init__(self,sigla="sp",cdd = [],):#COMPLETO
        
        self.sigla = sigla #Pronto
        self.cidades = cdd
    
    def mostrar(self):#rr
        
        print(f" Sigla {self.sigla}, ")# MOSTRA SIGLA
        for c in self.cidades:# MOSTRAR NOME CIDADE
            print(f"Uma cidade é {c.nomecdd}, e sua Poupulação {c.população}\n")

Sorocaba = Cidade("sorocaba",757)
Osasco = Cidade("osasco",759)
Sp = Estado("Sp",cdd=[Sorocaba,Osasco],)