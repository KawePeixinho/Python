import random #biblioteca de numeros aleatorios

number_random = random.randint(0, 30) #armazenamento dos numeros random do tipo int na variavel
print('='*15)
number_digit = int(input('diga-me um número: ')) #entrada de dados
print('='*15)


for chance in range(1, 5): #criação da variavel chance e quantidade repetidas, no caso será do 1 ao 4
    
    #verificação dos numeros

    if number_digit != number_random:
        if number_digit > number_random: #verificação se o numero é maior ou menor

            print(f'o numero secreto é menor que {number_digit}')
            number_digit = int(input('digite outro número: '))
            print('='*15)

        else:
            print(f'o numero secreto é maior que {number_digit}')
            number_digit = int(input('digite outro número: '))

            print('='*15)

    if number_digit == number_random:
        print('parabéns, vc acertou!')
        print('='*15)
        break
    if chance == 4: #caso a variavel chance seja = a 4, entenderá que a pessoa não acertou durante as 5 tentativas, exibindo a resposta
        print(f'o numero secreto era: {number_random}')
        print('='*15)
   
   
    #print(number_digit)
    #print(chance)
    #print(number_digit)