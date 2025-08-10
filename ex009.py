num = int(input('Digite um número: '))
contador = 0
for t in range(10):
    contador += 1
    print('{} X {} = {}'.format(num,contador,num*contador))
