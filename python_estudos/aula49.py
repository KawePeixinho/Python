"""
Introdução ao try / except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

nome = input('nome: ')
idade = input('idade: ')

try:
    print('-'*5, 'dados inseridos', '-'*5)
    print(f'nome: {nome}')
    idade = int(idade)
    print(f'idade: {idade}')
  
except:
    print('não foi digitado um número inteiro no campo "idade"')

