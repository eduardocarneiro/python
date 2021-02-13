
alunos = 8

notas = []

for i in range(1, alunos + 1):
    notas = 0
    for j in range(1, 5):
        notas = float(input("Digite a nota[%i/4] do aluno[%i/%i]: " %(j, i, alunos)))

print(notas)
