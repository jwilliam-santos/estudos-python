#Nome "lista_unica.py" como pedido no livro
from collections import UserList


class ListaÚnica(UserList):
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe

    def append(self, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().append(elem)

    def __setitem__(self, posição, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().__setitem__(posição, elem)

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo inválido")