#Modifique a Classe ListaÚnica para sobrescrever o método extend de UserList.
#extend funciona como append, mas recebe uma lista como parâmetros.
#Verifique o tipo de cada elemento na lista ande de adicioná.lo à lista
from collections import UserList

class ListaÚnica(UserList):
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe

    def append(self, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().append(elem)

    def extend(self, iteravel):
        for elem in iteravel:
            self.append(elem)

    def __setitem__(self, posição, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().__setitem__(posição, elem)

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo inválido")
#obs: teste foi feito  com o modo interativo