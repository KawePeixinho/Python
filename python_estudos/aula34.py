#if / elif / else
#se / se não se / se não

entrada = input('vc quer "entrar" ou "sair?" ')

while entrada != 'entrar' and entrada != 'sair':
    print('digite "entrar" ou "sair"'  '\n*'*20)
    #print('-'*20)
    entrada = input('vc quer entrar ou sair? ')

if entrada == 'entrar':
    print('vc entrou!!')
else:
    print('vc saiu :(')