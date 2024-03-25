nome = input('qual o seu nome? ')
idade = int(input('qual a sua idade?'))

print('_'*15)

if nome and idade == ' ':
    print('Desculpe, voce deixou campos vazios.')
else:
    print(f'o seu nome é: {nome}')
    print('_'*15)
    print(f'o seu nome invertido é: {nome[::-1]}')
    print('_'*15)
    print(f'o seu nome contém espaços: {' ' in nome}')
    print('_'*15)
    print(f'o seu nome contém {len(nome)} letras')
    print('_'*15)
    print(f'a primeira letra do seu nome é: {nome[0]}')
    print('_'*15)
    print(f'a ultima letra do seu nome é: {nome[:0:-len(nome)]}') #indice [-1] funcionaria tbm
    