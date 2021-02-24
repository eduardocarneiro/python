
tamanhoLista = int(input("Digite o qntos elemetos sua lista vai ter: "))

lista = []
listaAuxiliar = []

for i in range(tamanhoLista):
    print(i)
    elementosLista = int(input("Digite o valor para %i/%i da sua lista: " %(i + 1 ,tamanhoLista)))
    lista.append(elementosLista)
    listaAuxiliar.append(elementosLista)
    print(lista)

for j in listaAuxiliar:
    print("Elemento:" + str(j))
    quantidadeElementos = lista.count(j)
    print("o elemento  " + str(j) + " apareceu " + str(quantidadeElementos) + " na lista: ")
    for removeElemento in range(quantidadeElementos - 1):
        print(removeElemento)
        lista.remove(j)
print(lista)


