
lista = []

num = int(input("Digite um valor: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um valor: "))

numeroDesejado = int(input("Qual valor deseja procurar: "))
count = 0

for procuraNumero in range(len(lista)):
    if lista[procuraNumero] == numeroDesejado:
        count += 1

print ("O numero procurado %i, apareceu %i vezes." %(numeroDesejado, count))
