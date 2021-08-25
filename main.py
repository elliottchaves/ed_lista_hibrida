from ListaHibrida import *

lista = ListaHibrida()

lista.inserir_inicio(10)
#lista.imprime_lista()
lista.inserir_inicio(20)
lista.inserir_inicio(30)

lista.imprime_lista()
print('---')

lista.inserir_final(2)
lista.inserir_final(3)
lista.inserir_final(4)
lista.imprime_lista()

print('---vs2')
lista.inserir_inicio(6)
lista.imprime_lista()

print('--vs3')
lista.inserir_final(5)
lista.imprime_lista()


