import random
aluno = []
contador = 0
quantidade = int(input('Quantidade de alunos: '))
for i in range(quantidade):
    contador += 1
    nome = input(f'Digite o nome do {contador}º aluno: ')
    aluno.append(nome)
sorteio = random.choice(aluno)
print(f'O aluno sorteado foi: {sorteio}')
