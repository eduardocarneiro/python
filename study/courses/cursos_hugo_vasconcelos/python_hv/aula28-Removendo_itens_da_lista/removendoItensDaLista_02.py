
tamanhoLista = int(input("Digite o qntos elemetos sua lista vai ter: "))

lista = []

for i in range(tamanhoLista):
    print(i)
    elementosLista = int(input("Digite o valor para %i/%i da sua lista: " %(i + 1 ,tamanhoLista)))
    lista.append(elementosLista)
    print(lista)


