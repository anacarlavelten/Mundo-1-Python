cidade = str(input('Digite o nome da Cidade: ')).lower()
lista = cidade.split()
if lista[0] == 'santo':
    print('A cidade indicada começa com Santo')
else:
    print('A cidade indicada não começa com Santo')