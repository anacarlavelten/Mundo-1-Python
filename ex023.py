"""num = str(input('Digite o número: '))
num
print(f'UNIDADE {lista[3]}')
print(f'DEZENA {lista[2]}')
print(f'CENTENA {lista[1]}')
print(f'MILHAR {lista[0]}')"""


num = int(input('Digite um número: '))
if(num < 0 and num > 9999):
    print('Número inválido')
else:
    print(f'Milhar {num//1000}')
    print(f'Centena {(num%1000)//100}')
    print(f'Dezena {((num%1000)%100)//10}')
    print(f'Unidade {(((num%1000)%100)%10)}')