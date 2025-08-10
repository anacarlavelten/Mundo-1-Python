import math
from math import hypot

'''co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
h = math.sqrt((math.pow(co,2)) + (math.pow(ca,2)))
print(f'O valor da hipotenusa é : {h: .2f}')'''

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = hypot(co,ca)
print(f'O valor da hipotenusa é: {h: .2f}')