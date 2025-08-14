frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Na frase foram encontradas {frase.count('A')} letras A')
print(f'A primeira letra A aparece na {frase.find('A')+1}º posição')
print(f'A última letra A aparece na {frase.rfind('A')+1}º posição')
