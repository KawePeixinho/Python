import random #importando a biblioteca de numeros aleatórios

lista2 = ['nome', 'velho', 'idoso']
number_random = random.randint(0,2)

printar = lista2[number_random]

print(printar)

letra_digitada = input('digite uma letra: ')

comparar = letra_digitada in printar

if comparar:
    print('nice')
else:
    print('fail')




# lista3 = [
#     'nome','feijao','arroz','macarrao'
# ]

# palavra = 'arroz'

# letra_digitada = input('digite uma letra: ')

# comparar = letra_digitada in palavra

# print(comparar)