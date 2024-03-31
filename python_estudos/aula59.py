"""
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira 
Loop infinito -> quando um codigo nao tem fim
"""

bot1 = True

while bot1:
    nome = input('qual o seu nome? ')
    print(f'hello, {nome.capitalize()}')

    if nome == 'sair':
        break
print(f'acabou, {nome}')