import random
qtd = int(input('Quantidade de alunos: '))
aluno = []
contador = 0
for i in range(qtd):
    contador += 1
    nome = input(f'Digite o nome do {contador}º aluno: ')
    aluno.append(nome)
ordem = random.shuffle(aluno)
print('A ordem de apresentação será:')
print(aluno)