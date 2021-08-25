import copy

class Node:
    def __init__(self, dado):
        self.__carga = dado
        self.__prox = -1

    def set_prox(self,novo_prox):
        self.__prox = novo_prox

    def get_prox(self):
        return self.__prox

    def set_carga(self, nova_carga):
        self.__carga = nova_carga

    def get_carga(self):
        return self.__carga


class ListaHibrida:

    def __init__(self):
        self.__vetor = []
        self.__head = None

    def get_tamanho(self):
        return len(self.__vetor)

    def get_head(self):
        return self.__head

    def set_head(self, novo_head):
        self.__head = novo_head

    def set_vetor(self, novo_vetor):
        self.__vetor = novo_vetor

    def get_vetor(self):
        return self.__vetor

    def set_no(self, no):
        self.__vetor.append(no)

    #def get_

    def inserir_inicio(self, valor):

        novo_no = Node(valor)

        if self.get_head() == ( self.get_tamanho() - 1):
            novo_no.set_prox(self.get_tamanho() - 1)
            self.set_no(novo_no)
            self.set_head(self.get_tamanho() - 1)

        elif self.get_head() == 0:
            nova_lista = list(reversed(self.get_vetor()))
            for i in range(len(nova_lista)):
                nova_lista[i].set_prox(i - 1)

            nova_lista.append(novo_no)
            self.set_vetor(nova_lista)
            self.set_no(novo_no)
            self.set_head(self.get_tamanho() - 1)

    def inserir_final(self, valor):

        novo_no = Node(valor)

        if self.get_head() == 0:

            novo_vetor = copy.deepcopy(self.get_vetor())

            novo_vetor[-1].set_prox(self.get_tamanho())

            novo_vetor.set_no(novo_no)

            self.set_vetor(novo_vetor)
        pass
    def remover_inicio(self):
        pass
    def remover_final(self):
        pass


