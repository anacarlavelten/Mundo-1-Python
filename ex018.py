import math
from math import sin,cos,tan,radians

an = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {an} tem SENO de {sin(radians(an)): .2f}')
print(f'O ângulo de {an} tem COSSENO de {cos(radians(an)): .2f}')
print(f'O ângulo de {an} tem TANGENTE de {tan(radians(an)): .2f}')