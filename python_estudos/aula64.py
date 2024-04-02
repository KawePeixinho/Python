"""
while / else
"""
palavra = 'arroz feijão'

i = 0
while i<len(palavra):
    letra=palavra[i]

    if letra == ' ':
        break

    print(letra)
    i+=1
else:
    print('não encontrei espaço')
print('fora do while, espaço encontrado')