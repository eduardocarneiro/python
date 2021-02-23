#!/usr/bin/python

alunos = 2

media = []

for i in range(1, alunos +1):
    notas = 0
    for j in range(1, 5):
        print("Digite a nota %i para o aluno %i: " %(j,i))
        notas += float(input())
    notas /= 4
    media.append(notas)

n = 0 

print(media)
for mediaAluno in media:
    if mediaAluno >= 6:
        n += 1
print(n) 
