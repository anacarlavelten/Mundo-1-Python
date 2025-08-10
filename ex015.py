km = float(input('Digite a quantidade de KMS percorridos: '))
dias = int(input('Dias que o veículo ficou alugado: '))
total = km * 0.15 + dias * 60
print('O valor total a pagar é de {:.2f}'.format(total))