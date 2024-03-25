"""
Faça um programa que peça ao usuario para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, 
informe que não é um número inteiro.
# """
# print('-'*10, 'Sistema de Par ou Ímpar','-'*10)
# print('-'*45 ,'\n')
# opcao = 'y'

while opcao == 'y':

    try:
        num_int = int(input("digite um número inteiro: "))#variavel que recebe o numero digitado pelo usuario
        num_log = num_int % 2

        if num_log == 0:
            print('o número digitado é par')
            print('-'*5)
        else:
            print('o número digitado é impar')
            print('-'*5)
    except:
        print('não foi digitado um número inteiro')
        opcao = input('deseja tentar novamente? ')
        if opcao == 'n':
            print('fim do programa')




"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input('diga-me somente a hora, sem os minutos: '))

if  hora <= 11:
    print('bom dia')
elif hora <=17:
    print('boa tarde')
else:
    print('boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escrevea "seu nome é curto" ; se tiver entre 5 a 6 letras, eescreva
"Seu nome é normal" ; maior que 6 escreva "Seu nome é muito grande".
"""

name = input('diga-me o seu nome: ')
qtd_name = len(name)

if qtd_name <= 4:
    print('seu nome é curto')
elif qtd_name <= 6:
    print('seu nome é normal')
else:
    print('seu nome é comprido')
